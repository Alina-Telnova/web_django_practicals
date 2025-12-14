from django.urls import path
from . import views

urlpatterns = [
    # Организации
    path('organizations/', views.OrganizationListView.as_view(), name='org-list'),
    path('organizations/<int:pk>/', views.OrganizationDetailView.as_view(), name='org-detail'),
    path('organizations/create/', views.OrganizationCreateView.as_view(), name='org-create'),
    path('organizations/<int:pk>/update/', views.OrganizationUpdateView.as_view(), name='org-update'),
    path('organizations/<int:pk>/delete/', views.OrganizationDeleteView.as_view(), name='org-delete'),

    # Должности
    path('positions/', views.PositionListView.as_view(), name='position-list'),
    path('positions/<int:pk>/', views.PositionDetailView.as_view(), name='position-detail'),
    path('positions/create/', views.PositionCreateView.as_view(), name='position-create'),
    path('positions/<int:pk>/update/', views.PositionUpdateView.as_view(), name='position-update'),
    path('positions/<int:pk>/delete/', views.PositionDeleteView.as_view(), name='position-delete'),

    # Пользователи в организациях
    path('users/', views.UsersOrganizationsListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UsersOrganizationsDetailView.as_view(), name='user-detail'),
    path('users/create/', views.UsersOrganizationsCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', views.UsersOrganizationsUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', views.UsersOrganizationsDeleteView.as_view(), name='user-delete'),
]