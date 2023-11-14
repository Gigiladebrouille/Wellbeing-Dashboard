# Utiliser une image de base Python
FROM python:3.8-slim-buster

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendance dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le fichier Dashboard.py dans le conteneur
COPY Dashboard.py .

# Exécuter l'application Streamlit
CMD ["streamlit", "run", "Dashboard.py"]
