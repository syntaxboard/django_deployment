-- ----------------------------------------------------------------------------------
-- DB Script for Django Training
-- by Venkata Bhattaram
-- (c) 2020
-- Use these tables with MySQL database
-- ----------------------------------------------------------------------------------


-- ----------------------------------------------------------------------------------
-- Database Name: DB2
-- Tables:  1. students
--          2. courses
--          3. students_courses
--         
-- ----------------------------------------------------------------------------------

-- Create Database
create database db1;

-- Use the database
use db1;
-- select * from students;
-- delete from students where student_id in (11,22,33);


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
     
-- ----------------------------------------------------------------------------------
-- Create the Other DB,
-- Database Name: DB2
-- Tables:  1. app_users
--         
-- ----------------------------------------------------------------------------------
-- Create Database
create database db2;

use db2;

create table app_users
    ( username       varchar(30)
     ,passwd         varchar(30)
     ,registeredDate date
     ,email          varchar(200)
     ,constraint app_users_pk primary key(username)
    );
    
    
    
    