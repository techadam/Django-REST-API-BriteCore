from django.shortcuts import render
from rest_framework import generics
from .serializers import RiskTypeSerializer, RiskFieldSerializer, FieldTypeSerializer
from .models import RiskType, RiskField, FieldType

'''
    - RiskListView to returns JSON Object for all risk_types
    - It does both the functions of Fetching the Risk types &
    - Creating a new Risk Type
'''
class RiskListView(generics.ListCreateAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer


'''
    - RiskDetailView to return JSON Object for a Risk type
    - It does both the functions of Fetching the Risk type with id &
    - Updating the Risk type using the id &
    - Deleting the Risk type using the id
'''
class RiskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer


'''
    - RiskFieldListView to returns JSON Object for all risk_fields
    - It does both the functions of Fetching the Risk fields &
    - Creating a new Risk Field
'''
class RiskFieldListView(generics.ListCreateAPIView):
    queryset = RiskField.objects.all()
    serializer_class = RiskFieldSerializer
    

'''
    - RiskFieldDetailView to return JSON Object for a Risk type
    - It does both the functions of Fetching the Risk field with id &
    - Updating the Risk field using the id &
    - Deleting the Risk field using the id
'''    
class RiskFieldDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskField.objects.all()
    serializer_class = RiskFieldSerializer


'''
    - FieldTypeListView to returns JSON Object for all field types
'''
class FieldTypeListView(generics.ListAPIView):
    queryset = FieldType.objects.all()
    serializer_class = FieldTypeSerializer
    
