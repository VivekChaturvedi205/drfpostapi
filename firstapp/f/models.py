from django.db import models

# class information(models.Model):
#     fname=models.CharField(max_length=256)
#     lname=models.CharField(max_length=256)
#     phone=models.CharField(max_length=12)
#     email=models.EmailField(unique=True)
#     company=models.CharField(max_length=256)

#     def __str__(self):
#         return self.fname

    
class information(models.Model):
    firstName=models.CharField(max_length=256)
    lastName=models.CharField(max_length=256)
    phone=models.CharField(max_length=12)
    emailId=models.EmailField()
    companyName=models.CharField(max_length=256)

    def __str__(self):
        return self.firstName

