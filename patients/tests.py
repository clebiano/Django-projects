from django.test import TestCase
from .models import Patient


class PatientTestCase(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(id=1, name='Clebiano da Costa Sá', birth_date='1991-02-17',
                                              collection_date='2019-09-28', delivery_date='2019-09-28',
                                              doctor_name='Maria Oliveira')

    def test_patient_create(self):
        """" Checks if patients are being saved to the database """
        assert Patient.objects.all().count() >= 1

