from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class Property(BaseModel):
    """
    Pydantic model for a property.
    """
    url: HttpUrl
    location: str
    price: Optional[float] = None
    rooms: Optional[float] = None
    livable_area: Optional[float] = None
    total_area: Optional[float] = None
    date_found: datetime
    car_parking: Optional[bool] = None
    garage: Optional[bool] = None
    swimming_pool: Optional[bool] = None
    description: Optional[str] = None # To be passed to the LLM
    html_path: Optional[str] = None
    markdown_path: Optional[str] = None

    class Config:
        from_attributes = True
