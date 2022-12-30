from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from student.models import Student
from student.forms import StudentForm


class IndexView(TemplateView):
    template_name = "index.html"


class StudentCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StudentForm
        return render(request, "add.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student-create")
        else:
            return render(request, "add.html", {"form": form})


class StudentListView(View):
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        return render(request, "list.html", {"todo": qs})


class StudentDetailView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        qs = Student.objects.get(id=id)
        return render(request, "detail.html", {"detail-student": qs})


class StudentDelete(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        Student.objects.get(id=id).delete()
        return redirect("list")

# Create your views here.
