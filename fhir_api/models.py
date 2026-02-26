from django.db import models
import uuid

class Patient(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('unknown', 'Unknown'),
    ]

    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    family_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['identifier']),
            models.Index(fields=['family_name', 'given_name']),
        ]

    def __str__(self):
        return f"{self.family_name} {self.given_name}"


class Observation(models.Model):

    OBS_TYPES = [
        ('blood-pressure', 'Tension artérielle'),
        ('heart-rate', 'Fréquence cardiaque'),
        ('temperature', 'Température'),
        ('weight', 'Poids'),
        ('height', 'Taille'),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='observations'
    )

    observation_type = models.CharField(max_length=50, choices=OBS_TYPES)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    effective_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['patient', 'effective_date']),
        ]

    def __str__(self):
        return f"{self.patient} - {self.observation_type}"
