from django import forms


class UploadPhotoForm(forms.Form):
    """Photo upload form."""
    title = forms.CharField(max_length=50)
    photofile = forms.ImageField(
        label='Select an image to upload'
        )
