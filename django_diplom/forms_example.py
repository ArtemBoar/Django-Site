from django import forms

class AddWorkerForm(forms.Form):
    name = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'})
    )

    class AddWorkerForm(forms.Form):
        surname = forms.CharField(
            max_length=128,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'surname'})
        )

    class AddWorkerForm(forms.Form):
        age = forms.CharField(
            default=19,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'age'})
        )


    class AddWorkerForm(forms.Form):
        specialist = forms.CharField(
            max_length=128,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'specialist'})
        )

    class AddManagerForm(forms.Form):
        language = forms.CharField(
            max_length=128,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'language'})
        )

    class AddManagerForm(forms.Form):
        name = forms.CharField(
            max_length=128,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'})
        )

        class AddManagerForm(forms.Form):
            surname = forms.CharField(
                max_length=128,
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'surname'})
            )

        class AddManagerForm(forms.Form):
            age = forms.CharField(
                default=19,
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'age'})
            )