from kickbase_api.models.base_model import BaseModel
from typing import List
from datetime import datetime

class PlayerStats(BaseModel):
    market_value_change: int = None
    market_value_change_percent: float = None
    market_values = None

    def __init__(self, d: dict = {}):
        self._json_transform = {
        }
        self._json_mapping = {
            "marketValueChange": "market_value_change",
            "marketValueChangePercent": "market_value_change_percent",
            "marketValues": "market_values"
        }
        super().__init__(d)
