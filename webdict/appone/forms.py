from django import forms
from appone.models import DictWord

class FirstForm(forms.ModelForm):
    class Meta:
        model = DictWord
        #fields = "__all__"
        fields = ('name','description')

class SecondForm(forms.ModelForm):
    class Meta:
        model = DictWord
        #fields = "__all__"
        fields = ('name',)