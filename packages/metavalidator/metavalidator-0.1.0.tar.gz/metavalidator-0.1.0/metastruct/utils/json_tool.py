import json
from typing import Dict, List, Union


class JSONTool:
    @staticmethod
    def from_raw(text: str) -> Union[Dict, List]:
        return json.loads(text)
