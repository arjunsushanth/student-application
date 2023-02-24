from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView,CreateView,FormView
from student.models import Student
from student.forms import StudentForm,StudentRegistrationForm,StudentLoginForm
from django.urls import  reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



class IndexView(TemplateView):
    template_name = "index.html"
class LoginView(FormView):
    template_name = "login.html"
    form_class = StudentLoginForm
    def post(self, request, *args, **kwargs):
        form=StudentLoginForm

        def post(self, request, *args, **kwargs):
            form = StudentLoginForm(request.POST)
            if form.is_valid():
                uname = form.cleaned_data.get("username")
                pwd = form.cleaned_data.get("password")
                usr = authenticate(request, username=uname, password=pwd)
                if usr:
                    login(request, usr)
                    return redirect("home")
                else:
                    return render(request, "login.html", {"form": form})


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = StudentRegistrationForm
    success_url =reverse_lazy("home")



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


def Signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")# Create your views here.
