from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, CreateView

from posts.forms import CommentForm
from posts.models import Post, Comments


@login_required(login_url='login')
def posts(request):
    context = {
        'posts': Post.objects.all(),
        'user': request.user
    }
    return render(request, 'posts/posts.html', context)


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
        'comments': Comments.objects.filter(post=post)
    }
    return render(request, 'posts/post.html', context)


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


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')


def comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            post = Post.objects.get(pk=pk)
            comment = Comments.objects.create(user=request.user, post=post, content=content)
            comment.save()
            return redirect(reverse('post', kwargs={'pk': pk}))
    else:
        form = CommentForm()

    return render(request, 'posts/comment.html', context={'form': form})
