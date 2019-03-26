from django.test import TestCase
from .models import RiskType, FieldType, RiskField
from django.urls import reverse

# Create your tests here.
class RiskTypeModelTest(TestCase):
    
    def setUp(self):
        self.risktype = RiskType.objects.create(risk_name='Cyber Liability')
        
        self.fieldtype = FieldType.objects.create(
            type_name='text', 
            #type_options_required=0, 
            #type_options_multiple=0,
        )
        
        self.riskfield = RiskField.objects.create(
            risk_type_id = self.risktype,
            field_name = 'name_of_field',
            readable_name = 'Name of field',
            field_type_id = self.fieldtype,
        )
        
        
    def test_risk_type_content(self):
        self.assertEquals(f'{self.risktype.risk_name}', 'Cyber Liability')

    def test_field_type_content(self):
        fieldtype = FieldType.objects.get(id=1)
        expected_obj_name = f'{self.fieldtype.type_name}'
        self.assertEqual(expected_obj_name, 'text'),
        
    def test_risk_field_content(self):
        self.assertEqual(f'{self.riskfield.field_name}', 'name_of_field')
        self.assertEqual(f'{self.riskfield.readable_name}', 'Name of field')
        self.assertEqual(f'{self.riskfield.field_type_id}', f'{self.fieldtype}')
        
    
        