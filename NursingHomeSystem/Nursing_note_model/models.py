from django.db import models

# Create your models here.
class Nursing_note(models.Model):
    # 主键
    client_id = models.CharField(primary_key=True, max_length=12)

    operator_id = models.CharField(max_length=12)
    item_id= models.CharField(max_length=4)
    time =  models.DateField()
    remark =  models.TextField()


