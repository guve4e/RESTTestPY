import os
import inspect
from pathlib import Path

"""
Configuration file
"""

# Root Directory
ROOT_DIR = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

# Source directory
SRC_DIR = Path(ROOT_DIR) / "src"

# Source directory
TEST_CASES_DIR = Path(ROOT_DIR) / "testcases"

