from django import forms
from posts.models import Category, Post, Tag


class PostForm(forms.Form):
    image = forms.ImageField(required = False)
    title = forms.CharField(required = True, max_length = 256) 
    content = forms.CharField(required = True, max_length = 456)


    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError("Title cannot be Python")
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title and title.lower() == content.lower():
            raise forms.ValidationError("Title and content cannot be the same")
        if content and content.isdigit():
            raise forms.ValidationError("Content cannot be a number")
        return cleaned_data
    

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']


class SearchForm(forms.Form):
    search = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False)
    orderigs = (
        ("rate", "Rate"), 
        ("-rate", "Rate (desc)"),
        ("created_at", "Created_at"),
        ("-created_at", "Created_at (desc)"),
        (None, None)
    )

    ordering = forms.ChoiceField(choices=orderigs, required=False)