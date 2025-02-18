from django.contrib import admin
from .models import Objects, DiscrMatr, Roles, UserRoles, RoleMatr

admin.site.register(Objects)

# Discret model
admin.site.register(DiscrMatr)

# Role model
admin.site.register(Roles)
admin.site.register(UserRoles)
admin.site.register(RoleMatr)