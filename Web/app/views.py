from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Student, Combination, Faculty
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
import logging


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def register(request):
    logger.info(f"Request method: {request.method}")
    if request.method == 'POST':
        data = request.data
        logger.info(f"Received data: {data}")
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    elif request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        logger.info(f"Users: {serializer.data}")
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def studentlist(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Student(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def studentcount(request):
    count = Student.objects.count()
    return Response({'count': count})


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def studentdetails(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def combinationlist(request):
    if request.method == 'GET':
        combination = Combination.objects.all()
        serializer = CombinationSerializer(combination, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CombinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def combinationdetail(request, pk):
    try:
        combination = Combination.objects.get(pk=pk)
    except combination.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CombinationSerializer(combination)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CombinationSerializer(combination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        combination.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def facultylist(request):
    if request.method == 'GET':
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def facultydetail(request, pk):
    try:
        faculty = Faculty.objects.get(pk=pk)
    except Faculty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
