"""Tests unitaires pour le convertisseur Super-Directional-md-qd-Bridge."""

import pytest
from pathlib import Path
import sys
import os

# Ajout du dossier parent au path pour importer le package
sys.path.insert(0, str(Path(__file__).parent.parent))

from md_qd_bridge.md_to_qd import convert_md_to_qd
from md_qd_bridge.qd_to_md import convert_qd_to_md


class TestMdToQd:
    """Tests pour la conversion Markdown vers Quarkdown."""

    def test_simple_conversion(self):
        md_input = "# Titre\n\nCeci est un test."
        result = convert_md_to_qd(md_input)
        assert "# Titre" in result
        assert "Ceci est un test." in result

    def test_front_matter_conversion(self):
        md_input = "---\ntitle: Mon Titre\nlang: fr\n---\n\n# Contenu"
        result = convert_md_to_qd(md_input)
        assert ".title {Mon Titre}" in result
        assert ".lang {fr}" in result
        assert "---" not in result  # Le YAML doit être converti

    def test_pandoc_footnote_removal(self):
        md_input = "Un texte avec une note ^[Ceci est une note]."
        result = convert_md_to_qd(md_input)
        assert "<!-- Note: Ceci est une note -->" in result

    def test_pandoc_block_conversion(self):
        md_input = "::: {.warning}\nAttention !\n:::"
        result = convert_md_to_qd(md_input)
        assert '<div class="warning">' in result
        assert "</div>" in result


class TestQdToMd:
    """Tests pour la conversion Quarkdown vers Markdown."""

    def test_simple_reverse(self):
        qd_input = "# Titre\n\nContenu simple."
        result = convert_qd_to_md(qd_input)
        assert "# Titre" in result
        assert "Contenu simple." in result

    def test_directive_to_yaml(self):
        qd_input = ".title {Mon Titre}\n.lang {fr}\n\n# Body"
        result = convert_qd_to_md(qd_input)
        assert "---" in result
        assert "title:" in result
        assert "lang:" in result

    def test_no_directive_no_yaml(self):
        qd_input = "# Juste un titre\n\nParagraphe."
        result = convert_qd_to_md(qd_input)
        assert "---" not in result
