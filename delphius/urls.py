from django.urls import path
from . import views

urlpatterns = [
    path('', views.delphius_home, name='delphius_home'),
    path('add_lead/', views.add_lead, name="add-lead"),
    path('view_lead/', views.view_lead, name="view-lead"),
    path('show_lead/<New_Lead_id>', views.show_lead, name="show-lead"),
    path('update_lead/<New_Lead_id>', views.update_lead, name="update-lead"),
    path('forms/', views.show_forms, name="show-forms"),
    path('add_project/', views.add_project, name="add-project"),
    path('view_project/', views.view_project, name="view-project"),
    path('show_project/<New_Project_id>', views.show_project, name="show-project"),
    path('update_project/<New_Project_id>', views.update_project, name="update-project"),
    path('add_validation/', views.add_validation, name="add-validation"),
    path('view_validation/', views.view_validation, name="view-validation"),
    path('show_validation/<New_Validation_id>', views.show_validation, name="show-validation"),
    path('update_validation/<New_Validation_id>', views.update_validation, name="update-validation"),
    path('add_radio/', views.add_radio, name="add-radio"),
    path('view_radio/', views.view_radio, name="view-radio"),
    path('show_radio/<Radio_Planner_id>', views.show_radio, name="show-radio"),
    path('update_radio/<Radio_Planner_id>', views.update_radio, name="update-radio"),
    path('add_ILO/', views.add_radio, name="add-radio"),
    path('view_radio/', views.view_radio, name="view-radio"),
    path('show_radio/<Radio_Planner_id>', views.show_radio, name="show-radio"),
    path('update_radio/<Radio_Planner_id>', views.update_radio, name="update-radio"),

    ]

