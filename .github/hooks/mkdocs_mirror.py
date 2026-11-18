from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
BACKUP = ROOT / ".mkdocs-docs-original"


def _restore_original_docs():
    if BACKUP.exists():
        if DOCS.exists():
            shutil.rmtree(DOCS)
        BACKUP.replace(DOCS)


def on_pre_build(config):
    _restore_original_docs()
    if DOCS.exists():
        shutil.move(str(DOCS), str(BACKUP))

    ignored_names = {
        ".git",
        ".github",
        ".vscode",
        "docs",
        "site",
        "node_modules",
        "__pycache__",
        ".mkdocs-docs-original",
    }

    DOCS.mkdir()
    for source in ROOT.iterdir():
        if source.name in ignored_names:
            continue
        destination = DOCS / source.name
        if source.is_dir():
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(source, destination)


def on_post_build(config):
    _restore_original_docs()
