from django.db.models import Q
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView, UpdateView

from .forms import GradeForm, SearchForm
from .models import Grade
from apps.accounts.models import Student
from ..accounts.forms import StudentForm


class GradeView(View):
    def get(self, request):
        grades = Grade.objects.all()
        students = Student.objects.all()

        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_students = Student.objects.filter(
                Q(full_name__icontains=query) |
                Q(email__icontains=query) |
                Q(grade__icontains=query) |
                Q(address__icontains=query)
            )

            return render(request, 'school/index.html', {
                'grades': grades,
                'students': students,
                'form': form,
                'search_students': search_students,
            })

        return render(request, 'school/index.html', {'grades': grades, 'students': students})


class CreateGradeView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method != 'GET':
            return HttpResponseNotAllowed(['GET'])
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = GradeForm()
        return render(request, 'school/create_grade.html', {'form': form})

    def post(self, request):
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'school/create_grade.html', {'form': form})


class StudentDetailView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        return render(request, 'school/detail.html', {'student': student})


class StudentEditView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/update_student.html'

    def form_valid(self, form):
        form.save()
        return redirect('detail', pk=self.object.pk)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'school/delete_student.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())
