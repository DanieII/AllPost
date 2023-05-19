from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.contrib import messages

from posts.forms import CommentForm
from posts.models import Post, Comments


@login_required(login_url='login')
def posts(request):
    context = {
        'posts': Post.objects.all(),
        'user': request.user
    }
    return render(request, 'posts/posts.html', context)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.success(request, f"{post.title} deleted successfully")
    return redirect('posts')


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Handling the comment form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            post = Post.objects.get(pk=pk)
            comment = Comments.objects.create(user=request.user, post=post, content=content)
            comment.save()
            messages.success(request, "Comment added")

    # Create a new form in both cases because the post data doesn't need to be rendered again
    form = CommentForm()

    context = {
        'post': post,
        'comments': Comments.objects.filter(post=post),
        'form': form
    }

    return render(request, 'posts/post.html', context=context)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        return context


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
