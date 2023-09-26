# LITRevu - Publication et sollicitation de critique de Livre/Article

<p align="center">
<img src="./LITReview/static/assets/logo.png" width="100px">
</p>

## Projet

Création d'une application web permettant aux utilisateurs de publier ou de solliciter une critique sur un livre ou un article.

## Fonctionnalités

Un visiteur non connecté doit pouvoir :
- s’inscrire ;  
- se connecter. 

Un utilisateur connecté doit pouvoir : 
- consulter son flux contenant les derniers billets et les critiques des utilisateurs qu'il suit, classés par ordre antichronologique ;
- créer de nouveaux billets pour solliciter des critiques sur un livre ou un article ;
- rédiger de nouvelles critiques en réponse à des billets ;
- créer un billet et une critique sur ce même billet en une seule étape, pour rédiger des critiques "à partir de zéro" ;
- voir, modifier et supprimer ses propres billets et critiques ;
- suivre d'autres utilisateurs en entrant leur nom d'utilisateur ;
- voir la liste des utilisateurs qu'il suit et choisir de suivre de nouveaux utilisateurs ;
- arrêter de suivre ou bloquer un utilisateur.

Un développeur doit pouvoir : 
- configurer un environnement local et gérer le site en se basant sur la documentation détaillée présentée dans ce fichier README.md.

Le site doit :  
- présenter une interface utilisateur correspondant à celle des maquettes en termes d'architecture, le design restant libre ; 
- offrir une interface utilisateur propre et épurée. 

## Installation

- Python 3.10
- pip 22.3.1

**Cloner le répository suivant**
> https://github.com/DomninBenoit/LITRevu.git

Installation de l'environnement virtuel 
> python -m venv ENV   

Activation de l'environnement virtuel :
> .\ENV\Scripts\activate

Installation des dépendances:
> pip install -r requirements.txt

Génération de la 'SECRET_KEY' :
- Dans le répertoire contenant 'settings.py', créez un fichier 'settings_secret.py'.
- Utilisez la commande suivante:
> python generate_secret_key.py
- Ecrivez dans le fichier 'settings_secret.py':
> SECRET_KEY = "resultat de la commande python generate_secret_key.py"

## Utilisation

- Assurez-vous que l'environnement virtuel est activé, puis lancez le serveur :
> python .\manage.py runserver 

- Depuis votre navigateur, accédez à l'adresse suivante :  
> http://127.0.0.1:8000/

Vous pouvez désormais créer vos utilisateurs et vos différents articles/livres.



