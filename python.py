#!/usr/bin/env python3
import os
import sys
import subprocess
from time import sleep

def main():
    #verificar que se haya pasado la ruta del script a ejecutar y el entorno virtual
    if len(sys.argv) < 3:
        print("Uso: {} ruta_del_script.py venv [argumentos]".format(sys.argv[0]))
        sys.exit(1)
    
    #rutas
    script_path = os.path.abspath(sys.argv[1])
    script_dir = os.path.dirname(script_path)

    #pongo de nombre el nombre del script en la ventana de la consola
    os.system("title " + os.path.basename(script_path))

    #cambiar al directorio del script
    os.chdir(script_dir)

    #verificar que exista el directorio del entorno virtual
    venv_dir = sys.argv[2]
    if not os.path.isdir(venv_dir):
        print("No se encontró el directorio del entorno virtual: {}".format(venv_dir))
        sys.exit(1)

    #ruta del venv de python
    python_bin = os.path.join(venv_dir, "Scripts", "python.exe")

    if not os.path.exists(python_bin):
        print("No se encontró el intérprete de Python en el entorno virtual: {}".format(python_bin))
        sys.exit(1)

    #argumentos del script
    target_args = sys.argv[3:]
    command = [python_bin, script_path] + target_args

    #ejecutar el script
    try:
        result = subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        # print("Ocurrió un error al ejecutar el script: {}".format(e))
        # sys.exit(e.returncode)
        #llamo a main() para que no se cierre la ventana y espero que el usuario pulse una tecla
        input("Reiniciar")
        main()

if __name__ == "__main__":
    main()
