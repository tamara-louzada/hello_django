from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))


def soma(request, val1, val2):
    res = val1 + val2
    return HttpResponse('<h1>A soma de {} e {} é: {}</h1>'.format(val1, val2, res))

def multiplica(request, val1, val2):
    res = val1 * val2
    return HttpResponse('<h1>A multiplicação de {} e {} é: {}</h1>'.format(val1, val2, res))

