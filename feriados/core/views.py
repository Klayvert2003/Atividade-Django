from django.shortcuts import render
from datetime import date

dia_hoje = date.today().strftime('%d/%m')
dia_tiradentes = date(day=21, month=4, year=date.today().year)
dia_natal = date(day=25, month=12, year=date.today().year)
# dia_hoje = '25/12'
# dia_hoje = '21/04'

def natal(request):
    contexto = {
        'natal': True if dia_hoje == dia_natal.strftime('%d/%m') else False
    }
    return render(request, 'natal.html', contexto)

def tiradentes(request):
    contexto = {
        'tiradentes': True if dia_hoje == dia_tiradentes.strftime('%d/%m') else False
    }
    return render(request, 'tiradentes.html', contexto)