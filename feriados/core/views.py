from django.shortcuts import render
from datetime import datetime

def natal(request):
    contexto = {"natal": True, "carnaval": False}
    return render(request, 'natal.html', contexto)

def tiradentes(request):
    contexto = {"tiradentes": True, "outroferiado": False}
    return render(request, 'tiradentes.html', contexto)