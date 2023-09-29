from typing import Dict

from pydantic import BaseModel, root_validator


class BaseResponse(BaseModel):
    """Represents a base logic for response."""

    @root_validator(pre=True)
    def parse_main_data_from_response(cls, values: Dict) -> Dict:
        data = values.get('_embedded')
        if data is not None:
            values.pop('_embedded')
            merged_dict = {**data, **values}
            return merged_dict
        return values
