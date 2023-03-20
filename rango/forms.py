from django import forms
from rango.models import Page, Movie, UserProfile
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the movie name.")
    releaseDate = forms.CharField(max_length=128, help_text="Please enter the movie release date.")
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Movie
        fields = ('title',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('https://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
