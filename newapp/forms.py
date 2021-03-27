from django import forms
from django.forms import CharField
from .models import Books,Post
from datetime import datetime

class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ['name', 'description', 'price']
    
    def save(self, *args, **kwargs):
        obj = super(BookForm, self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        obj.save()


class TestForm(forms.Form):
    title = CharField(
        initial='',
        label='タイトル',
        max_length=10,
        required=True,  # 必須
    )
    comment = CharField(
        initial='',
        label='コメント',
        max_length=100,
        required=True,  # 必須
    )
    def save(self):
        # save data using the self.cleaned_data dictionary
        data = self.cleaned_data
        post = Post(
            title=data['title'], 
            comment=data['comment']
        )
        post.save()

