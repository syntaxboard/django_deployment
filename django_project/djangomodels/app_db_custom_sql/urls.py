from django.conf.urls import include, url
from django.urls import path
# from . import model_students
from . import views

urlpatterns = [
    path('GetStudentByID/<int:in_student_id>', views.GetStudentByID),
    path('CreateStudentsData/', views.CreateStudentsData),
    path('UpdateStudentNameByID/<int:in_student_id>/<str:in_student_name>', views.UpdateStudentNameByID),
    path('DeleteRecordByID/<int:in_student_id>', views.DeleteRecordByID),
]

# http://localhost:8000/app_db_custom_sql/CreateStudentsData/
# http://localhost:8000/app_db_custom_sql/GetStudentByID/11
# http://localhost:8000/app_db_custom_sql/UpdateStudentNameByID/11/EEE
# http://localhost:8000/app_db_custom_sql/DeleteRecordByID/11
