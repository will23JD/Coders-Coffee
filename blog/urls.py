from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('like/<int:blog_id>', views.like_blog, name='like_blog'),
    path('comment/<int:blog_id>', views.comment, name='comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment,
         name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
