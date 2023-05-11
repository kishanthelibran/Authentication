from django.db import models

# Create your models here.


class Department(models.Model):
    dept = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.dept


class Role(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name


class UserModel(models.Model):
    name = models.CharField(max_length=30, null=False, primary_key=True)
    city = models.CharField(max_length=40)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s %s" % (self.name, self.city, self.dept_id, self.role_id, self.salary)
