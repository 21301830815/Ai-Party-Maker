from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def setup_mafia(request):
    if request.method == "POST":
        game = "mafia"
    return render(request, 'main\setup.html')
