# Utilisez l'image de base Python
FROM python:3.12


# Répertoire de travail dans le conteneur
WORKDIR /app

COPY requirements.txt /app/

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

VOLUME [ "/app" ]

# Commande pour exécuter l'application
CMD [ "python", "api.py" ]