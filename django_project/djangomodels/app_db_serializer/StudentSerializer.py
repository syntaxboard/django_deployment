# import serializer from rest_framework 
from rest_framework import serializers 
# import model
from .models import Students 

class StudentsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Students
        fields = ['student_id','student_name','join_date'] 
        # fields = "__all__"
