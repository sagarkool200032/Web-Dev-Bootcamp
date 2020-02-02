from django import forms
from django.core import validators

# custom validator
def checkZ(value):
    if value[0].lower() != "z":raise forms.ValidationError("Start With Z")

class formName(forms.Form):
    name = forms.CharField(validators=[checkZ])
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label="Enter your Email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    
    # custom validator
    # clean one field 
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if(len(botcatcher)>0):
    #         raise forms.ValidationError("Elliot We got YOU !")
    #     return botcatcher

    # built-in validator using validators used in botcatcher

    #clean entire form
    def clean(self):
        allClean = super().clean()
        email = allClean['email']
        vemail = allClean['verifyEmail']
        if(email!=vemail):raise forms.ValidationError("Email Does'nt match")
