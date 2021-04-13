from django.test import TestCase, Client
from blog import views, models
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand
import datetime
from django.utils import timezone
from django.urls import reverse
from blog.models import Post
from django.utils.timezone import  now

client = Client()
# Create your tests here.

class TestUrls(TestCase):
    def setup(self):
        self.adminuser = User.objects.create_user('admin', 'admin@test.com', 'pass')
        self.adminuser.save()
        self.adminuser.is_staff = True
        self.adminuser.save()

    def test_AboutView_response(self):
        """Verifies if the response of the about view returns a status_code of 200.
        """
        response = client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)


    def test_PostListView_post_dates(self):
        """Verifies if all posts in post_list have post_date.
        """
        posts_list = client.get(reverse('post_list')).context['post_list']
        for i in posts_list:
            assert(posts_list[i].post_date != None or "" )

    def test_PostListView_response(self):
        """Verifies if the response code is a 200 code.
        """
        response = client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)


    def test_DraftListView_response(self):
        """Verifies if the response code of the DraftListView is a 302 code.
        """
        response = client.get(reverse("post_draft_list"))
        print(response)
        self.assertEqual(response.status_code, 302)

def create_Test_Post(Post, publication_date):
    test_post = Post
    test_post.publication_date = publication_date





class PostModelTests(TestCase):
    def test_publication_date(self):
        """Verifies if a published post has a published date"""
        post_pub_date_exists = False
        post_pub_date = Post.publication_date
        if post_pub_date != None and post_pub_date != "":
            post_pub_date_exists = True
        self.assertEqual(post_pub_date_exists, True)
        print("pub date is:", post_pub_date)






