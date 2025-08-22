# web archives generator

Ce dépôt contient une expérimentation de collecte automatisée et de vérification de la qualité des archives numériques (notamment des vidéos YouTube au format MP4), destinée à créer des sources exploitables scientifiquement et patrimonialement.

##  Contexte

Inspiré des pratiques d’automatisation et de contrôle qualité issues de l’industrie du jeu vidéo, ce projet applique une logique de **data continuous integration** à l’archivage numérique. L’objectif est de garantir la qualité des collectes au plus tôt dans le flux de production—une attention particulièrement cruciale lorsque la synchronisation entre image, son et métadonnées est un enjeu fondamental.

##  Fonctionnalités

- Acquisition automatisée de vidéos depuis YouTube (via `yt-dlp`)
- Contrôles d’intégrité (empreintes SHA-256), validation technique (`ffmpeg`)
- Structuration des fichiers collectés et des métadonnées (via `pandas`)
- Journalisation détaillée des opérations
- Génération de rapports exploitables (fichiers CSV)
- Chaîne complète, reproductible, documentée dans un notebook Jupyter

![Schéma pipeline](figures/process_pipeline.png)

##  Outils utilisés

| Outil       | Fonction principale | Motivation du choix |
|-------------|---------------------|----------------------|
| `yt-dlp`    | Téléchargement des vidéos depuis YouTube | Robuste, fréquemment mis à jour, supporte de nombreuses plateformes |
| `SHA-256`   | Empreinte cryptographique pour l’intégrité des fichiers | Sensible à toute altération, garantit la traçabilité |
| `ffmpeg`    | Vérification technique et lisibilité des fichiers vidéo | Référence éprouvée pour le traitement multimédia |
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

Clone le dépôt :
```bash
git clone https://github.com/sambec/web-archives-generator.git
cd web-archives-generator

Installe les dépendances (recommandé dans un environnement virtuel) :

pip install -r requirements.txt

Exécution :

    Lance le notebook ExperienceArchivage.ipynb pour suivre le pipeline complet

    Ou bien exécute le script principal (ex. python collect_and_validate.py) pour automatiser le processus

Structure du dépôt

web-archives-generator/
├── ExperienceArchivage.ipynb      # Notebook de la chaîne documentée
├── collect_and_validate.py        # Script principal (exemple)
├── requirements.txt               # Dépendances Python
├── README.md                      # Présentation et usage
└── figures/
    └── process_pipeline.png       # Schéma du pipeline