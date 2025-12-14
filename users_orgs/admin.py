from django.contrib import admin
from .models import Organization, Position, UsersOrganizations

admin.site.register(Organization)
admin.site.register(Position)
admin.site.register(UsersOrganizations)