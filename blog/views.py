from django.shortcuts import (render, get_object_or_404, redirect)
from django.utils import timezone
from blog.models import (Post, Comment)
from django.views.generic import (TemplateView,
                                  ListView, DetailView, 
                                  CreateView, UpdateView,
                                  DeleteView,
                                        )
from blog.forms import (PostForm, CommentForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'
    
    
class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')
    
class PostDetailView(DetailView):
    model = Post
    

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
    
###Comment views###       

@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('post_list')

def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_approve(request, slug):
    comment = get_object_or_404(Comment, slug=slug)
    comment.approve()
    return redirect('post_detail', slug=comment.post.slug)

@login_required
def comment_remove(request, slug):
    comment = get_object_or_404(Comment, slug=slug)
    post_slug = comment.post.slug
    comment.delete()
    return redirect('post_detail', slug=post_slug)