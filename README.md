# Lua Label & Description Translator (FiveM)

Este proyecto es un script en **Python** creado para automatizar la traducción de archivos Lua utilizados en servidores **FiveM**.

El problema original era un archivo de idioma muy extenso que era inviable traducir manualmente sin romper la estructura del script.  
En lugar de traducir todo el archivo, esta herramienta realiza una **traducción contextual**, procesando únicamente los campos necesarios.

## 🚀 ¿Qué hace?

- Analiza archivos `.lua`.
- Detecta específicamente los campos `['label']` y `['description']`.
- Traduce solo el texto dentro de las comillas simples `' '`.
- Mantiene intacta la estructura y sintaxis del archivo original.
- Automatiza horas de trabajo repetitivo.

## 🧠 Enfoque

El script utiliza:
- **Expresiones regulares** para localizar los bloques correctos.
- **googletrans** para la traducción.
- Procesamiento de texto para preservar formato y capitalización.

Aunque mi stack principal es JavaScript / Web, este proyecto muestra la capacidad de **adaptarme a nuevas herramientas según el problema a resolver**.

## 📦 Requisitos

```bash
pip install googletrans==4.0.0rc1
```
▶️ Uso

Colocá tu archivo Lua en el mismo directorio.

Editá las variables:

input_file = "tradu.lua"
output_file = "output.lua"


Ejecutá:

python translator.py

El archivo traducido se generará automáticamente.

🛠 Ejemplo

Antes:

['label'] = 'Vehicle Garage',
['description'] = 'Store your vehicle safely',


Después:

['label'] = 'Garaje de vehículos',
['description'] = 'Guarda tu vehículo de forma segura',
