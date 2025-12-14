from django.contrib.auth.models import User
from rest_framework import serializers
from users_orgs.models import Organization, UsersOrganizations

# Сериалайзер для Organization без пользователей
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

# Сериалайзер для User с организациями
class UserWithOrganizationsSerializer(serializers.ModelSerializer):
    organizations = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'organizations']

    def get_organizations(self, obj):
        # Получаем все связи пользователя с организациями
        user_orgs = UsersOrganizations.objects.filter(user=obj)
        # Возвращаем список названий организаций
        return [uo.organization.organization_name for uo in user_orgs]