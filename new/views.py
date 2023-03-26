from django.shortcuts import render
from django.http import HttpResponse


def my_veiw(request):
    return HttpResponse("<h1> Ataullah Sediqi</h1>")
