from django.urls import path

from posts.views import posts, post_details, PostUpdateView, PostCreateView, delete_post

urlpatterns = [
    path('', posts, name='posts'),
    path('<int:pk>/', post_details, name='post'),
    path('update-post/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete-post/<int:pk>/', delete_post, name='delete'),
    path('create-post/', PostCreateView.as_view(), name='create'),
]
