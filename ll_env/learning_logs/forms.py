from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # widgets are HTML form elements to override the default choice
        # this is an 80 col wide text area instead of the default 40
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}