from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from posts.decorators import validate_post_user
from posts.forms import CommentForm, CreateUpdatePostForm
from posts.models import Post, Comment


@login_required(login_url='login')
def posts(request):
    context = {
        'posts': Post.objects.all(),
        'user': request.user
    }
    return render(request, 'posts/posts.html', context)


def create_post(request):
    if request.method == 'POST':
        form = CreateUpdatePostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(user=request.user, **form.cleaned_data)
            post.save()
            return redirect('posts')
    else:
        form = CreateUpdatePostForm()

    context = {
        'form': form,
        'action': 'Create'
    }
    return render(request, 'posts/post_form.html', context=context)


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Handling the comment form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            post = Post.objects.get(pk=pk)
            comment = Comment.objects.create(user=request.user, post=post, content=content)
            comment.save()
            messages.success(request, "Comment added")

    # Create a new form in both cases because the comment content doesn't need to be rendered again
    form = CommentForm()

    context = {
        'post': post,
        'comments': Comment.objects.filter(post=post),
        'form': form
    }

    return render(request, 'posts/post.html', context=context)


@validate_post_user
def edit_post(request, post):
    if request.method == 'POST':
        changed = []
        form = CreateUpdatePostForm(request.POST)
        if form.is_valid():
            new_fields = form.cleaned_data

            for field_name in new_fields:
                field_value = new_fields[field_name]
                old_value = getattr(post, field_name)

                if field_value != old_value:
                    setattr(post, field_name, field_value)
                    changed.append(field_name)

            post.save()
            if changed:
                messages.success(request, f'Changed: {", ".join(changed)}')
            else:
                messages.warning(request, 'Nothing changed')

            return redirect('posts')
    else:
        form = CreateUpdatePostForm(instance=post)

    context = {
        'form': form,
        'action': 'Edit'
    }
    return render(request, 'posts/post_form.html', context=context)


@validate_post_user
def delete_post(request, post):
    post.delete()
    messages.success(request, f"{post.title} deleted successfully")
    return redirect('posts')


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('post', pk=post_pk)
