from django.shortcuts import render, redirect
from datetime import date

dia_hoje = date.today().strftime('%d/%m')

dia_hoje = '21/04'

def natal(request):
    contexto = {
        'natal': True if dia_hoje == '25/12' else False
    }
    return render(request, 'natal.html', contexto)

def tiradentes(request):
    contexto = {
        'tiradentes': True if dia_hoje == '21/04' else False
    }
    return render(request, 'tiradentes.html', contexto)

def redireciona(request):
    return render(request, 'tiradentes.html')