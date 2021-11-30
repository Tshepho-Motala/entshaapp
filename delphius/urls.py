from django.urls import path
from . import views

urlpatterns = [
    path('', views.delphius_home, name='delphius_home'),
    path('add_lead/', views.add_lead, name="add-lead"),
    path('view_lead/', views.view_lead, name="view-lead"),
    path('show_lead/<New_Lead_id>', views.show_lead, name="show-lead"),
    path('update_lead/<New_Lead_id>', views.update_lead, name="update-lead")
    
    
    ]

