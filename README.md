# EasyTask

EasyTask est une application de gestion de tâches simple développée avec Django. Elle permet aux utilisateurs de créer, gérer et visualiser leurs tâches, avec un indicateur de statut pour chaque tâche (complétée ou en cours).

## Fonctionnalités

- Ajouter des tâches avec un titre.
- Marquer les tâches comme complétées ou en cours.
- Afficher la liste des tâches, triée par date de création.
- Utilisation d'un utilisateur par défaut si l'utilisateur n'est pas connecté.

## Prérequis

- Python 3.10 ou supérieur
- Django 5.x
- SQLite (par défaut) ou MySQL (en option)
- Pip pour installer les dépendances

## Installation

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/votre-utilisateur/easytask.git
   cd easytask
   ```

2. Créez et activez un environnement virtuel :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Windows, utilisez .venv\Scripts\activate
   ```

3. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations de la base de données :
   ```bash
   python manage.py migrate
   ```

5. Créez un superutilisateur (facultatif) :
   ```bash
   python manage.py createsuperuser
   ```

6. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

## Utilisation

1. Accédez à l'application dans votre navigateur à l'adresse `http://localhost:8000/`.
2. Vous pouvez ajouter des tâches via le formulaire sur la page d'accueil.
3. Les tâches sont affichées avec un indicateur de statut :
   * **Complété** : bouton vert avec un pouce levé.
   * **À faire** : bouton rouge avec une croix.
4. Si un utilisateur n'est pas authentifié, les tâches seront associées à un utilisateur par défaut.

## Structure du projet

* `feed/models.py` : Définition du modèle `Task` pour les tâches.
* `feed/views.py` : Gestion de la logique des vues (ajout, affichage des tâches).
* `templates/` : Contient les fichiers HTML pour les vues (inclus `base.html` pour le layout global).
* `static/` : Fichiers CSS, JavaScript, et les assets statiques.

## Dépendances

Les principales bibliothèques utilisées dans ce projet sont :
* **Django** : Framework backend pour la gestion des vues, modèles et logique de l'application.
* **Bootstrap** : Utilisé pour le style des pages avec une intégration de Font Awesome pour les icônes.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez améliorer EasyTask, suivez ces étapes :

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commitez vos modifications (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Pushez la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.

**Auteur** : Dassoah Maixent