from django.urls import path

from posts.views import posts, post_details, PostUpdateView, PostDeleteView, PostCreateView, comment

urlpatterns = [
    path('', posts, name='posts'),
    path('<int:pk>/', post_details, name='post'),
    path('update-post/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete-post/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('create-post/', PostCreateView.as_view(), name='create'),
    path('add-comment/<int:pk>', comment, name='comment'),
]
