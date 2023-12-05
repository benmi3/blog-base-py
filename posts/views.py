from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post, Comment  # Category  # add this later
from .forms import CommentForm


class IndexView(generic.ListView):
    template_name = "posts/index.html"
    context_object_name = "latest_posts_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(
    generic.edit.FormMixin,
    generic.DetailView,
):
    model = Post
    template_name = "posts/detail.html"
    form_class = CommentForm
    success_url = "/detail/"

    def get_queryset(self):
        """
        Exclude any questions that are not published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Post
    template_name = "posts/results.html"


def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        selected_choice = post.choice_set.get(pk=request.POST["comment"])
    except (KeyError, Comment.DoesNotExist):
        return render(
            request,
            "posts/detail.html",
            {
                "question": post,
                "error_message": "You did not select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse("posts:results", args=(post.id,)))


def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print(f"here is the form -------\n{form}\n----------------------")
            #post_comment = form.comment_text
            #try:
            comment_object = post.comment_set.get(pk=request.POST["comment_text"])
            #except:
            #    comment_object = None
            new_comment = Comment(
                comment_author="TODO_test_user_hard_coded",  # TODO: add author auth
                comment_post=post,
                comment_text=comment_object,
                approved_comment=True,  # TODO: create a trust system
            )
            new_comment.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("posts:detail", args=(post.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()

    return render(request, "posts/comment.html",
                  {
                      "form": form,
                      "post": post,
                  })
