from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    url: str
    words: int

class SummaryOut(BaseModel):
    id: int
    url: str
    summary: str

    class Config:
        orm_mode = True
