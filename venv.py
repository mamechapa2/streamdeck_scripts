#!/usr/bin/env python3
import os
import sys
import subprocess

def main():
    #verificar que se haya pasado la ruta del script a ejecutar y el entorno virtual
    if len(sys.argv) < 4:
        print("Uso: {} ruta_del_venv ruta_cd nombre_ventana".format(sys.argv[0]))
        sys.exit(1)

    #ruta
    venv_dir = os.path.abspath(sys.argv[1])
    ruta_cd = os.path.abspath(sys.argv[2])
    nombre_ventana = sys.argv[3]

    #verificar que exista el directorio del entorno virtual
    if not os.path.isdir(venv_dir):
        print("El directorio del entorno virtual no existe: {}".format(venv_dir))
        sys.exit(1)

    #ruta del venv de python
    activate_script = os.path.join(venv_dir, "Scripts", "activate")
    if not os.path.exists(activate_script):
        print("No se encontró el script de activación: {}".format(activate_script))
        sys.exit(1)

    # abrir una nueva ventana de CMD y activar el entorno virtual, despues cambiar al directorio del script
    # 'start "Título" cmd /k "call <ruta_activate_script>"'
    # - start "Título": titulo de la ventana de la consola.
    # - cmd /k: ejecuta el comando y deja la ventana abierta.
    # - call: ejecuta el script y retorna al script que lo llamó.
    command = f'start "{nombre_ventana}" cmd /k "call {activate_script} && cd {ruta_cd}"'
    # command = (
    #     f'start "{nombre_ventana}" powershell.exe -NoExit -Command '
    #     f'"Set-Location \'{ruta_cd}\'; . \'{activate_script}\'"'
    # )
    # command = (
    #     f'wt new-tab --title "{nombre_ventana}" '
    #     f'powershell -NoExit -Command "Set-Location \'{ruta_cd}\'; . \'{activate_script}\'"'
    # )
    

    #ejecutar el script
    subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    main()
