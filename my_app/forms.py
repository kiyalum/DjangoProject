from django import forms
from .models import Student, Course, Article


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Subject', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'slug', 'description', 'price', 'level', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter a title of course...'}),
            'slug': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter slug of course...'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'rows': 4,
                                                 'placeholder': 'Enter a description of course...'}),
            'price': forms.NumberInput(attrs={'class': 'form-control',
                                              'step': 0.01}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if not price and price < 0:
            raise forms.ValidationError('Price cannot be negative')
        return price

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        if title and description and title.lower() in description.lower():
            pass
        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'slug', 'description', 'price', 'level', 'is_published']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',})
        }