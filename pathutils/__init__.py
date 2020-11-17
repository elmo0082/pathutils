from .get_dir_paths import *
from .various import *

# Add source dirs to python path:
import sys
sys.path += get_list_source_dirs()
