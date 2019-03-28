from django.db import models

from django.utils import timezone

from user_profile.models import User

from django.urls import reverse


class Post(models.Model):
    """Model representing a post"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # Return url to the PostUpdateView
    def get_absolute_url_to_update(self):
        return reverse('post-update', kwargs={'pk': self.pk})

    # Return url to the PostDeleteView
    def get_absolute_url_to_delete(self):
        return reverse('post-delete', kwargs={'pk': self.pk})

    # Return url to the CommentCreateView with pk of the post
    # The comment will be associated with the post
    def get_absolute_url_to_new_comment(self):
        return reverse('comment-create', kwargs={'pk': self.pk})

    # Return a list of comments associated with the post
    def get_comments_list(self):
        return Comment.objects.filter(post__id=self.pk)

    # Return a list that contains just two first comments associated with the post
    def get_two_first_comments(self):
        return Comment.objects.filter(post__id=self.pk)[:2]


class Comment(models.Model):
    """Model representing a comment"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_body = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Post TITLE: { self.post.title}, Comment ID: {self.id}'

    # We use get_absolute_url to dynamically redirect to the corresponding post
    # when a new comment has been created (CommentCreateView)
    def get_absolute_url(self):
        return self.get_absolute_url_to_the_post()

    # Return a full url to the DetailView of the post associated with the comment.
    # The'pk' is the pk of the post
    def get_absolute_url_to_the_post(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})

    # Return a full url to the CommentUpdateView
    def get_absolute_url_to_update(self):
        return reverse('comment-update', kwargs={'pk': self.pk})

    # Return a full url to the CommentDeleteView
    def get_absolute_url_to_delete(self):
        return reverse('comment-delete', kwargs={'pk': self.pk})

