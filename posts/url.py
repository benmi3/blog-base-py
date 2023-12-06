from django.urls import path

from . import views

app_name = "posts"  # namespace
urlpatterns = [
    # ex: /posts/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /posts/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /posts/5/results
    path("<int:pk>/category", views.CategoryView.as_view(), name="category"),
    # ex /posts/5/comment/
    path("<int:post_id>/comment/", views.comment, name="comment"),
]
