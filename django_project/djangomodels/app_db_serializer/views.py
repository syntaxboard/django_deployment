from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .StudentSerializer import StudentsSerializer
from .models import Students
from rest_framework.decorators import api_view
import json

# Create your views here.
class GetStudent(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class GetAllStudents(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class InsertStudentData(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class UpdateStudentData(UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class DeleteStudentData(DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


"""    
@api_view(['GET'])
def updateMany(request):

    
    in_data = ''
    
    in_data = request.GET['N1']

    in_data = json.loads(in_data)
    print("in_data")
    print(in_data)
    
    in_data = [{"student_id": 22,"student_name": "ZZZ","join_date": "2022-08-20"},{"student_id": 33,"student_name": "PPP","join_date": "2022-08-20"}]
    for row in in_data:
        x = UpdateStudentData()

    response = "Updated Rows"
    return HttpResponse(response)
"""