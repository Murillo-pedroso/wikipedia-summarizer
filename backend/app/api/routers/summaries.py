from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas import SummarizeRequest, SummaryOut
from app.models import Summary
from app.db import SessionLocal, engine
from app.services import create_summary, list_summaries

# garanta que as tabelas existam
Summary.metadata.create_all(bind=engine)

router = APIRouter(prefix="/summaries", tags=["summaries"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SummaryOut)
def post_summary(req: SummarizeRequest, db: Session = Depends(get_db)):
    return create_summary(req.url, db , req.words)

@router.get("/", response_model=List[SummaryOut])
def get_summaries(db: Session = Depends(get_db)):
    return list_summaries(db)
