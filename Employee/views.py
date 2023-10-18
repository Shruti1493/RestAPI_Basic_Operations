from django.shortcuts import render
from .models import Employee
# Create your views here.
from rest_framework.views import APIView
from .models import Employee
from rest_framework import status
from .serializers import EmployeeSerializer
from rest_framework.response import Response

class EmployeeAPI(APIView):
    def get(self,request,pk=None,format = None):
        id = pk
        if id is not None:
            Emp = Employee.objects.get(id = id)
            serializer = EmployeeSerializer(Emp)
            return Response(serializer.data)
        
        Emp = Employee.objects.all()
        serializer = EmployeeSerializer(Emp,many = True)
        return Response(serializer.data)

    
    def post(self,request, format = None):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format = None):
        id = pk
        Emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(Emp,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated '},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None,format = None):
        id = pk
        Emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(Emp,data= request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated '},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format = None):
        id = pk
        Emp = Employee.objects.get(pk = id)
        Emp.delete()
        return Response({'msg':'Data Deleted'})