from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.http import HttpResponse
from .models import information
from .serializers import Infoserializer
# from django.shortcut import redirect
from django.conf import settings
from django.core.mail import send_mail
# from .forms import Infopost


# def postal(request):
#     if request.method=='POST':
#         info=Infopost()
#         info.fname=request.POST['FirstName']
#         info.lname=request.POST['LastName']
#         info.company=request.POST['Company']
#         info.email=request.POST['Email_id']
#         info.save()
#         send_mail_registration(email)
#         return redirect('/')
#     else:
#         return HttpResponse("wrong")

class PostAPIViews(APIView):
    def post(self, request):
        serializer = Infoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail_registration(request=request.data)
            print(request)
            return Response(status=status.HTTP_200_OK)
            # return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            # return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            info = information.objects.get(id=id)
            serializer = Infoserializer(info)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        info = information.objects.all()
        serializer = Infoserializer(info, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

def send_mail_registration(request):
    subject = "One More Person Submit Form!!!"
    message=f" First Name: {request['firstName']} , Last Name: {request['lastName']}, Phone No.: {request['phone']},Email-Id.{request['emailId']},Company Name.{request['companyName']}"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=["vk126789@gmail.com"]
    send_mail(subject,message,email_from,recipient_list)