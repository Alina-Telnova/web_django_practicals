from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Organization(models.Model):
    organization_name = models.CharField(max_length=50, null=False)
    founding_date = models.DateField(null=False)
    address = models.CharField(max_length=200, null=False)
    director_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.organization_name

class Position(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class UsersOrganizations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    hire_date = models.DateTimeField(default=timezone.now)
    position = models.ForeignKey(Position, on_delete=models.SET_DEFAULT, default=1)  
    dismissal_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'organization') 

    def __str__(self):
        return f"{self.user.username} в {self.organization.organization_name} как {self.position.name}"