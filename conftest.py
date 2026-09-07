import sys
from pathlib import Path

# Automatically add the project root to sys.path for pytest
sys.path.insert(0, str(Path(__file__).parent))