
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Patient, Observation
from .serializers import PatientFHIRSerializer, ObservationFHIRSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-created_at')
    serializer_class = PatientFHIRSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['gender', 'family_name']


class ObservationViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.select_related('patient').all()
    serializer_class = ObservationFHIRSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {
        'patient': ['exact'],
        'observation_type': ['exact'],
        'effective_date': ['gte', 'lte'],
        'value': ['gte', 'lte'],
    }

# Create your views here.
