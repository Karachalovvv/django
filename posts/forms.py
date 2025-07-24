from django import forms


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