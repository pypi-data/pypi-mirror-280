from typing import List, Dict, Any, TypeVar, Generic
from pydantic import BaseModel
from .pandas import pd

DataClass = TypeVar("DataClass", bound=BaseModel)


class DataClassList(BaseModel, Generic[DataClass]):
    data: List[DataClass]
    default_key: Any = None

    def __init__(self, data: List[DataClass], **kwargs):
        super().__init__(data=data, **kwargs)
        if self.data:
            # 첫 번째 데이터 항목의 첫 번째 필드를 default_key로 설정
            self.default_key = list(self.data[0].model_fields.keys())[0]

    def __call__(self) -> List[DataClass]:
        return self.data

    def get_list_dict(self) -> List[Dict[str, Any]]:
        return [item.model_dump() for item in self.data]

    def get_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self.get_list_dict())

    @property
    def dict(self) -> Dict[Any, DataClass]:
        dictionary = {
            getattr(base_model, self.default_key): base_model
            for base_model in self.data
        }
        return dictionary

    def get_custom_dict(self, key) -> Dict[Any, DataClass]:
        dictionary = {getattr(base_model, key): base_model for base_model in self.data}
        return dictionary

    def get_value_list(self, key):
        list = [getattr(base_model, key) for base_model in self.data]
        return list
