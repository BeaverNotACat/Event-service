from pydantic import BaseModel, ConfigDict


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
