"""Logique de conversion Quarkdown (.qd) vers Markdown (.md)."""

import re
from pathlib import Path


def convert_qd_to_md(qd_content: str) -> str:
    """
    Convertit le contenu Quarkdown en Markdown standard.
    - Transforme les directives .key {value} en Front-Matter YAML.
    - Remplace les balises spécifiques par du Markdown standard.
    """
    lines = qd_content.splitlines()
    yaml_lines = ["---"]
    body_lines = []
    in_yaml_block = False
    processed_directives = set()

    for line in lines:
        # Capture des directives Quarkdown (.key {value})
        directive_match = re.match(r"\.(\w+)\s*\{([^}]+)\}", line)
        if directive_match and not in_yaml_block:
            key = directive_match.group(1)
            value = directive_match.group(2).strip()
            if key not in processed_directives:
                # On ne met pas de guillemets sauf si nécessaire
                if " " in value or ":" in value:
                    yaml_lines.append(f'{key}: "{value}"')
                else:
                    yaml_lines.append(f"{key}: {value}")
                processed_directives.add(key)
        else:
            body_lines.append(line)

    # Assemblage du Front-Matter
    md_content = ""
    if len(yaml_lines) > 1:  # S'il y a des métadonnées
        yaml_lines.append("---")
        yaml_lines.append("")  # Ligne vide après le bloc YAML
        md_content = "\n".join(yaml_lines) + "\n".join(body_lines)
    else:
        md_content = "\n".join(body_lines)

    return md_content.strip() + "\n"


def process_file(input_path: Path, output_path: Path) -> None:
    """Traite un fichier unique .qd -> .md."""
    from .utils import read_file, write_file
    content = read_file(input_path)
    converted = convert_qd_to_md(content)
    write_file(output_path, converted)
