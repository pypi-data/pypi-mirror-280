from pathlib import Path
import sys
import os

packagePath = Path(__file__).resolve()
# sys.path.append(f"{os.path.dirname(packagePath.parent)}")
sys.path.append(f"{os.path.dirname(packagePath)}")
