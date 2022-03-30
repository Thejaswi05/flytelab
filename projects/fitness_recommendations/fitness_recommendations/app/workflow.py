import logging
import math
import os
import time
from io import StringIO
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, NamedTuple, Optional

import joblib
from markupsafe import string

from dataclasses_json import dataclass_json
from pathlib import Path
import pathlib
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
from download_dataset import download_fitness_dataset

logger = logging.getLogger(__file__)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

@dataclass_json
@dataclass
class Features:
    body_part: string
    equipment: string
    gif_url: string
    id: string
    name: string
    target: string

def map_fitness_data_to_features():
    dataset = download_fitness_dataset()

map_fitness_data_to_features()