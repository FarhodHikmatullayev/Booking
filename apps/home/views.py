from django.shortcuts import render


def home(request):


    ctx = {

    }
    return render(request, 'home/index.html', ctx)
