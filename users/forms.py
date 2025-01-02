from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder':'Password'}))

class AdminUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    groups = forms.ModelChoiceField(
            queryset=Group.objects.all(), 
            required=True,
            widget=forms.Select(attrs={"class": "form-control"})
        )    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            
            # Create UserProfile
            profile = UserProfile.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                phone_number=self.cleaned_data['phone_number']
            )
            if self.cleaned_data['groups']:
                group = self.cleaned_data['groups']
                profile.groups.add(group)  # Add to profile
                user.groups.add(group) 
        return user



class AdminUserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    groups = forms.ModelChoiceField(
        queryset=Group.objects.all(), 
        required=True,
        widget=forms.Select(attrs={"class": "form-control"})
    )
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.instance, 'userprofile'):
            self.fields['groups'].initial = self.instance.userprofile.groups.all()
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            
            # Update or create UserProfile
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    'first_name': self.cleaned_data['first_name'],
                    'last_name': self.cleaned_data['last_name'],
                    'phone_number': self.cleaned_data['phone_number'],
                }
            )
            
            if not created:
                profile.first_name = self.cleaned_data['first_name']
                profile.last_name = self.cleaned_data['last_name']
                profile.phone_number = self.cleaned_data['phone_number']
                profile.save()
                
            if self.cleaned_data['groups']:
                group = self.cleaned_data['groups']
                profile.groups.set([group])  # Update UserProfile group
                user.groups.set([group])  # Update Django User groups
            else:
                profile.groups.clear()
                user.groups.clear()
        
        return user