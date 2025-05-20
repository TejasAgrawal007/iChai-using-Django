from django.shortcuts import render

# Create your views here.

def allChai(request):
    return render(request, 'allChai.html')