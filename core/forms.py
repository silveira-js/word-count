from django import forms


class TextForm(forms.Form):
    text = forms.CharField(
        label="Word Counter", label_suffix="",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter your text here...',
                'class': 'form-class'
            }
        ),
        required=True,
        error_messages={"required": "Your text must not be empty"})
