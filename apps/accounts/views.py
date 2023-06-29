from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import CreateView

from .models import Student
from .utils import send_newsletter
from .forms import TeacherRegistrationForm, TeacherLoginForm, StudentForm, NewsletterForm


class TeacherRegistrationView(View):
    def get(self, request):
        form = TeacherRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.is_staff = True
            form.save()
            return redirect('login')
        return render(request, 'accounts/register.html', {'form': form})


class TeacherLoginView(View):
    def get(self, request):
        form = TeacherLoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid phone number or password.')
        return render(request, 'accounts/login.html', {'form': form})


class TeacherLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class CreateStudentView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'accounts/add_student.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.photo = self.request.FILES.get('photo')
        return super().form_valid(form)


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_newsletter(subject, message)
            return render(request, 'accounts/success.html')
    else:
        form = NewsletterForm()
    return render(request, 'accounts/mailing.html', {'form': form, 'subject': '', 'message': ''})
