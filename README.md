# LITRevu - Publication et sollicitation de critique de Livre/Article

<p align="center">
<img src="./LITReview/static/assets/logo.png" width="100px">
</p>

## Projet

Création d'une application web qui permet aux utilisateurs de publier 
ou de demander une critique sur un Livre ou un Article.

## Fonctionnalités

Un visiteur non connecté doit pouvoir :
- s’inscrire ;  
- se connecter. 

Un utilisateur connecté doit pouvoir :  
- consulter son flux contenant les derniers billets et les critiques des
utilisateurs qu’il suit, classés par ordre antichronologique ;  
- créer des nouveaux billets pour demander des critiques sur un livre/un
article ;  
- créer des nouvelles critiques en réponse à des billets ;  
- créer un billet et une critique sur ce même billet en une seule étape, pour
créer des critiques « à partir de zéro »  
- voir, modifier et supprimer ses propres billets et critiques ;  
- suivre les autres utilisateurs en entrant leur nom d'utilisateur ;  
- voir qui il suit et suivre qui il veut ;  
- arrêter de suivre ou bloquer un utilisateur.  

Un développeur devra pouvoir :  
- créer un environnement local et gérer le site en se basant sur la
documentation détaillée présentée dans le fichier README.md.  

Le site devra :  
- avoir une interface utilisateur correspondant à celle des wireframes dans son
architecture, le design restant assez libre ;  
- avoir une interface utilisateur propre et minimale.  

## Installation

- Python 3.10
- pip 22.3.1

installation de l'environnement virtuel:
> pip install venv  
> python -m venv ENV   

Lancer l'environnement virtuel:
> .\ENV\Scripts\activate

Installation des dépendances:
> pip install -r requirement.txt

## Utilisation

- Vérifier que l'environnement virtuel soit bien en fonction puis lancer le serveur:
> python .\manage.py runserver 

- depuis votre navigateur, acceder à l'adresse suivante :  
> http://127.0.0.1:8000/

Vous pouvez maintenant créé vos utilisateurs et vos différents articles/livres.



