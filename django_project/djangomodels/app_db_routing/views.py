from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections, transaction

# Import the Model from current APP
from .model_students import Students
from datetime import datetime

# Insert THREE rows into STUDENTS table in MySQL database
def django_status(request):

    return HttpResponse('Docker Django is Running Congrats !!')

# Insert THREE rows into STUDENTS table in MySQL database
def CreateStudentsData(request):

    # Create Student Object
    # save using the save() method
    StuRec1 = Students( student_id   = 1
                       ,student_name = "AAA"
                       ,join_date    = datetime.now())

    StuRec1.save()

    StuRec2 = Students( student_id   = 2
                       ,student_name = "BBB"
                       ,join_date    = datetime.now())

    StuRec2.save()

    StuRec3 = Students( student_id   = 3
                       ,student_name = "CCC"
                       ,join_date    = datetime.now())

    StuRec3.save()

    return HttpResponse('3 Rows Inserted')


# Function to Update Salary By EmpID
def UpdateStudentNameByID(request, in_student_id, in_student_name):

    rowObj = Students.objects.get(pk=in_student_id)
    rowObj.student_name = in_student_name
    rowObj.save()

    return HttpResponse("Student ID "+str(in_student_id)+ " name updated to "+in_student_name)


# Function to Delete Record By EmpID
def DeleteRecordByID(request, in_student_id):
    #Delete an entry
    rowObj = Students.objects.get(pk=in_student_id)
    rowObj.delete()

    return HttpResponse("student_id - " + str(in_student_id) + " deleted")


# Function to Delete All Records
def DeleteAllRecords(request):
    data = ""
    for s in Students.objects.all():
        data = data + str(s.student_id) + "<br>"
        s.delete();

    return HttpResponse("Student Records deleted for " + "<br>" + data)


# Get Student Data record by student_id
def GetRecordByID(request, in_student_id):

    # Get Row Data by primary key
    rowObj = Students.objects.get(pk=in_student_id)

    data = str(rowObj.student_id) + " " + str(rowObj.student_name) + " "
    data = data + " " + str(rowObj.join_date)

    return HttpResponse(data)


# Method to return all rows from the EMP table
def GetAllRecords(request):
    data = ""
    for s in Students.objects.all():
        data = data + str(s.student_id) + "                                     " + str(s.student_name) + " "
        data = data + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; " + str(s.join_date) + " " + "<br>"

    if data == "":
        data = "No Records Found !"

    return HttpResponse(data)


def my_custom_sql(request,in_student_id):

    #cursor = connection['DB1'].cursor()
    with connections['DB1'].cursor() as cursor:

        cursor.execute("SELECT student_name FROM students WHERE student_id = {}".format(in_student_id))
        row = cursor.fetchone()

    return HttpResponse(row)

