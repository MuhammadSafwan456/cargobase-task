from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult

from .serializers import (
    GetFlightInfoQueryParams,
    FlightInfoSerializer,
    ScrapDataQueryParams,
)
from .models import FlightInfo
from .tasks import scrap_flight_info

# Create your views here.


class ScrapView(APIView):
    def get(self, request):
        query_params = request.GET.dict()
        query_params = ScrapDataQueryParams(data=query_params)
        if not query_params.is_valid():
            return Response(query_params.errors, status=status.HTTP_400_BAD_REQUEST)

        query_params = query_params.data
        airline = query_params.get("airline")
        flight_number = query_params.get("flight_number")
        date = query_params.get("date")
        
        task = scrap_flight_info.delay(airline, flight_number, date)
        return Response(task.task_id, status=status.HTTP_200_OK)


class InfoView(APIView):
    def get(self, request, *args, **kwargs):
        query_params = request.GET.dict()
        query_params = GetFlightInfoQueryParams(data=query_params)
        if not query_params.is_valid():
            return Response(query_params.errors, status=status.HTTP_400_BAD_REQUEST)

        query_params = query_params.data
        airline = query_params.get("airline", None)
        flight_number = query_params.get("flight_number", None)
        date = query_params.get("date", None)

        query_set = FlightInfo.objects.all()
        if airline:
            query_set = query_set.filter(airline=airline)
        if flight_number:
            query_set = query_set.filter(flight_number=flight_number)
        if date:
            query_set = query_set.filter(date=date)
        query_set = FlightInfoSerializer(query_set, many=True)
        return Response(query_set.data, status=status.HTTP_200_OK)


class StatusView(APIView):
    def get(self, request, *args, **kwargs):
        task_id = str(kwargs.get("task_id"))
        _status = AsyncResult(task_id).state
        return Response(_status, status=status.HTTP_200_OK)
