from django.shortcuts import render
from .services.services import get_all_objects, get_object

def main(request):
    data = {
        "title": "Главная страница"
    }

    objects = get_all_objects()
    data['objects'] = objects

    return render(request, 'main/index.html', data)


def object_info(request, id):
    data = get_object(request, id=id)

    return render(request, 'main/object.html', data)
