from django import forms
from website.models import Contact, NewsLetter  

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContantForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'



class NameForm(forms.ModelForm):
    email = forms.EmailField()


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']
