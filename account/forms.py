# from django import forms
# from .models import CustomUser
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.forms import AuthenticationForm


# class CustomUserCreationForm(UserCreationForm):

#     usable_password = None

#     username = forms.CharField(
#         label="Username",
#         max_length=25,
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
#                 "type": "text",
#                 "placeholder": "Usernamingizni kiriting...",
#             }
#         ),
#     )
#     email = forms.EmailField(
#         label="Email",
#         max_length=50,
#         required=True,
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
#                 "type": "email",
#                 "placeholder": "Emailingizni kiriting...",
#             }
#         ),
#     )
#     password1 = forms.CharField(
#         label="Parol",
#         widget=forms.HiddenInput(
#             attrs={
#                 "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
#                 "type": "password",
#                 "placeholder": "Parol oylab toping...",
#             }
#         ),
#     )
#     password2 = forms.CharField(
#         label="Parolni Tastiqlash",
#         widget=forms.HiddenInput(
#             attrs={
#                 "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
#                 "type": "password",
#                 "placeholder": "Parolni qaytaring...",
#             }
#         ),
#     )

#     class Meta:
#         model = CustomUser
#         fields = ("username", "email", "password1", "password2")


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(
#         label="Username",
#         max_length=25,
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "border rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
#                 "type": "text",
#                 "placeholder": "Usernamingizni kiriting...",
#             }
#         ),
#     )
#     password = forms.CharField(
#         label="Parol",
#         widget=forms.HiddenInput(
#             attrs={
#                 "class": "border rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
#                 "type": "password",
#                 "placeholder": "Parolingizni kiriting...",
#             }
#         ),
#     )

#     class Meta:
#         model = CustomUser
#         fields = ("username", "password")


# class CustomUserChangeForm(UserChangeForm):
#     username = forms.CharField(
#         label="Username",
#         max_length=25,
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "border rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
#                 "type": "text",
#                 "placeholder": "Username",
#             }
#         ),
#     )
#     email = forms.EmailField(
#         label="Email",
#         max_length=50,
#         required=True,
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "border rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
#                 "type": "email",
#                 "placeholder": "Email",
#             }
#         ),
#     )
#     password = forms.CharField(
#         widget=forms.HiddenInput(
#             attrs={
#                 "class": "border rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
#                 "type": "password",
#                 "placeholder": "Password",
#             }
#         ),
#     )

#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")
