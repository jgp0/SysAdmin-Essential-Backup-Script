import os
import shutil
import time
import zipfile

# Directorio de origen (los archivos/folders a respaldar)
origen = 'test/old'

# Directorio de destino (dónde se guardarán las copias de seguridad)
destino = 'test/new'

# Nombre del archivo de copia de seguridad
nombre_copia_seguridad = f'backup_{time.strftime("%Y%m%d_%H%M%S")}.zip'

# Crear un archivo zip para la copia de seguridad
with zipfile.ZipFile(os.path.join(destino, nombre_copia_seguridad), 'w', zipfile.ZIP_DEFLATED) as archivo_zip:
    for carpeta_raiz, _, archivos in os.walk(origen):
        for archivo in archivos:
            ruta_archivo_completa = os.path.join(carpeta_raiz, archivo)
            archivo_zip.write(ruta_archivo_completa, os.path.relpath(ruta_archivo_completa, origen))

print(f'Copia de seguridad creada en: {os.path.join(destino, nombre_copia_seguridad)}')