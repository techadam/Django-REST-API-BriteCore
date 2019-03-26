from django.db import models

# Risk types Model for holding data related to Risk types
class RiskType(models.Model):
    risk_name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['risk_name'] #Ordering by risk_name in descending order
            
    def __str__(self):
        #String representation of the Model
        return self.risk_name


#RiskField Model for holding field related to a risk type
class RiskField(models.Model):
    risk_type_id = models.ForeignKey('RiskType', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=200)
    readable_name = models.CharField(max_length=200)
    field_type_id = models.ForeignKey('FieldType', on_delete=models.CASCADE)
    field_options = models.CharField(max_length=255, blank=True, default='')
    
    class Meta:
        ordering = ['readable_name'] #Ordering by field_name in descending order
    
    def __str__(self):
        #String representation of the Model
        return self.field_name
    

#Field TYpe Model to represent the types of field a user can create for a risk field
class FieldType(models.Model):
    type_name = models.CharField(max_length=200)
    type_options_req = models.BooleanField(default=False)
    type_options_multiple = models.BooleanField(default=False)
    
    def __str__(self):
        return self.type_name


