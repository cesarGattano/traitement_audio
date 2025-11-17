# 🎵 Traitement Audio

Un projet Python pour mélanger et traiter des fichiers audio. Ce projet permet de charger plusieurs pistes audio (voix, ambiance, bruits de pas), d'ajuster leur volume, d'ajouter des effets (fade in), et de les combiner en une seule piste finale exportée au format MP3.

## 📋 Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Architecture du projet](#architecture-du-projet)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Modules](#modules)
- [Licence](#licence)

## ✨ Fonctionnalités

- **Chargement d'audio** : Importation de fichiers MP3 à partir d'un répertoire
- **Ajustement de volume** : Modification du volume des pistes en décibels
- **Effets audio** : Application de fade-in aux pistes
- **Mixage multi-piste** : Superposition et fusion de plusieurs fichiers audio
- **Export** : Sauvegarde du résultat final en MP3
- **Configuration YAML** : Gestion facile des chemins et paramètres via fichier de configuration

## 🏗️ Architecture du projet

```
traitement_audio/
├── config.yaml              # Configuration des chemins et paramètres audio
├── main.py                  # Point d'entrée principal
├── requirements.txt         # Dépendances Python
├── README.md               # Ce fichier
├── LICENSE                 # Licence du projet
├── data/
│   ├── raw/               # Fichiers audio bruts (entrée)
│   └── export/            # Fichiers audio exportés (sortie)
└── scripts/
    ├── load_export.py     # Fonctions de chargement et export audio
    └── transform.py       # Fonctions de transformation audio
```

## 📦 Installation

### Prérequis
- Python 3.7+
- pip

### Étapes d'installation

1. Clonez le repository :
```bash
git clone <url-du-repository>
cd traitement_audio
```

2. Créez un environnement virtuel (optionnel mais recommandé) :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Modifiez le fichier `config.yaml` pour configurer votre projet :

```yaml
path:
  raw: "data/raw"          # Dossier contenant les fichiers audio source
  export: "data/export"    # Dossier de destination pour l'export

sounds:
  voice:
    name: "voice"          # Nom du fichier (sans extension)
    format: "mp3"          # Format du fichier
    volume: 10             # Ajustement de volume en dB

  ambiance:
    name: "ambiance"
    format: "mp3"
    volume: -20

  walking:
    name: "monster-footsteps-on-gravel"
    format: "mp3"
    volume: -5
    fade_in: 0             # Durée du fade in en ms (optionnel)
```

**Notes sur la configuration :**
- Les ajustements de volume sont en décibels (dB). Positif = plus fort, négatif = plus faible
- Le paramètre `name` correspond au nom du fichier **sans extension**
- Les fichiers audio doivent être placés dans le dossier `data/raw/`

## 🚀 Utilisation

1. Placez vos fichiers audio dans le dossier `data/raw/` :
   ```
   data/raw/
   ├── voice.mp3
   ├── ambiance.mp3
   └── monster-footsteps-on-gravel.mp3
   ```

2. Ajustez la configuration dans `config.yaml` selon vos besoins

3. Exécutez le script principal :
   ```bash
   python main.py
   ```

4. Le fichier mixé sera généré dans `data/export/final_mix.mp3`

## 🔧 Modules

### `scripts/load_export.py`
Gère le chargement et l'export des fichiers audio.

**Fonctions principales :**
- `load_sound(config, name, format)` : Charge un fichier audio
- `load_voice(config)` : Charge la piste vocale
- `load_ambiance(config)` : Charge l'ambiance
- `load_walking(config)` : Charge les bruits de pas
- `export_sound(sound, config, name, format)` : Exporte le résultat final

### `scripts/transform.py`
Applique des transformations et effets aux fichiers audio.

**Fonctions principales :**
- `volume(audio, db_adjustment)` : Ajuste le volume en dB
- `fade_in(audio, duration)` : Applique un effet de montée en volume (fade-in)
- `overlap_sound(base, sounds)` : Superpose plusieurs pistes sur une piste de base

## 📚 Dépendances

- **pydub** (0.25.1) : Manipulation et traitement audio
- **PyYAML** (6.0.3) : Parsing des fichiers YAML
- **simpleaudio** (1.0.4) : Lecture audio
- **setuptools** (80.9.0) : Outils de distribution Python

## 📝 Licence

Ce projet est sous licence [voir LICENSE](./LICENSE)
