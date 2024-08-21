# from django.shortcuts import redirect, render
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
# from .forms import CustomUserCreationForm, LoginForm
# from django.views.generic.edit import CreateView

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "account/signup.html"

#     def form_valid(self, form):
#         user = form.save()
#         user.save()

#         return redirect(self.success_url)

#     def form_invalid(self, form):
#         form.add_error("title")
    

# class CustomLoginView(LoginView):
#     form_class = LoginForm
#     template_name = "account/login.html"
#     success_url = reverse_lazy("home")

#     def form_invalid(self, form):
#         return render(
#             self.request,
#             "account/login.html",
#             {"error": "Incorrect Credentials.", "form": form},
#         )
