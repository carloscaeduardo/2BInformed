from django.test import TestCase, Client
from blog import views, models
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

# store the password to login later

client = Client()
# Create your tests here.
class TestUrls(TestCase):
    def setup(self):
        self.adminuser = User.objects.create_user('admin', 'admin@test.com', 'pass')
        self.adminuser.save()
        self.adminuser.is_staff = True
        self.adminuser.save()
    
    def test_AboutView_response(self):
        """Verifies if the response
        """
        response = client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    
    def test_PostListView_post_dates(self):
        """Verifies if all posts in post_list have post_date. 
        """
        posts_list = client.get(reverse('post_list')).context['post_list']
        for i in posts_list:
            assert(posts_list[i].post_date != null or "" )
    
    def test_PostListView_response(self):
        """Verifies if the response
        """
        response = client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)

    
    
    def test_DraftListView_response(self):
        """Verifies if the response
        """
        response = client.get(reverse("post_draft_list"))
        print(response)
        self.assertEqual(response.status_code, 302)
        
    # def test_DraftListView_missing_post_date(self):
    #     """ Asserts that DraftListView posts have no post_date.
    #     """
    #     draft_list = client.get(reverse("post_draft_list")).context['Draft']
          
        
        
        
    