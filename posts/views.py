import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post, Comment  # Category  # add this later


class IndexView(generic.ListView):
    template_name = "posts/index.html"
    context_object_name = "latest_posts_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = "posts/detail.html"

    def get_queryset(self):
        """
        Exclude any questions that are not published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Post
    template_name = "posts/results.html"


def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        new_comment = Comment(
            comment_author="TODO_test_user_hard_coded",  # TODO: add author auth
            comment_post=post,
            pub_date=datetime.datetime.now(),
            comment_text=request.POST["comment_text"],
            approved_comment=True,  # TODO: create a trust system
        )
        new_comment.save()
        # redirect to a new URL:
        return HttpResponseRedirect(reverse("posts:detail", args=(post.id,)))

    return HttpResponseRedirect(reverse("posts:detail", args=(post.id,)))
