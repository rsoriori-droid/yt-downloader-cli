# YouTube Downloader CLI 🚀

A robust, terminal-based YouTube downloader built for **Pop!_OS** and other Linux distributions. Designed specifically to handle long-duration videos (10h+) with ease and reliability.

## ✨ Features
- **Long Video Support:** Optimized to handle downloads of 10 hours or more without timing out.
- **Resumable Downloads:** If your PC shuts down or the connection drops, simply run the command again to pick up exactly where you left off.
- **Quality Selection:** Choose between 1080p, 720p (recommended for long videos), or 480p.
- **MP3 Extraction:** High-quality audio-only mode.
- **Clean Filenames:** Automatically sanitizes filenames to avoid issues with special characters in Linux.

## 🛠️ Installation

This repository includes an `install.sh` script to set up all dependencies (`yt-dlp`, `ffmpeg`, `pipx`) and register the global command.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rsoriori-droid/yt-downloader-cli.git](https://github.com/rsoriori-droid/yt-downloader-cli.git)
   cd yt-downloader-cli
