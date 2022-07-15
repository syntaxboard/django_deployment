# Django Model
* A model in Django is an python object that represents a database table, that contains fields or 
  properties of the dataset that is stored.
* Almost usually each model maps to a single database table.
* Each Model represents a source database table, with fields or 
  properties (or table columns) of the table record
* Below are the steps to demonstrate the Django Models, We divide the coding steps
  into Command Line, Project Files, App Files

## Django Model - DB Data Type Mapping

* The column datatypes that are supported by the
* CharField(max_length) Used for String Data Types
* DecimalField(max_digits, decimal_places) Used for Decimal Data Types (100.20)
* IntegerField Used for Integer Data Types (1,2..)
* TextField Multi-line Strings
* DateField used for date data
* DateTimeField used for Date Time Data
* BooleanField True / False Data
* FileField Binary File Data

## Django Models Demonstration

### Step 1. Create a Django Project

```bash
django-admin startproject djangomodels
```

### Step 2. Create Apps for the Project

* Navigate to the project folder where the `manage.py` exists.
* Create the APP, Here we name the app name as app_models
```bash
# Create APP to demonstrate Database Routing
python manage.py startapp app_db_routing

# Create APP for that uses Serializer
python manage.py startapp app_db_serializer

# Create APP to execute custom SQL directly
python manage.py startapp app_db_custom_sql
# user https://docs.djangoproject.com/en/3.1/topics/db/sql/

# Create APP to demonstrate Database Query Sets
python manage.py startapp app_db_querysets

```

### Step 3. Project Files Changes

#### Step 3.1 Project File settings.py

* File Location / Name `djangomodels/settings.py`

* Add the APP and DB details to the `settings.py` file
```python
# settings.py

# Add APP name to INSTALLED_APPS
################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # User Defined APPs
    'app_db_routing',
    'app_db_custom_sql',
    #'app_db_serializer',
    #'app_db_querysets',
 ]
 
# Add to DB Settings
# ################################################
DATABASE_ROUTERS = ['djangomodels.dbrouters.AppRouter']

DATABASES = {
    'default': {},
    'app_models_one_db' : {
       'ENGINE': 'django.db.backends.mysql'
      ,'NAME':'app_onedb'
      ,'USER':'root'
      ,'PASSWORD':'tinitiate'
      ,'HOST':'localhost'
      ,'PORT':'3306'
    },
    'app_models_multi_db' : {
       'ENGINE': 'django.db.backends.mysql'
      ,'NAME':'app_multidb'
      ,'USER':'root'
      ,'PASSWORD':'tinitiate'
      ,'HOST':'localhost'
      ,'PORT':'3306'
    }
}
```

* Add the APP details to the `project/urls.py ` file, here ``
```python
# djangomodels/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_models/', include('app_models.urls')),
]

```

* Create the `dbrouter.py` file in the location `project/app/router-file-name.py`
* Here we create the file in folder as `djangomodels/models_one_db/dbrouter.py`
```python
# <project>/dbrouter.py
from django.conf import settings

class AppRouter:

    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to mysql_db.
        """
        if model._meta.app_label == 'app_models':
            return 'mysql_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to mysql_db.
        """
        if model._meta.app_label == 'app_models':
            return 'mysql_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'app_models' or \
           obj2._meta.app_label == 'app_models':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'mysql_db'
        database.
        """
        if app_label == 'app_models':
            return db == 'mysql_db'
        return None
```

## Step 3. Create Database Tables
* Here we use MySQL database, we use a table `testing`
```sql
-- Create Database
create database testing;
-- Use the database
use testing;

-- Create Tables
create table students
    ( student_id   int
     ,student_name varchar(30)
     ,join_date    date
     ,constraint students_pk primary key(student_id));

create table courses
    ( course_id       int
     ,course_name     varchar(30)
     ,course_details  text
     ,constraint courses_pk primary key(course_id));

create table students_courses
    ( stu_crs_id   int
     ,student_id   int
     ,course_id    int
     ,primary key(stu_crs_id)
     ,constraint fk_courses foreign key (course_id) references courses(course_id)
     ,constraint fk_sudents foreign key (student_id) references students(student_id)
     );
```

## Step 4. Command Line 
* Generate Django Models from existing Database Tables
* Here we have multiple databases, hence we specify the DB name using the `--database`
* Navigate to the `projects/manage.py` and run the below commands
```bash
python manage.py inspectdb --database DB1 students > app_db_routing/model_students.py
python manage.py inspectdb --database DB1 courses > app_db_routing/model_courses.py
python manage.py inspectdb --database DB1 students_courses > app_db_routing/model_students_courses.py
```
* The above commands will create the `models.py` file to the `project` folder

```bash
python manage.py inspectdb --database DB1 students > app_db_serializer/model_students.py
python manage.py inspectdb --database DB1 courses > app_db_serializer/model_courses.py
python manage.py inspectdb --database DB1 students_courses > app_db_serializer/model_students_courses.py
```




## Step 5. App Files
* Copy the `projects/models.py` file to the APP folder

* Create the `views.py` and the `urls.py` files
```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse

# Import the Model from current APP
from .models import Students,Courses,StudentsCourses
from datetime import datetime 


def InsertStudentData(request):

    # Create Few Data Sets
    StuentRecord1 = Students( student_id   = 1
                             ,student_name = "AAA"
                             ,join_date    = datetime.now())

    StuentRecord1.save()

    StuentRecord2 = Students( student_id   = 2
                             ,student_name = "BBB"
                             ,join_date    = datetime.now())

    StuentRecord2.save()

    return HttpResponse('2 Rows Inserted')


# Get Students record by student_id
def GetStudentByID(request, in_student_id):

    data = ""
    
    # Get Row Data by primary key
    rowObj = Students.objects.get(pk=in_student_id)

    data = str(rowObj.student_id) + " " + str(rowObj.student_name) + " "
    data = data + " " + str(rowObj.join_date)

    return HttpResponse(data)


# Method to return all rows from the students table
def GetAllRecords(request):
    data = ""
    for e in Students.objects.all():
        data = data + str(e.student_id) + " " + str(e.student_name) + " "
        data = data + " " + str(e.join_date) + "<br>"

    if data == "":
        data = "No Records Found !"

    return HttpResponse(data)


# Function to Update in_student_name By in_student_id
def UpdateStudentByID(request, in_student_id, in_student_name):

    rowObj = Students.objects.get(pk=in_student_id)
    rowObj.student_name = in_student_name
    rowObj.save()

    return HttpResponse("student_id - " + str(in_student_id) + " updated salary " + str(in_student_name))


# Function to Delete Record By in_student_id
def DeleteStudentByID(request, in_student_id):
    #Delete an entry
    rowObj = Students.objects.get(pk=in_student_id)
    rowObj.delete()
        
    return HttpResponse("student_id - " + str(in_student_id) + " deleted.")


# Function to Delete All Records
def DeleteAllRecords(request):
    data = ""
    for e in Students.objects.all():
        data = data + str(e.student_id) + "<br>"
        e.delete();

    return HttpResponse("student_id Records deleted for " + "<br>" + data)

```

* Create the `urls.py`
```python
# urls.py
# from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    # For URL: localhost:8000/app_models/InsertStudentData
    path('InsertStudentData', views.InsertStudentData),
    path('GetStudentByID/<int:in_student_id>', views.GetStudentByID),
    path('GetAllRecords', views.GetAllRecords),
    path('UpdateStudentByID/<int:in_student_id>/<str:in_student_name>', views.UpdateStudentByID),
    path('DeleteStudentByID/<int:in_student_id>', views.DeleteStudentByID),
    path('DeleteAllRecords', views.DeleteAllRecords),
]
```


## Step 6. Runserver and test Templates
* At commandline start the project, using the command:
```
python manage.py runserver
```
* Open a browser to test the URLs defined in the `app/urls.py`
  * localhost:8000/app_models/InsertStudentData
  * localhost:8000/app_models/GetStudentByID/1
  * localhost:8000/app_models/GetAllRecords
  * localhost:8000/app_models/UpdateStudentByID/1/CCC
  * localhost:8000/app_models/DeleteStudentByID/1
  * localhost:8000/app_models/DeleteAllRecords
