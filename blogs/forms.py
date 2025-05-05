from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'title': 'Enter a title for your blog post.',
            'content': 'Write your blog post here.',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'bad' in title.lower():
            raise forms.ValidationError("Title contains inappropriate word.")
        return title
