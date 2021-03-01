from django.shortcuts import (render, get_object_or_404, redirect)
from django.utils import timezone
from blog.models import (Post)
from django.views.generic import (TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView,
                                        )
from blog.forms import (PostForm, )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.forms import formset_factory
from hitcount.views import HitCountDetailView





# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')


class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()[:5]
        context['post_views'] = ["ajax", "detail", "detail-with-count"]
        return context

class CreatePostView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView ):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name= 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publication_date__isnull = True).order_by('created_date')

class SearchPostView(ListView):
    template_name = 'post_list.html'

    def get_queryset(self):

        search_value = self.kwargs.get("urlsearch")
        if search_value:
            queryset = Post.objects.filter(title__icontains = search_value)
        else:
            queryset = Post.object.none()
        return queryset


@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('post_list')

