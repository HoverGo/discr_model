from django.shortcuts import render, redirect
from .services.services import get_all_objects, get_discr_object, get_role_object

def main(request):
    data = {
        "title": "Главная страница"
    }
    return redirect("discret_model")
    return render(request, 'main/index.html', data)


def discret_model(request):
    data = {
        "title": "Дискретная модель"
    }

    objects = get_all_objects()
    data['objects'] = objects

    return render(request, 'main/discret_model.html', data)


def role_model(request):
    data = {
        "title": "Ролевая модель"
    }

    objects = get_all_objects()
    data['objects'] = objects   

    return render(request, 'main/role_model.html', data)


def object_info(request, model, id):
    if model == 'discret':
        data = get_discr_object(request, id=id)
    elif model == 'role':
        data = get_role_object(request, id=id)

    return render(request, 'main/object.html', data)