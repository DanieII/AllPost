from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from posts.models import Post


@login_required(login_url='login')
def posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/posts.html', context)


# class Posts(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'posts/posts.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')


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
