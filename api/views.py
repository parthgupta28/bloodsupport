from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import bloodbank
from .serializers import bloodbankSerializer
from django.core import serializers
import math
from django.db.backends.signals import connection_created
from django.dispatch import receiver
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
import json
@receiver(connection_created)
def extend_sqlite(connection=None, **kwargs):
    connection.connection.create_function("acos", 1, math.acos)
    connection.connection.create_function("cos", 1, math.cos)
    connection.connection.create_function("sin", 1, math.sin)
    connection.connection.create_function("radians", 1, math.radians)



class BBList(APIView):
    def get(self, request):


        lat=request.GET['lat']
        lng=request.GET['long']
        radius=request.GET['radius']



        query = """SELECT * FROM blood WHERE (6367*acos(cos(radians(%f))
                       *cos(radians(latitude))*cos(radians(longitude)-radians(%f))
                       +sin(radians(%f))*sin(radians(latitude)))) < %f ORDER BY (6367*acos(cos(radians(%2f))
                       *cos(radians(latitude))*cos(radians(longitude)-radians(%f))
                       +sin(radians(%f))*sin(radians(latitude))))""" % (
            float(lat),
            float(lng),
            float(lat),
            float(radius),
            float(lat),
            float(lng),
            float(lat),

        )

        blood = bloodbank.objects.raw(query)
        serial = bloodbankSerializer(blood, many=True)

        return Response(serial.data)

    def post(self):
        pass



"""
class BBUpdate(APIView):
    #permission_classes = (IsAuthenticated,)
    def post(self,request):
        model1 = bloodbank
        rrr=json.loads(request.body.decode("utf-8"))
        data1 = bloodbankSerializer(data=rrr)
        if data1.is_valid():
            return Response(data1.validated_data)
        return Response(data1.error_messages)

"""