"""Logique de conversion Markdown (.md) vers Quarkdown (.qd)."""

import re
from pathlib import Path
import frontmatter


def convert_md_to_qd(md_content: str) -> str:
    """
    Convertit le contenu Markdown en format Quarkdown.
    - Extrait le Front-Matter YAML.
    - Remplace les extensions Pandoc spécifiques.
    - Garde le Markdown standard intact.
    """
    # 1. Gestion du Front-Matter (YAML)
    try:
        post = frontmatter.loads(md_content)
        body = post.content
        yaml_meta = post.metadata
    except Exception:
        # Si le frontmatter échoue, on traite comme du texte brut
        body = md_content
        yaml_meta = {}

    # Transformation du Front-Matter en directives Quarkdown
    qd_header = ""
    if yaml_meta:
        # On ne garde que les clés standard compatibles Quarkdown
        allowed_keys = ["title", "lang", "author", "tags", "date"]
        for key, value in yaml_meta.items():
            if key in allowed_keys:
                if isinstance(value, list):
                    value_str = ", ".join(value)
                    qd_header += f".{key} {{{value_str}}}\n"
                else:
                    qd_header += f".{key} {{{value}}}\n"
        if qd_header:
            qd_header += "\n"

    # 2. Suppression/Réécriture des extensions Pandoc
    # a) Footnotes inline ^[...] -> Format Quarkdown (commentaire ou note)
    # Pour l'instant, on les laisse en commentaire HTML pour ne pas casser
    body = re.sub(
        r"\^\[([^\]]+)\]",
        r"<!-- Note: \1 -->",
        body
    )

    # b) Blocs Pandoc ::: {.class} ... ::: -> <div class="...">...</div>
    # Regex pour capturer le contenu entre :::
    def replace_pandoc_blocks(match):
        cls = match.group(1).strip() if match.group(1) else ""
        content = match.group(2).strip()
        return f'<div class="{cls}">\n{content}\n</div>'

    body = re.sub(
        r":::\s*\{([^}]+)\}\s*\n?(.*?):::",
        replace_pandoc_blocks,
        body,
        flags=re.DOTALL
    )

    # 3. Assemblage final
    qd_content = qd_header + body
    return qd_content.strip() + "\n"


def process_file(input_path: Path, output_path: Path) -> None:
    """Traite un fichier unique .md -> .qd."""
    from .utils import read_file, write_file
    content = read_file(input_path)
    converted = convert_md_to_qd(content)
    write_file(output_path, converted)
