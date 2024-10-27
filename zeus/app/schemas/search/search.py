from pydantic import BaseModel


class SearchSchema(BaseModel):
    """
    :param
    """
    search_by: str
    q: str
