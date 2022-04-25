from django import forms

from core.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    # def clean(self) -> None:
    #  super().clean()
    #   data['user'] = User.objects.first()
       # return data 

   