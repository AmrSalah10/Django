from django.shortcuts import render, redirect
from netflix.models import Movie
from .serialize import MovieSerial, UserSerialize
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated





@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerial(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = MovieSerial(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'Data':serializer.data,
            'Sucess':True,
            'Message': ('%s movie is created successfully' %serializer.data['name'])
            },
            status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def api_signup(request):
    serialzer = UserSerialize(data=request.data)
    if serialzer.is_valid():
        serialzer.save()
        return Response(data={
            'Success':True,
            'Message': 'User is created successfully'
        },status=status.HTTP_201_CREATED)

    return Response(data={
        'Success':False,
        'Error': serialzer.errors
        },status=status.HTTP_400_BAD_REQUEST)



class MovieCreate(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class =  MovieSerial


class MovieUpdate(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class =  MovieSerial


class MovieDelete(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serialzer_class = MovieSerial

class MovieViewSet(viewsets.ModelViewSet):
    model = Movie
    # It must be queryset not movies
    queryset = Movie.objects.all()
    serializer_class =  MovieSerial