#Usa una imagen oficial de python
FROM python:3.8-slim-buster

#Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

#Copiamos el archivo de requisitos al directorio de trabajo
COPY requirements.txt .

#Instalamos las dependencias 
RUN pip install --no-cache-dir -r requirements.txt

# Instalar matplotlib
RUN pip install matplotlib

 

#Copiamos el resto de la aplicación al directorio de trabajo
COPY . .

# Cambiar el comando para ejecutar el nuevo script
CMD ["python", "modelo_de_tren.py"]