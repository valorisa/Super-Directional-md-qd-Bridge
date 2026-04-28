# Super-Directional-md-qd-Bridge

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.9+-green.svg)
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![GitHub: valorisa](https://img.shields.io/badge/GitHub-valorisa--black?logo=github)

**Super-Directional-md-qd-Bridge** est un convertisseur bidirectionnel complet et robuste entre les fichiers **Markdown standard (.md)** et le format **Quarkdown (.qd)**. Ce projet répond au besoin croissant de faire cohabiter l'écosystème Markdown classique avec Quarkdown, un système de typographie moderne et Turing-complet basé sur Markdown.

## Table des matières

- [Super-Directional-md-qd-Bridge](#Super-Directional-md-qd-Bridge)
  - [Table des matières](#table-des-matières)
  - [Introduction](#introduction)
  - [Pourquoi ce projet ?](#pourquoi-ce-projet-)
  - [Fonctionnalités](#fonctionnalités)
  - [Architecture du projet](#architecture-du-projet)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
    - [Installation via Git](#installation-via-git)
    - [Configuration de l'environnement virtuel](#configuration-de-lenvironnement-virtuel)
    - [Dépendances](#dépendances)
  - [Utilisation](#utilisation)
    - [Conversion Markdown vers Quarkdown (.md → .qd)](#conversion-markdown-vers-quarkdown-md--qd)
    - [Conversion Quarkdown vers Markdown (.qd → .md)](#conversion-quarkdown-vers-markdown-qd--md)
    - [Conversion par lot (Batch)](#conversion-par-lot-batch)
    - [Options avancées](#options-avancées)
  - [Format des fichiers](#format-des-fichiers)
    - [Markdown standard](#markdown-standard)
    - [Quarkdown (.qd)](#quarkdown-qd)
    - [Mappage des éléments](#mappage-des-éléments)
  - [Gestion des extensions Pandoc](#gestion-des-extensions-pandoc)
  - [Gestion du Front-Matter](#gestion-du-front-matter)
  - [Exemples concrets](#exemples-concrets)
    - [Exemple 1 : Conversion simple](#exemple-1--conversion-simple)
    - [Exemple 2 : Gestion du Front-Matter](#exemple-2--gestion-du-front-matter)
    - [Exemple 3 : Blocs personnalisés](#exemple-3--blocs-personnalisés)
  - [Intégration CI/CD](#intégration-cicd)
    - [GitHub Actions](#github-actions)
  - [Tests](#tests)
  - [Contribution](#contribution)
  - [Roadmap](#roadmap)
  - [Licence](#licence)
  - [Remerciements](#remerciements)
  - [Contact](#contact)

## Introduction

Quarkdown, développé par [iamgio](https://github.com/iamgio/quarkdown), représente une évolution majeure du langage Markdown traditionnel. En transformant Markdown en un véritable langage de programmation Turing-complet, Quarkdown permet l'utilisation de fonctions, variables, boucles et conditions directement dans le texte. Cependant, cette puissance introduit une rupture de compatibilité avec l'écosystème Markdown existant.

Le projet **Super-Directional-md-qd-Bridge** se positionne comme la solution de pont technologique permettant une transition fluide entre ces deux mondes. Que vous souhaitiez migrer vos documents Markdown existants vers Quarkdown pour profiter de ses capacités de typographie avancée, ou inversement exporter vos documents Quarkdown vers un format Markdown standard pour une publication sur des plateformes comme GitHub ou GitLab, cet outil répond à vos besoins.

## Pourquoi ce projet ?

Le format Markdown classique, bien que universellement adopté, présente des limitations lorsqu'il s'agit de générer des documents complexes (livres, présentations, sites web). Des outils comme Pandoc excellent dans la conversion multi-format, mais ajoutent une couche de complexité supplémentaire.

Quarkdown simplifie ce workflow en intégrant nativement l'export vers HTML, PDF (via Puppeteer) et les slides. Cependant, son format natif `.qd` diffère légèrement du Markdown standard sur certains points (gestion des métadonnées, blocs personnalisés, syntaxe des fonctions).

**Super-Directional-md-qd-Bridge** résout ce problème en :

1.  **Automatisant la migration** : Convertit les fichiers `.md` existants en `.qd` en nettoyant le front-matter et en adaptant la syntaxe.
2.  **Préservant la compatibilité** : Convertit les fichiers `.qd` en `.md` pour une lecture sur les plateformes ne supportant pas Quarkdown.
3.  **Gérant les spécificités** : Traite les extensions Pandoc, les blocs HTML imbriqués et les métadonnées YAML.

## Fonctionnalités

-   **Conversion bidirectionnelle** : `.md` vers `.qd` et `.qd` vers `.md`.
-   **Gestion intelligente du Front-Matter** : Extraction, transformation et réinjection des métadonnées YAML.
-   **Compatibilité Pandoc** : Remplacement ou adaptation des extensions spécifiques à Pandoc (notes de bas de page, blocs personnalisés `:::`).
-   **Préservation de la syntaxe standard** : Les éléments Markdown standards (titres, listes, liens, images) restent inchangés.
-   **Interface en ligne de commande (CLI)** : Facile à intégrer dans des scripts PowerShell ou des pipelines CI/CD.
-   **Traitement par lot (Batch)** : Conversion récursive de dossiers entiers.
-   **Verbosité configurable** : Modes silencieux ou verbeux pour le débogage.

## Architecture du projet

```text
Super-Directional-md-qd-Bridge/
├── README.md                 # Ce fichier
├── LICENSE                   # Licence MIT
├── requirements.txt          # Dépendances Python
├── setup.py                  # Configuration du package
├── md_qd_bridge/
│   ├── __init__.py
│   ├── cli.py                # Interface ligne de commande
│   ├── converter.py          # Logique de conversion core
│   ├── md_to_qd.py           # Spécifique .md -> .qd
│   ├── qd_to_md.py           # Spécifique .qd -> .md
│   └── utils.py              # Fonctions utilitaires
├── tests/
│   ├── test_converter.py
│   ├── samples_md/           # Fichiers .md d'exemple
│   └── samples_qd/           # Fichiers .qd d'exemple
└── .github/
    └── workflows/
        └── ci.yml            # Workflow GitHub Actions
```

## Prérequis

-   **Python** : Version 3.9 ou supérieure.
-   **PowerShell** : Version 7.6.1 ou supérieure (pour l'exécution sous Windows).
-   **Pip** : Gestionnaire de paquets Python.

## Installation

### Installation via Git

Clonez le dépôt sur votre machine locale :

```bash
git clone https://github.com/valorisa/Super-Directional-md-qd-Bridge.git
cd Super-Directional-md-qd-Bridge
```

### Configuration de l'environnement virtuel

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances :

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Sous Windows PowerShell
# source venv/bin/activate   # Sous Linux/macOS
```

### Dépendances

Installez les paquets requis listés dans `requirements.txt` :

```bash
pip install -r requirements.txt
```

Contenu type de `requirements.txt` :

```text
mistletoe>=1.0.0
python-frontmatter>=1.1.0
PyYAML>=6.0
click>=8.0.0
```

## Utilisation

Le script principal `cli.py` offre une interface intuitive pour effectuer les conversions.

### Conversion Markdown vers Quarkdown (.md → .qd)

Pour convertir un fichier Markdown standard en format Quarkdown :

```bash
python -m md_qd_bridge.cli convert-md-to-qd --input "C:\Users\bbrod\Documents\article.md" --output "C:\Users\bbrod\Documents\article.qd"
```

**Options spécifiques :**

-   `--strip-pandoc` : Supprime agressivement les extensions Pandoc non supportées.
-   `--keep-html` : Conserve les balises HTML intactes (par défaut, tentative d'adaptation).

### Conversion Quarkdown vers Markdown (.qd → .md)

Pour convertir un fichier Quarkdown en Markdown standard :

```bash
python -m md_qd_bridge.cli convert-qd-to-md --input "C:\Users\bbrod\Documents\presentation.qd" --output "C:\Users\bbrod\Documents\presentation.md"
```

**Options spécifiques :**

-   `--simplify` : Transforme les fonctions Quarkdown complexes en éléments Markdown simples (peut entraîner une perte de dynamisme).

### Conversion par lot (Batch)

Pour convertir tous les fichiers d'un répertoire :

```bash
python -m md_qd_bridge.cli batch-convert --source "C:\Users\bbrod\Projets\docs-md" --dest "C:\Users\bbrod\Projets\docs-qd" --direction md-to-qd
```

### Options avancées

| Option | Description |
|--------|-------------|
| `--verbose` | Affiche les détails du processus de conversion. |
| `--dry-run` | Simule la conversion sans écrire de fichiers. |
| `--recursive` | Parcourt les sous-dossiers lors d'une conversion par lot. |

## Format des fichiers

### Markdown standard

Le Markdown standard repose sur une syntaxe minimaliste :

```markdown
# Titre principal

Ceci est un paragraphe avec **du gras** et *de l'italique*.

- Liste à puces
- Élément 2

[Un lien](https://example.com)
```

### Quarkdown (.qd)

Quarkdown étend cette syntaxe avec des directives de document et des fonctions logiques :

```markdown
.doctype {paged}
.title {Mon Document Quarkdown}

# Titre principal

Ceci est un paragraphe généré dynamiquement.

.loop {i in 1..3}
  Itération {i}
.endloop
```

### Mappage des éléments

| Élément Markdown | Élément Quarkdown | Note de conversion |
|------------------|-------------------|--------------------|
| `---` (Front-Matter) | Directives `.key {value}` | Le YAML est parsé et transformé en directives Quarkdown. |
| `^[note]` | `.footnote{note}` | Adaptation des notes de bas de page Pandoc. |
| `::: {.class} ...` | `<div class="..."> ...` | Les blocs spéciaux sont transformés en divs compatibles. |

## Gestion des extensions Pandoc

Pandoc introduit des syntaxes qui ne sont pas nativement comprises par Quarkdown. Le convertisseur applique les règles suivantes :

1.  **Blocs personnalisés** : `::: {.class}` est converti en syntaxe de module Quarkdown ou en `<div>`.
2.  **Notes de bas de page** : Les notes inline `^[...]` sont extraites et listées, ou converties au format Quarkdown.
3.  **Inclusions** : Les commandes d'inclusion spécifiques sont commentées ou remplacées par les équivalents Quarkdown `.include`.

## Gestion du Front-Matter

Le Front-Matter YAML (utilisé par Jekyll, Hugo, etc.) est traité comme suit lors d'une conversion `.md` vers `.qd` :

-   **Extraction** : Le bloc `---` est retiré du corps du texte.
-   **Filtrage** : Seules les clés `title`, `lang`, `author`, `tags` sont conservées par défaut.
-   **Transformation** : Chaque ligne est convertie en directive Quarkdown `.key {value}`.

Exemple de transformation :

**Markdown (Entrée)**

```yaml
---
title: Mon super article
lang: fr
date: 2026-04-28
---
```

**Quarkdown (Sortie)**

```markdown
.title {Mon super article}
.lang {fr}
```

## Exemples concrets

### Exemple 1 : Conversion simple

Fichier `input.md` :

```markdown
# Bonjour le monde

Ceci est un test de **conversion**.
```

Commande :

```bash
python -m md_qd_bridge.cli convert-md-to-qd -i input.md -o output.qd
```

Résultat `output.qd` :

```markdown
# Bonjour le monde

Ceci est un test de **conversion**.
```

### Exemple 2 : Gestion du Front-Matter

Fichier `blog.md` :

```markdown
---
title: Voyage au Japon
author: valorisa
layout: post
---

## Introduction

Ceci est un récit de voyage.
```

Résultat après conversion :

```markdown
.title {Voyage au Japon}
.author {valorisa}

## Introduction

Ceci est un récit de voyage.
```

### Exemple 3 : Blocs personnalisés

Fichier `docs.md` avec bloc Pandoc :

```markdown
::: {.warning}
Attention, ceci est un avertissement important.
:::
```

Résultat `docs.qd` :

```markdown
<div class="warning">
Attention, ceci est un avertissement important.
</div>
```

## Intégration CI/CD

### GitHub Actions

Vous pouvez automatiser la conversion de vos documents lors de chaque push sur la branche `main`.

Fichier `.github/workflows/convert.yml` :

```yaml
name: Convert MD to QD

on:
  push:
    branches: [ main ]
    paths:
      - 'docs/**.md'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run conversion
        run: python -m md_qd_bridge.cli batch-convert --source docs --dest qd-docs --direction md-to-qd --recursive
      - name: Commit changes
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: "Auto-convert MD to QD"
```

## Tests

Pour lancer la suite de tests (à venir) :

```bash
pytest tests/
```

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer :

1.  Forkez le projet.
2.  Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-super-feature`).
3.  Commitez vos changements (`git commit -m 'Ajout de ma super feature'`).
4.  Pushez vers la branche (`git push origin feature/ma-super-feature`).
5.  Ouvrez une Pull Request.

## Roadmap

-   [x] Conversion de base `.md` vers `.qd`.
-   [x] Gestion du Front-Matter YAML.
-   [ ] Conversion inverse `.qd` vers `.md`.
-   [ ] Support des fonctions logiques Quarkdown dans la conversion inverse.
-   [ ] Interface graphique (GUI) basée sur Tkinter.
-   [ ] Support des thèmes de conversion personnalisables.

## Licence

Ce projet est distribué sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

-   **iamgio** pour le développement de [Quarkdown](https://github.com/iamgio/quarkdown), un outil révolutionnaire pour la typographie moderne.
-   La communauté **Pandoc** pour avoir défini des standards de conversion de documents.
-   Tous les contributeurs qui aident à améliorer ce pont technologique.

## Contact

-   **Auteur** : valorisa
-   **GitHub** : [https://github.com/valorisa](https://github.com/valorisa)
-   **Projet** : [https://github.com/valorisa/Super-Directional-md-qd-Bridge](https://github.com/valorisa/Super-Directional-md-qd-Bridge)

---

*README généré le 28 avril 2026. Mis à jour régulièrement.*
