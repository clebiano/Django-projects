from rest_framework.serializers import ModelSerializer
from patients.models import Patient


class PatientSerializer(ModelSerializer):

    class Meta:
        model = Patient
        fields = ['id', 'name', 'birth_date', 'collection_date', 'delivery_date', 'doctor_name']
