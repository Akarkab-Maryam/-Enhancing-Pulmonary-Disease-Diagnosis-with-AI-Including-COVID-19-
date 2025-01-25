# Amélioration du diagnostic des maladies pulmonaires grâce à l'IA (y compris la COVID-19)

## Brève description
Ce projet combine l'intelligence artificielle et l'imagerie médicale pour diagnostiquer les maladies pulmonaires, notamment la COVID-19, en utilisant des réseaux de neurones convolutifs (CNN).

---

## Objectif
Développer un modèle d'IA capable d'analyser les radiographies thoraciques afin d'améliorer la précision et la rapidité des diagnostics.

---

## Techniques utilisées
- **Prétraitement d'images** : Égalisation d'histogrammes pour améliorer la qualité des images.
- **Modélisation et entraînement** : 
  - Développement d'un CNN formé sur la base de données COVID-QU (15 000 images).
  - Optimisation des paramètres et suivi des performances.
- **Évaluation des performances** : 
  - Utilisation de métriques avancées telles que la matrice de confusion et la courbe ROC.

---

## Résultats obtenus
- Modèle **très performant** après 20 époques d'entraînement.
- Potentiel d'application pour des diagnostics **plus rapides et plus précis** dans un contexte clinique.

---

## Compétences développées
- Apprentissage automatique et apprentissage profond.
- Utilisation de bases de données médicales (COVID-QU).
- Conception et implémentation de modèles CNN.
- Analyse et interprétation des métriques d'évaluation des modèles.

---

## Outils et technologies
- **Langages de programmation** : Python.
- **Bibliothèques et frameworks** : TensorFlow/Keras, NumPy, Matplotlib.
- **Techniques** : Prétraitement d'images médicales.

---

## Structure du projet
1. **Prétraitement des données** : Optimisation des images radiographiques.
2. **Développement du modèle CNN** : Architecture personnalisée pour un diagnostic précis.
3. **Entraînement et validation** : Analyse des performances sur la base de données COVID-QU.
4. **Documentation des résultats** : Visualisation des métriques et des performances du modèle

---

## Pourquoi ce projet est important
En exploitant l'intelligence artificielle, ce projet vise à fournir un outil diagnostique innovant et accessible, particulièrement utile en période de crise sanitaire comme celle de la COVID-19.


![image](https://github.com/user-attachments/assets/e50b4222-8ce6-42a3-abff-cb583a270beb)

## Résultats du prétraitement des images médicales

L'image ci-dessus illustre une comparaison entre :  
1. **L'image originale** (à gauche) : Radiographie thoracique brute.  
2. **Le résultat de l'algorithme de détection de contours Canny** (à droite) : Permet d'extraire les contours significatifs pour identifier des structures pulmonaires et anomalies potentielles.  

Ce prétraitement est une étape clé pour réduire les informations inutiles et améliorer l'entrée des images dans le modèle d'IA.


![image](https://github.com/user-attachments/assets/66d43709-7853-43a9-8f64-00ad54a96f61)
![image](https://github.com/user-attachments/assets/a1574617-6bc1-47cc-811c-82870c452277)
![image](https://github.com/user-attachments/assets/16c73389-957e-47f8-86db-c45b15d53154)
![image](https://github.com/user-attachments/assets/b12c4aef-3d3e-4f2d-b6e7-5b34f0a835ae)
![image](https://github.com/user-attachments/assets/54b7dd31-b870-4277-addd-8ceb62858f1d)
![image](https://github.com/user-attachments/assets/7c060762-d97a-4ff6-8a5f-5e7d794a065d)



