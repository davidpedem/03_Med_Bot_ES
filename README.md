# Consulta_Med_Bot
**Instrucción CLAVE**: TIENES QUE DESCARGARTE EL ARCHIVO LLAMADO `Consulta_03_Med_Bot_ES_UR_David_Peña.ipynb`. Y SUBIRLO A GOOGLE DRIVE. Desde ahí lo abres y le das a conectar.
## Resumen del Proyecto

Este proyecto de Trabajo de Fin de Máster (TFM) aborda el desarrollo y análisis de un modelo en tres partes:

1. **Desarrollo de un Chatbot de Consulta Médica en RASA:** Se ha creado un chatbot que realiza un interrogatorio habitual de una consulta médica. Recopila datos personales del paciente, síntomas, antecedentes familiares, medicamentos, y uso de alcohol y tabaco.
   
2. **Procesamiento de un Corpus de Enfermedades Hematológicas:** Tras generar el historial clínico, se descarga un corpus de enfermedades hematológicas previamente creado. Se utilizan técnicas de procesamiento del lenguaje natural (NLP) para almacenar solo información relevante para el programa.
   
3. **Cálculo de Semejanza entre Historial Clínico y Enfermedades:** Los archivos procesados se convierten en vectores para calcular los porcentajes de semejanza entre el historial clínico y cada una de las enfermedades del corpus. Se generan dos archivos: 
   - El historial clínico completo para el médico.
   - Un archivo con los porcentajes de posibles enfermedades identificadas, ordenadas de mayor a menor.

Además, se incluye una interpretación de los resultados y una evaluación de las posibles limitaciones y mejoras.

## Instrucciones para el Usuario

### Requisitos Previos

- **Cuenta de Google:** Necesitarás una cuenta de Google para usar Google Drive y Google Colab.
- **Google Drive:** Asegúrate de tener espacio suficiente en tu Google Drive para subir y ejecutar el archivo.

### Descarga y Configuración

1. **Descargar el Documento:**
   - Descarga el archivo `Consulta_03_Med_Bot_ES_UR_David_Peña.ipynb`.

2. **Subir a Google Drive:**
   - Sube el archivo descargado a tu Google Drive.

3. **Abrir en Google Colab:**
   - Abre Google Colab y selecciona la opción de abrir un archivo desde Google Drive.
   - Navega hasta el archivo `Consulta_03_Med_Bot_ES_UR_David_Peña.ipynb` y ábrelo.

### Ejecución del Código

1. **Configurar y Ejecutar el Chatbot:**
   - Sigue las instrucciones dentro del cuaderno de Colab para configurar y ejecutar el chatbot de consulta médica.

2. **Interacción con el Chatbot:**
   - Interactúa con el chatbot proporcionando la información requerida (datos personales, síntomas, antecedentes, etc.).

3. **Procesamiento y Resultados:**
   - Permite que el cuaderno procese la información y genere los archivos de resultados.
   - Descarga los archivos generados:
     - El historial clínico con la información introducida.
     - El archivo con los porcentajes de enfermedades posibles.

### Notas Adicionales

- **Interpretación de Resultados:** Revisa la sección final del cuaderno para entender la interpretación de los resultados y las limitaciones del modelo.
- **Mejoras y Evaluaciones:** Considera las sugerencias de mejoras y las evaluaciones presentadas para futuros desarrollos.



Si tienes alguna pregunta o necesitas asistencia, no dudes en contactarme a través de mi perfil de GitHub.

---

¡Gracias por utilizar mi proyecto de TFM! Espero que encuentres útil este trabajo y que te sirva para tus necesidades de consulta médica automatizada.
