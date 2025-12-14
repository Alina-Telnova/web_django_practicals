from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count

from users_orgs.models import Organization, UsersOrganizations
from .serializers import OrganizationSerializer, UserWithOrganizationsSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @action(detail=False, methods=['get'], url_path='many-employees')
    def many_employees(self, request):

        orgs_with_count = (
            UsersOrganizations.objects
            .values('organization')
            .annotate(employee_count=Count('user'))
            .order_by('-employee_count')[:10]
        )


        org_ids = [item['organization'] for item in orgs_with_count]
        orgs = Organization.objects.filter(id__in=org_ids)


        count_dict = {item['organization']: item['employee_count'] for item in orgs_with_count}


        data = []
        for org in orgs:
            org_data = OrganizationSerializer(org).data
            org_data['employee_count'] = count_dict[org.id]
            data.append(org_data)

        return Response(data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWithOrganizationsSerializer