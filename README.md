# Backend Task

A Django-based backend project with GIS support (GDAL) and common development workflows automated via a Makefile.

---

## 🚀 Features
- Django backend with modular apps
- PostgreSQL / SQLite (default) support
- GIS features powered by **GDAL**
- Makefile automation for development tasks
- Ready-to-extend for production

---

## 📦 Requirements
- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/) and [virtualenv](https://virtualenv.pypa.io/en/latest/)
- GDAL library installed on your system  
  - Ubuntu/Debian:  
    ```bash
    sudo apt update
    sudo apt install -y gdal-bin libgdal-dev
    ```
  - macOS (Homebrew):  
    ```bash
    brew install gdal
    ```
  - Fedora:  
    ```bash
    sudo dnf install gdal gdal-devel
    ```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/akhad-abdullaev/backend_task.git
   cd backend_task
