from django.conf.urls import include, url
from django.urls import path
from . import views


urlpatterns = [
    # path("updateMany",views.updateMany),
    path("get_student_details",views.GetAllStudents.as_view()),
    path("insert_student_details", views.InsertStudentData.as_view()),
    path("update_student_details/<int:pk>",views.UpdateStudentData.as_view()),
    path("delete_student_details/<int:pk>",views.DeleteStudentData.as_view())
]


## ##################################################################################
## TESTING
## ##################################################################################

# http://127.0.0.1:8000/app_db_serializer/get_student_details
"""
Use the method = GET HTTP  in postman
"""

# http://127.0.0.1:8000/app_db_serializer/insert_student_details
"""
# With postman apply the following
1. Method = POST 
2. Content = Body>Raw
3. type = JSON

content
--------
{
    "student_id": 4
    ,"student_name":"D"
    ,"join_date":"2022-01-02"
}

"""

# http://127.0.0.1:8000/app_db_serializer/update_student_details/4
"""
# With postman apply the following
1. Method = PUT 
2. Content = Body>Raw
3. type = JSON

content
--------
{
    "student_id": 4
    ,"student_name":"HHHHHHH"
    ,"join_date":"2021-08-20"
}

"""


# http://127.0.0.1:8000/app_db_serializer/delete_student_details/4
"""
# With postman apply the following
1. Method = DELETE 
No Content To Pass
"""


# [{"student_id": 22,"student_name": "ZZZ","join_date": "2022-08-20"},{"student_id": 33,"student_name": "PPP","join_date": "2022-08-20"}]


