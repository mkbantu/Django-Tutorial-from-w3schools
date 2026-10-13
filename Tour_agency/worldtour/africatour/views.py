from django.shortcuts import render


def afritour1(request):
    return render(request, 'africa/index.html')