from django import forms

from .models import ModelEntity, ProtocolEntity


class ModelEntityForm(forms.ModelForm):
    version = forms.CharField(max_length=255)
    commit_message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ModelEntity
        fields = ['name', 'version', 'commit_message', 'visibility']


class ProtocolEntityForm(forms.ModelForm):
    class Meta:
        model = ProtocolEntity
        fields = ['name']


class FileUploadForm(forms.Form):
    uploaded_file = forms.FileField()
