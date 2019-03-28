from .models import Post, Comment

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import get_object_or_404

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'post_body']
    success_message = 'Post has been created'

    # Set actual logged user as the author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'post_body']
    success_message = 'Post has been updated'

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post has been deleted')
        return super().delete(request, *args, **kwargs)


class CommentCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment_body']
    success_message = 'Comment has been created'

    # Set actual logged user as the author of the post
    # Bind the comment with the post 'pk'
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['pk'])
        return super().form_valid(form)


class CommentUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['comment_body']
    success_message = 'Comment has been updated'

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        return False

    # Set success_url to the PostDetailView of the associated post
    def get_success_url(self):
        self.success_url = reverse('post-detail', kwargs={'pk': self.get_object().post.id})
        return super().get_success_url()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Comment has been deleted')
        return super().delete(request, *args, **kwargs)

