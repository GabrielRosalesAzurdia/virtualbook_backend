from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#formulario de creacion de usuario
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name','country')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            user.save()
        
        return user

#formulario para actualizar la info de un usuario
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'is_active', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]

#formulario para actualizar la info de un cliente
class UserUpdateForm(forms.ModelForm):
    class Meta:
        ordering = ['-id']
        model = get_user_model()
        fields = (
            'first_name', 'last_name',
            'city','address_1',
            'address_2','region','postal_code',
            'country','day_phone',
            'eve_phone','mob_phone'
        )

#formulario para que el usuario actualize su tarjeta de credito
class UserUpdateCreditCartForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('credit_card',)