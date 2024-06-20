from typing import Union
import numpy as np
from dataclasses import dataclass, field
from pms_inference_engine.utility import create_uuid


@dataclass
class EngineIOData:
    frame_id: int
    frame: np.ndarray
    uuid: str = field(default_factory=lambda: create_uuid())
