# Object_tracker
Este proyecto es un sistema de seguimiento y conteo de vehículos creado con Python y OpenCV. Este proyecto se puede utilizar para el monitoreo del tráfico, el análisis de datos y otras aplicaciones relacionadas con el flujo de vehículos y la gestión del tráfico

# Vehicle Tracking and Counting System

Este proyecto utiliza Python y OpenCV para detectar, rastrear y contar vehículos que pasan a través de una zona de interés en una grabación de video. Se ha implementado un sistema de detección y seguimiento que asigna un ID único a cada vehículo, permitiendo un conteo preciso a medida que cruzan una línea definida en el área de interés.

## Estructura del Proyecto

- `detector.py`: Script principal que carga el video, define el área de interés, aplica la detección de vehículos usando sustracción de fondo y rastrea cada vehículo con un ID único.
- `tracker.py`: Clase `Tracker` que maneja la lógica de seguimiento de vehículos mediante el cálculo de distancias entre el centro de los objetos detectados, asignando y manteniendo IDs únicos para cada vehículo.
- `resources`: Carpeta que contiene el archivo de video (`Street.mp4`) usado en el análisis.

## Requisitos

- Python 3.x
- OpenCV
- Numpy (opcional, según configuración de OpenCV)

## Instalación

Instala las dependencias en el entorno virtual
```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  .\venv\Scripts\activate  # Windows
  pip install opencv-python
