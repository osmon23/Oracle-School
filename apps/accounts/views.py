from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import TeacherRegistrationForm, TeacherLoginForm, StudentForm


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


class CreateStudentView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method != 'GET':
            return HttpResponseNotAllowed(['GET'])
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = StudentForm()
        return render(request, 'accounts/add_student.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'accounts/add_student.html', {'form': form})
