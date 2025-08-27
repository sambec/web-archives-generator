# web archives generator

Ce dépôt contient une expérimentation de collecte automatisée et de vérification de la qualité des archives numériques (ici des vidéos YouTube au format MP4), destinée à créer des sources exploitables scientifiquement et patrimonialement.

##  Contexte

Dans le cadre de l'archivage de la jouabilité, il faut aux archivistes et au historiens d'aujourd'hui des outils capables de capter les traces de ces expériences de jeux en ligne. Nombre des archives de la jouabilité se trouvent dans des vidéos aujourd'hui hebergées sur YouTube. Nous proposons donc un script capable de réaliser une collecte automatisée et contrôlé de vidéos depuis YouTube. Inspiré des pratiques d’automatisation et de contrôle qualité issues de l’industrie du jeu vidéo, ce projet applique une logique de data continuous integration à l’archivage numérique. L’objectif est de garantir la qualité des collectes au plus tôt dans le flux de production, une attention particulièrement cruciale lorsque la synchronisation entre image, son et métadonnées est un enjeu fondamental.

##  Fonctionnalités

- Acquisition automatisée de vidéos depuis YouTube (via `yt-dlp`)  
- Contrôles d’intégrité (empreintes SHA-256), validation technique (`ffmpeg`)  
- Extraction de métadonnées techniques (via `MediaInfo` / `pymediainfo`)  
- Structuration et documentation des fichiers collectés (`pandas`, CSV)  
- Journalisation détaillée des opérations  
- Analyse statistique des collectes (durée totale, volumes, taux d’échec)  
- Visualisations interactives (diagrammes de statut, scatter plots, chronologie)  
- Simulation de fichiers corrompus pour tester la robustesse des contrôles  
- Chaîne complète, reproductible et auditable dans un notebook Jupyter  


<!-- ![Schéma pipeline](figures/schema_process.png) -->
<p align="center">
  <img src="figures/schema_process.png" alt="Schéma pipeline" width="250"/>
</p>

##  Outils utilisés

| Outil       | Fonction principale | Motivation du choix |
|-------------|---------------------|----------------------|
| `yt-dlp`    | Téléchargement des vidéos depuis YouTube | Robuste, fréquemment mis à jour, supporte de nombreuses plateformes |
| `SHA-256`   | Empreinte cryptographique pour l’intégrité des fichiers | Sensible à toute altération, garantit la traçabilité |
| `ffmpeg`    | Vérification technique et lisibilité des fichiers vidéo | Référence éprouvée pour le traitement multimédia |
| `MediaInfo`  | Extraction de métadonnées normalisées (format, codec, débit, fps) | Essentiel pour détecter anomalies et documenter chaque objet |
| `pandas`    | Structuration, analyse, génération de rapports CSV | Puissant pour la gestion de données tabulaires en Python |

Ces outils forment un flux cohérent, qui garantit acquisition, vérification, documentation et traçabilité.

##  Accès au notebook

La chaîne complète est documentée et exécutable via un notebook Jupyter, accessible ici :  
[ExperienceArchivage.ipynb](https://github.com/sambec/web-archives-generator/blob/main/ExperienceArchivage.ipynb)

Ce notebook permet :
- d’exécuter pas à pas chaque étape du processus,
- d’analyser les résultats,  
- de comprendre les choix techniques (intégrité, alerte, journalisation).

##  Installation & Utilisation

Cloner le dépôt :
```bash
git clone https://github.com/sambec/web-archives-generator.git
```

Exécution :

 Lancez le notebook ExperienceArchivage.ipynb sur votre ordinateur directement ou vous pouvez l'ouvrir et l'excuter dans votre navigateur grâce à [Google Colab](https://colab.research.google.com/). 

 ## Note

 Ce script a été réalisé dans le cadre de la rédaction de mon mémoire de fin d’étude (M2 TNAH, École nationale des chartes), après un stage de 6 mois à Ubisoft en tant qu’ingénieure de données chargée d’automatiser la vérification de la qualité des données de production.

Il fait partie des livrables techniques présentés dans ce mémoire et a été développé avec l’aide d’Adrien Lafage (doctorant en Intelligence Artificielle), dont l’expertise a permis d’assurer l’intégration correcte des librairies et la mise en place d’un prototype robuste.