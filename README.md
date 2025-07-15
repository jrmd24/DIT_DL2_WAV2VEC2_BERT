---
title: DIT DL2 WAV2VEC2 BERT
emoji: 🏃
colorFrom: yellow
colorTo: pink
sdk: gradio
sdk_version: 5.36.2
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
# DIT_DL2_WAV2VEC2_BERT

Ce dépôt contient le code d'une application d'analyse de sentiment associé à des déclarations au format audio.

## Le modèle
Le modèle permettant d'automatiser cette analyse est construit comme suit :
- Un module de reconnaissance automatisée de la parole basé sur le modèle "facebook/wav2vec2-base-960h" disponible sur huggingface. C'est un modèle a été préentraîné sur 960 heures d'audio anglaise echantillonné à 16kHz. Nous l'utilisons tel quel pour la transcription des audios en texte
- Un module d'analyse de sentiment basé un modèle BERT "google-bert/bert-base-uncased" également disponible sur huggingface. Ce modèle BERT nous donne une représentation fiable du texte, qui lui est soumis, dans un espace. Cette représentation est ensuite projetée sur un première couche cachée linéaire de 30 neurones. Cette couche cachée est suivie de la couche de sortie composée de trois neurones pour effectuer la classification objet du projet selon les modalités souhaitées : "Positif", "Négatif", "Neutre". Le modèle BERT de base n'a pas été modifié pendant l'entraînement à l'analyse de sentiment à partir d'entrée en format texte.

## Le Dataset
L'entraînement et l'évaluation de la chaîne d'analyse a été effectué avec les données du sous-ensemble "Voxceleb" du dataset "asapp/slue" également disponible sur huggingface. Ce jeu de données est fait de correspondances entre des enregistrements audio de paroles de célébrités, la transcription textuelle de cette dernière et le sentiment associé. Ce jeu de données est subdivisé en trois sous-ensembles nommés "dev", "fine-tune" et "test". Dans le cadre de ce projet, nous avons utilisé les sous-groupes "fine-tune" et "test" respectivement pour l'entraînement et l'évaluation de la chaîne d'analye de sentiment. Ils comprennent respectivement 5777 et 3553 enregistrements. 

## L'entraînement et l'évaluation
L'entraînement a été fait pour ajuster les poids des couches de neurones ajoutées au modèle BERT de base. Il a été effectué sur google colab en utilisant les correspondances entre texte et sentiment du sous-groupe "fine-tune" du dataset.
L'évaluation a également été effectuée sur google colab en utilisant les correspondances entre le texte et les sentiments faites dans le sous-groupe "test" du dataset pour la partie BERT dans un premier temps. Dans un second temps, la correspondance entre fichiers audio et sentiments disponibles dans le même sous-groupe ont été utilisée pour l'évaluation de l'ensemble de la chaîne d'analyse de sentiment. Nous en avons tiré une matrice de confusion ainsi qu'un accuracy globale.
Les graphes d'évolution des fonctions de pertes lors de l'entraînement et lors de l'évaluation de l'analyse textuelle ainsi que la matrice de confusion et l'accuracy globales sont disponibles sur la page de l'application permettant de tester le modèle obtenu : https://huggingface.co/spaces/jrmd/DIT_DL2_WAV2VEC2_BERT
Toutes les actions d'entraînement, d'évaluation et de production sont disponibles dans le fichier "AudioSpeechSentimentAnalysis_JRMDIOUF.ipynb" qui a été utilisé sur google colab pour profiter des GPU qui y sont disponibles. Le fichier "audiospeechsentimentanalysis_jrmdiouf.py" est le pendant du notebook au format python simple. Mais ce dernier est utilisé par le fichier "app.py" pour les inférences demandées par les utilisateurs de l'application en ligne.

## Mise à disposition du modèle obtenu
Le modèle obtenu peut être testé via l'application gradio disponible à l'URL : https://huggingface.co/spaces/jrmd/DIT_DL2_WAV2VEC2_BERT
Vous pouvez y télécharger une audio en Anglais présente sur votre machine et voir le sentiment associé que vous proposera le modèle obtenu suite à nos travaux. Le code de l'application est disponible dans le fichier "app.py".

## API
Vous pouvez utiliser le modèle à travers une API mise à disposition à la même URL et expose une action predict. Vous pourrez voir comment utiliser l'API en vous référant au fichier "demo_api_client.py"