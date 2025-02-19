from main.models import Objects, DiscrMatr, RoleMatr, UserRoles
from django.shortcuts import get_object_or_404
from django.db.models import Q
from functools import reduce
from operator import or_

def get_all_objects():
    objects = Objects.objects.all()
    return objects

def check_auth(user):
    if not user.is_authenticated:
        data = {
            'title': "Error! Not authorized",
            'object': None,
            'successfull': False,
            'error': "User not authorized",
        }
        return data
    
    return None

def get_discr_object(request, id):
    user = request.user

    auth_error = check_auth(user)
    if auth_error:
        return auth_error
    
    discr_object = get_object_or_404(Objects, id=id)

    discr_matr = DiscrMatr.objects.filter(user=user, object=discr_object).first()


    if (not discr_matr or not discr_matr.read) and (user != discr_object.owner):
        data = {
            'title': "Error! Not allowed",
            'object': None,
            'successfull': False,
            'error': "Access not allowed",
        }
        return data
    
    can_write = (discr_object.owner == user) or (discr_matr and discr_matr.write)

    data = {
        'title': "Success",
        'object': discr_object,
        'write': can_write,
        'successfull': True,
        'error': None,
    }
    
    return data


def get_role_object(request, id):
    user = request.user

    auth_error = check_auth(user)
    if auth_error:
        return auth_error
    
    role_object = get_object_or_404(Objects, id=id)
    user_roles = UserRoles.objects.filter(user=user)
    
    data = {
            'title': "Success",
            'object': role_object,
            'write': True,
            'successfull': True,
            'error': None,
        }

    if role_object.owner == user:
        
        return data

    if len(user_roles) == 0:
        data = {
            'title': "Error! Users have no roles and this is not its object",
            'object': None,
            'successfull': False,
            'error': "User has no roles",
        }
        return data


    has_read_permission = RoleMatr.objects.filter(
        object=role_object,
        read=True,
        role_id__in=user_roles.values_list('role_id', flat=True)
    ).first()

    if not has_read_permission:
        data = {
            'title': "Error! Not allowed",
            'object': None,
            'successfull': False,
            'error': "Access not allowed",
        }
        return data
    
    can_write = has_read_permission and has_read_permission.write
    data['write'] = can_write

    return data


def get_mandat_object(request, id):
    user = request.user

    auth_error = check_auth(user)
    if auth_error:
        return auth_error
    
    user_access_class = user.access_class
    role_object = get_object_or_404(Objects, id=id)
    object_access_class = role_object.class_object

    if object_access_class <= user_access_class:
        data = {
                'title': "Success",
                'object': role_object,
                'write': True,
                'successfull': True,
                'error': None,
            }
    else:
        data = {
            'title': "Error! Not allowed",
            'object': None,
            'write': False,
            'successfull': False,
            'error': "Access not allowed",
        }

    return data
