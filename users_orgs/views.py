from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Organization, Position, UsersOrganizations
from django.contrib.auth.models import User
from .forms import OrganizationForm, PositionForm, UsersOrganizationsForm

# ===== Организации =====

class OrganizationListView(ListView):
    model = Organization
    template_name = 'users_orgs/list_orgs.html'
    context_object_name = 'organizations'

class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'users_orgs/detail_org.html'
    context_object_name = 'organization'

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'users_orgs/create_org.html'
    success_url = reverse_lazy('org-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'users_orgs/update_org.html'
    success_url = reverse_lazy('org-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'users_orgs/delete_org.html'
    success_url = reverse_lazy('org-list')

# ===== Должности =====

class PositionListView(ListView):
    model = Position
    template_name = 'users_orgs/list_positions.html'
    context_object_name = 'positions'

class PositionDetailView(DetailView):
    model = Position
    template_name = 'users_orgs/detail_position.html'
    context_object_name = 'position'

class PositionCreateView(CreateView):
    model = Position
    form_class = PositionForm
    template_name = 'users_orgs/create_position.html'
    success_url = reverse_lazy('position-list')

class PositionUpdateView(UpdateView):
    model = Position
    form_class = PositionForm
    template_name = 'users_orgs/update_position.html'
    success_url = reverse_lazy('position-list')

class PositionDeleteView(DeleteView):
    model = Position
    template_name = 'users_orgs/delete_position.html'
    success_url = reverse_lazy('position-list')

# ===== Пользователи в организациях  =====

class UsersOrganizationsListView(ListView):
    model = UsersOrganizations
    template_name = 'users_orgs/list_users.html'
    context_object_name = 'user_orgs'

class UsersOrganizationsDetailView(DetailView):
    model = UsersOrganizations
    template_name = 'users_orgs/detail_user.html'
    context_object_name = 'user_org'

class UsersOrganizationsCreateView(CreateView):
    model = UsersOrganizations
    form_class = UsersOrganizationsForm
    template_name = 'users_orgs/create_user.html'
    success_url = reverse_lazy('user-list')

class UsersOrganizationsUpdateView(UpdateView):
    model = UsersOrganizations
    form_class = UsersOrganizationsForm
    template_name = 'users_orgs/update_user.html'
    success_url = reverse_lazy('user-list')

class UsersOrganizationsDeleteView(DeleteView):
    model = UsersOrganizations
    template_name = 'users_orgs/delete_user.html'
    success_url = reverse_lazy('user-list')