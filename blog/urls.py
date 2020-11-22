# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


        
urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<slug>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<slug>/publish/', views.post_publish, name='post_publish'),
    path('post/<urlsearch>/', views.SearchPostView.as_view(), name='searchfromurl'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


