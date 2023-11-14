# Projet de Dashboard Streamlit pour le Bien-être des Employés

## Introduction

Ce projet est une application de dashboard développée avec Streamlit pour analyser le bien-être des employés. Il s'agit avant tout d'un projet personnel visant à explorer les capacités de Streamlit et à démontrer mes compétences en Python et en tant qu'ingénieur de fiabilité de site (SRE).

Le contexte du bien-être des employés est utilisé ici comme un exemple pour montrer comment Streamlit et les principes SRE peuvent être appliqués dans le domaine des ressources humaines pour améliorer la fiabilité et la disponibilité des systèmes.

## Fonctionnalités

- **Analyse univariée, bivariée et multivariée**
- **Tests statistiques** comme ANOVA, Chi-carré, etc.
- **Matrice de corrélation**
- **Régression logistique** pour la prédiction
- Et bien plus encore...

## Installation et Exécution

### Prérequis

- Python 3.8 ou supérieur
- Docker (optionnel)

### Installation

1. **Clonez ce dépôt GitHub.**
2. **Accédez au répertoire du projet.**
3. **Installez les dépendances** en utilisant le fichier `requirements.txt` :

    ```bash
    pip install -r requirements.txt
    ```

### Exécution

- **Sans Docker** :

    ```bash
    streamlit run Dashboard.py
    ```

- **Avec Docker** :

    ```bash
    docker build -t my_dashboard .
    docker run -p 8501:8501 my_dashboard
    ```

## Contribution

Ce projet est ouvert aux contributions. N'hésitez pas à ouvrir une issue ou à soumettre une pull request.