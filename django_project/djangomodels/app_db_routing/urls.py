from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/app_db_routing/CreateStudentsData/
    # http://localhost:8000/app_db_routing/UpdateStudentNameByID/1/EEE
    # http://localhost:8000/app_db_routing/DeleteRecordByID/1
    # http://localhost:8000/app_db_routing/DeleteAllRecords/
    # http://localhost:8000/app_db_routing/GetAllRecords/
    # http://localhost:8000/app_db_routing/GetRecordByID/1
    # http://localhost:8000/app_db_routing/my_custom_sql/1

    path('', views.django_status),
    path('CreateStudentsData/', views.CreateStudentsData, name='CreateStudentsData'),
    path('UpdateStudentNameByID/<int:in_student_id>/<str:in_student_name>', views.UpdateStudentNameByID, name='UpdateStudentNameByID'),
    path('DeleteRecordByID/<int:in_student_id>', views.DeleteRecordByID, name='DeleteRecordByID'),
    path('DeleteAllRecords/', views.DeleteAllRecords, name='DeleteAllRecords'),
    path('GetAllRecords/', views.GetAllRecords, name='GetAllRecords'),
    path('GetRecordByID/<int:in_student_id>', views.GetRecordByID, name='GetRecordByID'),
    path('my_custom_sql/<int:in_student_id>', views.my_custom_sql, name='my_custom_sql'),    
]
