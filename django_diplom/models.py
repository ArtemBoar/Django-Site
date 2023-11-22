from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=128)
    balance = models.IntegerField(null=True, blank=True)
    next_meet = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)


class Worker(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    age = models.IntegerField(null=True, blank=True)
    specialist = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)


