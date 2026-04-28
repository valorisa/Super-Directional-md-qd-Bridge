"""Interface en ligne de commande (CLI) pour Super-Directional-md-qd-Bridge."""

import click
from pathlib import Path
from .md_to_qd import process_file as md_to_qd_process
from .qd_to_md import process_file as qd_to_md_process
from .utils import clean_whitespace


@click.group()
@click.version_option(version="0.1.0", prog_name="Super-Directional-md-qd-Bridge")
def main():
    """Convertisseur bidirectionnel entre Markdown (.md) et Quarkdown (.qd)."""
    pass


@main.command("md-to-qd")
@click.option("--input", "-i", required=True, type=Path, help="Fichier Markdown source (.md).")
@click.option("--output", "-o", required=True, type=Path, help="Fichier Quarkdown de destination (.qd).")
def md_to_qd_cmd(input, output):
    """Convertit un fichier Markdown vers Quarkdown."""
    if not input.exists():
        raise click.FileError(input, hint="Fichier source introuvable.")
    if input.suffix != ".md":
        click.echo(f"Attention : Le fichier source {input} n'a pas l'extension .md", err=True)

    click.echo(f"Conversion de {input} vers {output}...")
    md_to_qd_process(input, output)
    click.echo("[OK] Conversion .md -> .qd terminee.")


@main.command("qd-to-md")
@click.option("--input", "-i", required=True, type=Path, help="Fichier Quarkdown source (.qd).")
@click.option("--output", "-o", required=True, type=Path, help="Fichier Markdown de destination (.md).")
def qd_to_md_cmd(input, output):
    """Convertit un fichier Quarkdown vers Markdown."""
    if not input.exists():
        raise click.FileError(input, hint="Fichier source introuvable.")
    if input.suffix != ".qd":
        click.echo(f"Attention : Le fichier source {input} n'a pas l'extension .qd", err=True)

    click.echo(f"Conversion de {input} vers {output}...")
    qd_to_md_process(input, output)
    click.echo("[OK] Conversion .qd -> .md terminee.")


@main.command("batch")
@click.option("--source", "-s", required=True, type=Path, help="Dossier source.")
@click.option("--dest", "-d", required=True, type=Path, help="Dossier de destination.")
@click.option("--direction", type=click.Choice(["md-to-qd", "qd-to-md"], case_sensitive=False), required=True)
@click.option("--recursive", "-r", is_flag=True, help="Parcourt les sous-dossiers.")
def batch_cmd(source, dest, direction, recursive):
    """Convertit tous les fichiers d'un dossier."""
    if not source.exists():
        raise click.ClickException(f"Le dossier source {source} n'existe pas.")

    dest.mkdir(parents=True, exist_ok=True)

    pattern = "**/*.md" if direction == "md-to-qd" else "**/*.qd"
    files = source.glob(pattern) if recursive else source.glob(pattern.replace("**/", ""))

    count = 0
    for file_path in files:
        if direction == "md-to-qd":
            rel_path = file_path.relative_to(source)
            out_path = dest / rel_path.with_suffix(".qd")
            md_to_qd_process(file_path, out_path)
        else:
            rel_path = file_path.relative_to(source)
            out_path = dest / rel_path.with_suffix(".md")
            qd_to_md_process(file_path, out_path)
        count += 1
        click.echo(f"  Traité : {file_path.name}")

    click.echo(f"[OK] {count} fichier(s) converti(s).")


if __name__ == "__main__":
    main()
