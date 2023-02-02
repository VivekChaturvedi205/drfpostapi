from rest_framework import serializers
from .models import information

class Infoserializer(serializers.ModelSerializer):
    class Meta:
        model= information
        fields=('firstName','lastName','phone','companyName','emailId')


# {
#     "fname":"vivek",
#     "lname":"chaubey",
#     "phone":"9811694732",
#     "email":"abc3@gmail.com",
#     "company":"xyz"
# }

# class information(models.Model):
#     firstName=models.CharField(max_length=256)
#     lastName=models.CharField(max_length=256)
#     phone=models.CharField(max_length=12)
#     emailId=models.EmailField(unique=True)
#     companyName=models.CharField(max_length=256)

#     def __str__(self):
#         return self.firstName
