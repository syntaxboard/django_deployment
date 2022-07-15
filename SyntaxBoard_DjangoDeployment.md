# Syntax Board Django Deployment

> Srikanth A



* Welcome to Django Deployment Guide, here are the steps to Deploy a Django Application with the following components:

  * Database
  * Python Code for Django
  * Gunicorn Web Server

* Please follow the steps specified below

  * `STEP 1` Create the DB , Navigate  to the **MySQL** folder in command line and run 
    * `docker-compose up -d`

     * `STEP 2` Connect to MYSQL from the above **Docker** and run the DB script

     * ` STEP 3` Build the Python-Django docker image, navigate to **django_project**  folder and run

       *  `docker-compose up -d`

     * `STEP 4` Check the Server Status by Running the Following in your browser

       * `http://localhost:8000/`

       *      # http://localhost:8000/app_db_routing/CreateStudentsData/
              # http://localhost:8000/app_db_routing/UpdateStudentNameByID/1/EEE
              # http://localhost:8000/app_db_routing/DeleteRecordByID/1
              # http://localhost:8000/app_db_routing/DeleteAllRecords/
              # http://localhost:8000/app_db_routing/GetAllRecords/
              # http://localhost:8000/app_db_routing/GetRecordByID/1
              # http://localhost:8000/app_db_routing/my_custom_sql/1

       