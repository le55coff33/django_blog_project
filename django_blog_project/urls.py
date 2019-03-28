"""django_blog_project URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from blog.views import (PostListView,
                        PostDetailView,
                        PostCreateView,
                        PostUpdateView,
                        PostDeleteView,
                        CommentCreateView,
                        CommentUpdateView,
                        CommentDeleteView,
                        )

from user_profile import views as user_profile_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

urlpatterns += [
    path('comment/<int:pk>/new_comment/', CommentCreateView.as_view(), name='comment-create'),
    # path('post/<int:post_pk>/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    # path('post/<int:post_pk>/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', user_profile_views.register, name='register'),
    path('accounts/profile/', user_profile_views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
