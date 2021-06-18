from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Employees(MPTTModel):

    id = models.AutoField(primary_key=True)
    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(max_length=150, db_index=True)
    position = models.CharField(max_length=150, db_index=True)
    emp_date = models.DateField(db_index=True)
    salary = models.IntegerField(db_index=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

