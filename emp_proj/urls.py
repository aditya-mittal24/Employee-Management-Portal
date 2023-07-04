from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_all/',views.view_all, name="view_all"),
    path('add_emp/', views.add_emp, name="add_emp"),
    path('update_emp/', views.update_emp, name="update_emp"),
    path('update_emp/<int:id>', views.update_form, name="update_form"),
    path('remove_emp/', views.remove_emp, name="remove_emp"),
    # path('remove_emp/<int:id>', views.delete_emp, name="delete_emp"),
    path('delete_emp/',views.delete_emp, name="delete_emp"),
]
