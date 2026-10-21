import json
from pathlib import Path

def process_notebook(input_path: str, output_path: str = None):
    """
    Parcourt un notebook Jupyter, met à jour les métadonnées des cellules
    en fonction de leurs tags et supprime les cellules contenant le tag 'solution'.
    """
    input_file = Path(input_path)
    output_file = Path(output_path) if output_path else input_file

    with input_file.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    new_cells = []
    for cell in nb.get("cells", []):
        tags = cell.get("metadata", {}).get("tags", [])

        # 1. Supprimer la cellule si le tag "solution" est présent
        if "solution" in tags:
            continue

        # S'assurer que le dictionnaire metadata existe
        metadata = cell.setdefault("metadata", {})

        # 2. Règle pour le tag "enonce"
        if "enonce" in tags:
            metadata["deletable"] = False
            metadata["editable"] = False

        # 3. Règle pour le tag "a_completer"
        if "a_completer" in tags:
            metadata["deletable"] = False
            metadata["editable"] = True

        new_cells.append(cell)

    nb["cells"] = new_cells

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")

# --- Exemples d'utilisation ---

# 1. Traiter un fichier et remplacer le fichier d'origine :
# process_notebook("exercice.ipynb")

# 2. Traiter un fichier et sauvegarder sous un nouveau nom :
process_notebook("exos_arithmetique_3AM.ipynb",
                 "exos_arithmetique_3AM_eleve.ipynb")