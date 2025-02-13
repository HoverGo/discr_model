from main.models import ObjectsDiscr, DiscrMatr


def get_all_objects():
    objects = ObjectsDiscr.objects.all()
    return objects


def get_object(request, id):
    user = request.user

    if not user.is_authenticated:
        data = {
            'title': "Error! Not authorized",
            'object': None,
            'successfull': False,
            'error': "User not authorized",
        }
        return data
    
    discr_object = ObjectsDiscr.objects.filter(id=id).first()

    if not discr_object:
        data =  {
            'title': "Error! Not found",
            'object': None,
            'successfull': False,
            'error': "Object not found",
        }

        return data

    discr_matr = DiscrMatr.objects.filter(user=user, discr_object=discr_object)


    if (len(discr_matr) == 0 or not discr_matr.first().read) and (user != discr_object.owner):
        data = {
            'title': "Error! Not allowed",
            'object': None,
            'successfull': False,
            'error': "Access not allowed",
        }
        return data
    
    if (discr_object.owner == user) or (discr_matr.first().write):
        can_write = True
    else:
        can_write = False

    data = {
        'title': "Error! Not allowed",
        'object': discr_object,
        'write': can_write,
        'successfull': True,
        'error': None,
    }
    
    return data
     
