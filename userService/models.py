from django.db import models


# Create your models here.
class SysUser(models.Model):
    user_id = models.CharField(max_length=200)
    user_name = models.CharField(max_length=512)
    user_image = models.FileField(null=True, blank=True)
    dob = models.DateTimeField()
    skin_type = models.IntegerField()
    gender = models.CharField(max_length=10, default="M")
    uk_size = models.CharField(max_length=10, default="XL")

    def __str__(self):
        return self.user_id + "-" + self.user_name


