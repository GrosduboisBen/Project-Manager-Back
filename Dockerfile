# Utiliser une image Python officielle
FROM python:3.11-slim

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    curl \
    && apt-get clean

# Ajouter un utilisateur pour éviter de travailler en tant que root
RUN useradd -m vscode
USER vscode

# Définir le répertoire de travail
WORKDIR /workspace

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="${HOME_DIR}/.local/bin:${PATH}"