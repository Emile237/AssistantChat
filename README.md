# Assistant Chat

## Description du projet :

  Le projet consiste en un assistant personnel basé sur le langage naturel, qui utilise la technologie de traitement du langage naturel pour comprendre et répondre aux requêtes de l'utilisateur. Il integre l'assistant de chatGpt pour pouvoir généré des question. Ainsi elle aide l'utilisateur a transmettre sa question par la parole et recevoir une réponse verbale.
## Installation:

  Pour une utilisation de mon apllication vous aurez besoin de:
  + Clonez le dépôt en exécutant la commandeg
  ```
  git clone https://github.com/AssistantChat/chat.git
  ```
  + Accédez au dossier du projet :
  ```
  cd ChatGPT-Voice-Assistant
  ```
  + Installez les dépendances nécessaires avec Pipenv en exécutant la commande suivante :
 ```
 pipenv install
 ```
 + Activez l'environnement virtuel
 ```
 pipenv shell
 
 ```
 + Configurez le fichier .env en ajoutant votre clé API OpenAI que vous pouvez avoir en vous rendant sur: https://platform.openai.com/account/api-keys et noter votre clé dans la variable CHATGPKKEY.
 ```
 CHATGPKKEY=<votre_clé_api_openai>
```

## Utilisation
+ nous pouvons à présent éxécuté notre projet par la commande 
```
python ./main.py
```
+ Dites quelque chose après avoir vu le message Dites quelque chose! s'afficher.

+ L'assistant vocal traitera votre requête et vous répondra avec une réponse sous forme de texte et de voix.
## Configuration
Si vous avez besoin de configurer l'application, vous pouvez le faire en modifiant le fichier .env. Assurez-vous de configurer votre clé API OpenAI avant de lancer l'application.

## Contribution 
Les contributions à ce projet sont les bienvenues. Si vous souhaitez contribuer, vous pouvez le faire en suivant les étapes suivantes :

+ Forkez le dépôt sur votre compte GitHub.

+ Créez une branche pour votre contribution :
```
+ git checkout -b nom-de-votre-branche
```
+ Faites vos modifications et committez-les :
```
git commit -m "votre message de commit"
```
+ Poussez vos modifications sur votre fork :
```
git push origin nom-de-votre-branche
```
Créez une demande de fusion sur le dépôt original.
## Licence 
