"""Fonctions utilitaires pour la gestion des fichiers et le nettoyage."""

import re
from pathlib import Path


def read_file(file_path: Path) -> str:
    """Lit un fichier texte avec gestion d'erreur."""
    try:
        return file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")
    except Exception as e:
        raise IOError(f"Erreur de lecture {file_path}: {e}")


def write_file(file_path: Path, content: str) -> None:
    """Écrit le contenu dans un fichier."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")


def clean_whitespace(text: str) -> str:
    """Nettoie les espaces blancs superflus en fin de ligne."""
    return re.sub(r"[ \t]+\n", "\n", text)
