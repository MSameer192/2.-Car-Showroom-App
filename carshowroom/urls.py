from django.urls import path
from . import views

app_name = 'carshowroom'

urlpatterns = [
    path('', views.ShowroomListView, name='showroom_list'), # Add this line for showroom_list
    path('<int:showroom_id>', views.ShowroomDetails, name='showroom_detail'), # Add this line for car showroom detail
    path('<int:showroom_id>/our-team/', views.our_team, name='our_team'),  # New URL for Our Team page
    path('car_listing/<int:model_id>/', views.car_listing, name='car_listing'),  # Add this line for car listing
]

