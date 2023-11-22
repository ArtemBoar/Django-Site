from django import forms

class AddWorkerForm(forms.Form):
    name = forms.CharField(
        max_length=128,
        label='Ім\я',
        widget=forms.TextInput(attrs={'placeholer': 'Ім\я'})
    )

    surname = forms.CharField(
        max_length=128,
        label='Призвище',
        widget=forms.TextInput(attrs={'placeholer': 'Прізвище'})
    )

    age = forms.CharField(
        max_length=128,
        label='Вік',
        widget=forms.TextInput(attrs={'placeholder': 'Вік'})
    )

    specialist = forms.CharField(
        max_length=128,
        label='Спеціальність',
        widget=forms.TextInput(attrs={'placeholer': 'Спеціальність'})
    )

    language = forms.CharField(
        max_length=128,
        label='Мова Програмування',
        widget=forms.TextInput(attrs={'placeholer': 'Мова Програмування'})
    )




class AddManagerForm(forms.Form):
    name = forms.CharField(
        max_length=128,
        label='Ім\я',
        widget=forms.TextInput(attrs={'placeholer': 'Ім\я'})
    )

    surname = forms.CharField(
        max_length=128,
        label='Призвище',
        widget=forms.TextInput(attrs={'placeholer': 'Прізвище'})
    )

    age = forms.CharField(
        max_length=128,
        label='Вік',
        widget=forms.TextInput(attrs={'placeholder': 'Вік'})
    )




class AddCompanyForm(forms.Form):
    name = forms.CharField(
        max_length=128,
        label='Назва Компанії',
        widget=forms.TextInput(attrs={'placeholer': 'Назва Компанії'})
    )

    balance = forms.CharField(
        max_length=128,
        label='Баланс Компанії',
        widget=forms.TextInput(attrs={'placeholer': 'Баланс Компанії'})
    )





class FilterWorkerForm(forms.Form):
    age_from = forms.IntegerField(required=False, label='Age From')
    age_to = forms.IntegerField(required=False, label='Age To')

class FilterManagerForm(forms.Form):
    age_from = forms.IntegerField(required=False, label='Age From')
    age_to = forms.IntegerField(required=False, label='Age To')
