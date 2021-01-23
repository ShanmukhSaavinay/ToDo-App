from django.db import models

# Create your models here.
class Work(models.Model):
    work_to_do = models.CharField(max_length=200)
    work_done = models.BooleanField(default = False )
    created  = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.work_to_do
