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
    
    discr_object = ObjectsDiscr.objects.filter(id=id)

    if len(discr_object) == 0:
        data =  {
            'title': "Error! Not found",
            'object': None,
            'successfull': False,
            'error': "Object not found",
        }

        return data

    discr_matr = DiscrMatr.objects.filter(user=user, discr_object=discr_object[0])


    if len(discr_matr) == 0 or not discr_matr.first().read:
        data = {
            'title': "Error! Not allowed",
            'object': None,
            'successfull': False,
            'error': "Access not allowed",
        }
        return data
    
    data = {
        'title': "Error! Not allowed",
        'object': discr_object[0],
        'write': discr_matr.first().write,
        'successfull': True,
        'error': None,
    }
    
    return data
     
