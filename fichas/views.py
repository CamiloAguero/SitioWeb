from django.shortcuts import render

# Create your views here.
def fichas(request):
    return render(request,"fichas/fichas.html")