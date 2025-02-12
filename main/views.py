from django.shortcuts import render

def main(request):
    data = {
        "title": "Главная страница"
    }
    return render(request, 'main/index.html', data)
