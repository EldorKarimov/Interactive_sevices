from django import forms
from .models import SendData, AnswerData

class SendDataForm(forms.ModelForm):
    class Meta:
        model = SendData
        fields = (
            'full_name',
            'email',
            'phone',
            'leader',
            'faculty',
            'direction',
            'subject',
            'message',
            'upload'
        )

class AnswerDataForm(forms.ModelForm):
    class Meta:
        model = AnswerData
        fields =[
            'answer'
        ]