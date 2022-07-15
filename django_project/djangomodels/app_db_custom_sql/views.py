from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections, transaction
from django.db import connection, transaction


# Using Connection only where there is a DEFAULT Connection
# ###################################################################################
# def my_custom_sql1(request,in_student_id):
# 
#     cursor = connection.cursor()
#     cursor.execute("SELECT student_name FROM students WHERE student_id = {}".format(in_student_id))
#     row = cursor.fetchone()
# 
#     return HttpResponse(row)

# Using Connections
# ###################################################################################
def GetStudentByID(request,in_student_id):

    #cursor = connection['DB1'].cursor()
    with connections['DB1'].cursor() as cursor:

        cursor.execute("SELECT student_name,join_date FROM students WHERE student_id = {}".format(in_student_id))
        row = cursor.fetchone()

    return HttpResponse(row)



# Insert THREE rows into STUDENTS table in MySQL database
def CreateStudentsData(request):

    with connections['DB1'].cursor() as cursor:
    #
        cursor.execute("insert into students values(11,'P',curdate());")
        cursor.execute("insert into students values(22,'Q',curdate());")
        cursor.execute("insert into students values(33,'R',curdate());")
        
    connections['DB1'].commit()
        
    return HttpResponse('3 Rows with IDs [11,22,33] Inserted')


# Function to Update Salary By EmpID
def UpdateStudentNameByID(request, in_student_id, in_student_name):

    with connections['DB1'].cursor() as cursor:
    #
        cursor.execute("update students set student_name = '{0}' where student_id = {1};".format(in_student_name, in_student_id))

    return HttpResponse("StudentID - " + str(in_student_id) + " updated Student Name " + str(in_student_name))


# Function to Delete Record By EmpID
def DeleteRecordByID(request, in_student_id):

    with connections['DB1'].cursor() as cursor:
    #
        cursor.execute("delete from students where student_id = {0};".format(in_student_id))

    return HttpResponse("student_id - " + str(in_student_id) + " deleted")





