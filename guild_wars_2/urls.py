"""
URL configuration for guild_wars_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static
#from blog.models import Comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('terms/', views.terms_and_conditions, name='terms-and-conditions'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('topics/', views.TopicListView.as_view(), name='topic-list'),
    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic-detail'),
    path('form-example/', views.form_example, name='form-example'),
    path('formview-example/', views.FormViewExample.as_view(), name='formview-example'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contest/', views.PhotoContestSubmissionFormView.as_view(), name='contest'),
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('comments/<int:pk>/like/', views.comment_like, name='comment-like'),
    path('comments/<int:pk>/dislike/', views.comment_dislike, name='comment-dislike'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
