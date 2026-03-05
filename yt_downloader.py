#!/usr/bin/env python3
import os
import sys
import subprocess

def check_dependencies():
    """Verifica si yt-dlp está instalado."""
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: yt-dlp no está instalado. Ejecuta el instalador primero.")
        sys.exit(1)

def menu():
    print("\n" + "="*30)
    print("  YOUTUBE DOWNLOADER CLI")
    print("="*30)
    
    url = input("\n🔗 Introduce la URL: ").strip()
    if not url:
        print("❌ URL no válida.")
        return

    print("\nFormato:")
    print("1. Video (MP4)")
    print("2. Audio (MP3)")
    opcion = input("Selecciona (1/2): ")

    # Parámetros base: -c (continuar), --no-mtime (fecha actual), --restrict-filenames (evita carácteres raros)
    base_cmd = 'yt-dlp -c --no-mtime --restrict-filenames --no-check-certificates'

    if opcion == "1":
        print("\nCalidad:")
        print("a. 1080p")
        print("b. 720p (Recomendado para 10h+)")
        print("c. 480p")
        calidad = input("Opción (a/b/c): ").lower()
        res = {"a": "1080", "b": "720", "c": "480"}.get(calidad, "720")
        
        comando = f'{base_cmd} -f "bestvideo[height<={res}][ext=mp4]+bestaudio[ext=m4a]/best[height<={res}][ext=mp4]/best" "{url}"'
    
    elif opcion == "2":
        comando = f'{base_cmd} -x --audio-format mp3 --audio-quality 0 "{url}"'
    
    else:
        print("❌ Opción cancelada.")
        return

    print("\n🚀 Iniciando/Reanudando descarga...")
    try:
        os.system(comando)
    except KeyboardInterrupt:
        print("\n\n🛑 Descarga pausada. Ejecuta de nuevo para reanudar.")

if __name__ == "__main__":
    check_dependencies()
    menu()
