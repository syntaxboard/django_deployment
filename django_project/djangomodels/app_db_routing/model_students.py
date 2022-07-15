from django.db import models


class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=30, blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'
