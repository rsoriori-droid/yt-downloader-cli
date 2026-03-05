#!/bin/bash

echo "📦 Instalando dependencias para YouTube Downloader..."

# Actualizar e instalar ffmpeg (necesario para unir audio y video)
sudo apt update && sudo apt install -y ffmpeg python3-pip pipx

# Instalar la última versión de yt-dlp usando pipx
pipx install yt-dlp
pipx ensurepath

# Dar permisos al script y moverlo a binarios locales
chmod +x yt_downloader.py
sudo cp yt_downloader.py /usr/local/bin/descargar

echo "✅ Instalación completada."
echo "Escribe 'descargar' en cualquier terminal para empezar."
