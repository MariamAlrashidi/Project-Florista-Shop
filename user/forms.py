from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .models import  Profile



class UserForm(UserCreationForm):
        
    class Meta: 
        model = User
        fields = ('username', 'first_name' , 'last_name' , 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image", "bio", "location")
# class PasswordForm(SetPasswordForm):
#     model = User
#     fields = ('password1', 'password1' )

#     def __init__(self, *args, **kwargs):
#         super(SetPasswordForm, self).__init__(*args, **kwargs)

#         for fieldname in form:
#             self.fields[fieldname].help_text = None

# class AccountUpdateForm(AccountCreationForm):

# 	class Meta:
# 		model = Account
# 		fields = ('email', 'username', )

# 	def clean_email(self):
# 		email = self.cleaned_data['email']
# 		try:
# 			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
# 		except Account.DoesNotExist:
# 			return email
# 		raise forms.ValidationError('Email "%s" is already in use.' % account)

# 	def clean_username(self):
# 		username = self.cleaned_data['username']
# 		try:
# 			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
# 		except Account.DoesNotExist:
# 			return username
# 		raise forms.ValidationError('Username "%s" is already in use.' % username)
