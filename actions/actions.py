from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import re
import csv
import os

class ValidateMedicForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_medic_form"

    def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""
        if not slot_value.strip():
            dispatcher.utter_message(text="That must've been a typo.")
            return {"first_name": None}
        return {"first_name": slot_value}

    def validate_last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""
        if not slot_value.strip():
            dispatcher.utter_message(text="That must've been a typo.")
            return {"last_name": None}
        return {"last_name": slot_value}
   
    def validate_gender(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `gender` value."""

        valid_gender = ["masculino", "femenino", "ninguno"]
        
        # Si el nombre del género no está en las opciones válidas
        if slot_value.lower() not in valid_gender:
            dispatcher.utter_message(text="Por favor, selecciona un género válido.")
            return {"gender": None}
        
        # Si el género es válido
        return {"gender": slot_value}

    def validate_blood_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `blood_type` value."""

        valid_blood_type = ["0-", "0+", "A-", "A+", "B-", "B+", "AB-", "AB+", "a-","a+","b-", "b+", "ab-","ab+", "ninguno"]
        
        # Si el nombre de la ocupación no está en las opciones válidas
        if slot_value.lower() not in valid_blood_type:
            dispatcher.utter_message(text="Por favor, selecciona un grupo sanguíneo válido.")
            return {"blood_type": None}
        
        # Si el género es válido
        return {"blood_type": slot_value}
    
    def validate_occupation(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `occupation` value."""

        valid_occupations = ["empleado", "empleada", "desempleado", "desempleada", "estudiante", "jubilado", "jubilada"]
        
        # Si el nombre de la ocupación no está en las opciones válidas
        if slot_value.lower() not in valid_occupations:
            dispatcher.utter_message(text="Por favor, selecciona una ocupación válida.")
            return {"occupation": None}
        
        # Si la ocupación proporcionada es válida
        return {"occupation": slot_value}
    
    def validate_civil_status(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `civil_status` value."""

        valid_civils = ["casado", "casada", "divorciado", "divorciada", "separado", "separada", "viudo", "viuda", "soltero", "soltera"]
        
        # Si el nombre de la ocupación no está en las opciones válidas
        if slot_value.lower() not in valid_civils:
            dispatcher.utter_message(text="Por favor, selecciona un estado civil válido.")
            return {"civil_status": None}
        
        # Si la ocupación proporcionada es válida
        return {"civil_status": slot_value}
    
    def validate_personal_history(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `personal_history` value."""
        # No se aplican restricciones al historial personal, así que simplemente los devolvemos
        return {"personal_history": slot_value}
    
    def validate_family_history(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `family_history` value."""
        # No se aplican restricciones al historial familiar, así que simplemente los devolvemos
        return {"family_history": slot_value}
    
    def validate_alcohol_use(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `alcohol_use` value."""

        valid_alcohol_use = ["nunca", "raramente", "frecuencia muy baja", "frecuencia baja", "frecuencia media", "frecuencia alta", "frecuencia muy alta"]
        
        # Si el nombre de la ocupación no está en las opciones válidas
        if slot_value.lower() not in valid_alcohol_use:
            dispatcher.utter_message(text="Por favor, selecciona una frecuencia de consumo válida.")
            return {"alcohol_use": None}
        
        # Si la ocupación proporcionada es válida
        return {"alcohol_use": slot_value}

    def validate_tobaco_use(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `tobaco_use` value."""

        valid_tobaco_use = ["nunca", "raramente", "frecuencia muy baja", "frecuencia baja", "frecuencia media", "frecuencia alta", "frecuencia muy alta"]
        
        # Si el nombre de la ocupación no está en las opciones válidas
        if slot_value.lower() not in valid_tobaco_use:
            dispatcher.utter_message(text="Por favor, selecciona una frecuencia de consumo válida.")
            return {"tobaco_use": None}
        
        # Si la ocupación proporcionada es válida
        return {"tobaco_use": slot_value}
    
    def validate_symptoms(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `symptoms` value."""
        # No se aplican restricciones a los síntomas, así que simplemente los devolvemos
        return {"symptoms": slot_value}
    
    def validate_medication(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `medication` value."""
        # No se aplican restricciones a los síntomas, así que simplemente los devolvemos
        return {"medication": slot_value}
    
    def validate_birth_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `birth_date` value."""
        pattern = r'(0[1-9]|1[0-9]|2[0-9]|3[01])\/(0[1-9]|1[0-2])\/(19\d{2}|20(?:0\d|1[0-9]|20|21|22|23|24))'
        if re.match(pattern, slot_value):
            return {"birth_date": slot_value}
        else:
            dispatcher.utter_message(text="Por favor, proporciona una fecha de nacimiento válida en el formato DD/MM/AAAA como 15/04/1984.")
            return {"birth_date": None}

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `email` value."""
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        if re.match(pattern, slot_value):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text="Por favor, proporciona una dirección de correo electrónico válida.")
            return {"email": None} 

# Función para guardar datos en un archivo CSV con coma como delimitador
def save_to_csv(data, filename='/content/03_Med_Bot_ES/data/Historial_clinico.csv'):
    with open(filename, mode='w', newline='') as file:  # Cambiado a 'w' para sobreescribir
        writer = csv.writer(file, delimiter=',')  # Especificar coma como delimitador
        writer.writerow(data.keys())  # Escribir cabeceras
        writer.writerow(data.values())  # Escribir los nuevos datos

# Clase de acción personalizada
class ActionSaveToCSV(Action):

    def name(self) -> Text:
        return "action_save_to_csv"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extraer datos del tracker
        user_data = {
            "Nombre": tracker.get_slot("first_name"),
            "Apellido": tracker.get_slot("last_name"),
            "Sexo": tracker.get_slot("gender"),
            "Email": tracker.get_slot("email"),
            "Fecha de nacimiento": tracker.get_slot("birth_date"),
            "Grupo sanguíneo": tracker.get_slot("blood_type"),
            "Ocupación": tracker.get_slot("occupation"),
            "Estado civil": tracker.get_slot("civil_status"),
            "Historial personal": tracker.get_slot("personal_history"),
            "Antecedentes familiares": tracker.get_slot("family_history"),
            "Uso de alcohol": tracker.get_slot("alcohol_use"),
            "Uso de tabaco": tracker.get_slot("tobaco_use"),
            "Síntomas": tracker.get_slot("symptoms"),
            "Medicación": tracker.get_slot("medication"),
            # Añade más campos según sea necesario
        }

        # Guardar los datos en el archivo CSV
        save_to_csv(user_data)

        dispatcher.utter_message(text="La información ha sido guardada correctamente.\nEn el archivo '{}' verás tus datos disponibles.".format('/content/03_Med_Bot_ES/data/Historial_clinico.csv'))
        return []


## Clase del disclaimer

class ActionDisclaimer(Action):

    def name(self) -> Text:
        return "action_disclaimer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        disclaimer_text = (
            "Disclaimer:\n"
            "Ten en cuenta que los siguientes resultados se han generado automáticamente.\n"
            "La información proporcionada debe utilizarse junto con el juicio clínico y no sustituye el asesoramiento médico profesional.\n"
            "Cualquier decisión relacionada con el cuidado del paciente debe ser tomada por un profesional sanitario autorizado.\n"
            "Este proyecto es creado como una herramienta para facilitar y hacer más eficiente el diagnóstico del profesional sanitario.\n"
            "El desarrollador no se hace responsable del mal uso o interpretación de la información.\n"
        )
        dispatcher.utter_message(text=disclaimer_text)
        return []
