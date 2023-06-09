from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer,UserSerializer
from rest_framework import status
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login

# Create your views here.

@csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
def departmentApi(request,id=0,format=None):
    if request.method == 'GET':
        departments = Departments.objects.all()  
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to save",safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(pk = id)
        departments_serializer = DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("updated successfully",safe=False)
        return JsonResponse("failed to update")
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)

class SignupView(APIView):
    permission_classes = [AllowAny]
    @csrf_exempt
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse("user created",safe=False)
        return JsonResponse("error")

class LoginView(APIView):
    permission_classes = [AllowAny]
    @csrf_exempt
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'data' : UserSerializer(user).data }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
