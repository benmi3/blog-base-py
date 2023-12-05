from django import forms


class CommentForm(forms.Form):
    comment_text = forms.CharField(label="Comment text")
    #fields = ('comment_author', 'comment_text', 'comment_post',)


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
