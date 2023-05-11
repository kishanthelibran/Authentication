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
    name = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=40)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s %s" % (self.name, self.city, self.dept, self.role, self.salary)
