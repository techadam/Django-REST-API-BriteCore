from rest_framework import serializers
from .models import RiskType, RiskField, FieldType

'''
    RiskTypeSerializer to convert RiskType model Data to JSON
'''
class RiskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'risk_name',
        )
        model = RiskType

'''
    RiskFieldSerializer to convert RiskField model Data to JSON
'''
class RiskFieldSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = (
            'id',
            'risk_type_id',
            'field_name',
            'readable_name',
            'field_type_id',
            'field_options',
        )
        model = RiskField
        

'''
    FieldTypeSerializer to convert FieldType model Data to JSON
'''
class FieldTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'type_name',
            'type_options_req',
            'type_options_multiple',
        )
        model = FieldType

