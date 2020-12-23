from django.contrib import admin
from django.urls import path
from studentdetailsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('add_student/',views.add_student,name='add_student'),
    path('save_data/',views.save_data,name='save_data'),
    path('update_data/<pk>',views.update_data,name='update_data'),
    path('save_update_data/<pk>',views.save_update_data,name='save_update_data'),
    path('delete_data/<pk>',views.delete_data,name='delete_data')
]
