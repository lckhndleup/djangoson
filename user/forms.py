from django import forms



class LoginForm(forms.Form):
    username=forms.CharField(label="kullanıcı adı")
    password=forms.CharField(label="parola",widget=forms.PasswordInput)

class RegisterForm(forms.Form):

    username = forms.CharField(max_length=50,label="kullanıcı adı")
    password = forms.CharField(max_length=20,label="parola",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="parolayı doğrula",widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError("parolalar eşleşmiyor!!!")
    
        values = {
            "username" : username,
            "password" : password
            }
        return values
