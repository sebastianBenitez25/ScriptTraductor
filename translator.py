from googletrans import Translator
import re

def translate_lua_file(input_file, output_file, target_language='es'):
    """
    Traduce las etiquetas 'label' y 'description' de un archivo lua manteniendo el formato.
    
    Args:
        input_file (str): Ruta del archivo de entrada
        output_file (str): Ruta del archivo de salida
        target_language (str): Código del idioma destino (default: 'es' para español)
    """
    translator = Translator()
    
    # Patrones para encontrar las líneas de label y description
    label_pattern = r"(\['label'\] = ')(.+?)(')"
    desc_pattern = r"(\['description'\] = ')(.+?)(')"
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            
        def translate_match(match):
            """Función auxiliar para traducir el contenido dentro de las comillas"""
            prefix, text, suffix = match.groups()
            translated = translator.translate(text, dest=target_language).text
            # Capitalizar primera letra si el original estaba capitalizado
            if text[0].isupper():
                translated = translated.capitalize()
            return f"{prefix}{translated}{suffix}"
        
        # Realizar las traducciones
        content = re.sub(label_pattern, translate_match, content)
        content = re.sub(desc_pattern, translate_match, content)
        
        # Guardar el archivo traducido
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print(f"Traducción completada. Archivo guardado como: {output_file}")
        
    except Exception as e:
        print(f"Error durante la traducción: {str(e)}")

# Ejemplo de uso
if __name__ == "__main__":
    input_file = "tradu.lua"  # Cambia esto por tu archivo de entrada
    output_file = "output2.lua"  # Cambia esto por tu archivo de salida deseado
    translate_lua_file(input_file, output_file)