from django.shortcuts import get_object_or_404, redirect

from posts.models import Post


def validate_post_user(func):
    def wrapper(request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.user != post.user:
            return redirect('posts')

        return func(request, post, *args, **kwargs)

    return wrapper
