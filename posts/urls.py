from django.urls import path

from posts.views import posts, post_details, delete_post, edit_post, create_post, delete_comment

urlpatterns = [
    path('', posts, name='posts'),
    path('<int:pk>/', post_details, name='post'),
    path('create-post/', create_post, name='create'),
    path('update-post/<int:pk>/', edit_post, name='update'),
    path('delete-post/<int:pk>/', delete_post, name='delete'),
    path('delete-comment/<int:post_pk>/<int:comment_pk>/', delete_comment, name='delete comment'),
]
