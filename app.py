import sys
import os
from pathlib import Path

# Ajouter le répertoire src au chemin de recherche
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from ui.streamlit_app import main

if __name__ == "__main__":
    main()
