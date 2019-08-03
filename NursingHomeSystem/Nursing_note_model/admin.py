from django.contrib import admin

# Register your models here.
class ServiceTable(models.Model):
    # 主键
    client_id = models.CharField(primary_key=True, max_length=12)

    operator_id = models.CharField(max_length=12)
    time = models.CharField(max_length=20)
    item_id= models.CharField(max_length=4)
    remarks = models.CharField(max_length=200)
