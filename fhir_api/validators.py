from fhir.resources.patient import Patient as FHIRPatient
from fhir.resources.observation import Observation as FHIRObservation
from rest_framework.exceptions import ValidationError

def validate_fhir_resource(data, resource_type='Patient'):
    try:
        if resource_type == 'Patient':
            FHIRPatient(**data)
        elif resource_type == 'Observation':
            FHIRObservation(**data)
        return True
    except Exception as e:
        raise ValidationError({"fhir_validation": str(e)})