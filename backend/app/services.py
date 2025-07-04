from sqlalchemy.orm import Session
from app.models import Summary as SummaryModel
import requests
from bs4 import BeautifulSoup
import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def get_page_text(url: str, max_chars: int = 8000) -> str:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    text = " ".join(p.get_text() for p in soup.select("p"))
    return text[:max_chars]

def summarize_text(text: str, words:int) -> str:
    resp = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        messages=[     
            {
                "role": "user",
                "content": (
                    f"Resuma o texto abaixo em no máximo {words} palavras. "
                    f"Tente chegar o mais próximo possível de {words} palavras, sem ultrapassar esse número. "
                    f"Nunca use mais do que {words} palavras. "
                    f"Se ficar abaixo de {words}, tente chegar o mais perto possível do limite sem repetir frases. "
                    f"Texto para resumo:\n\n{text}"
                )
            }
        ]
    )
    summary = resp.choices[0].message.content
    return summary

def create_summary(url: str, db: Session, words:int):
    obj = db.query(SummaryModel).filter_by(url=url).first()
    if obj:
        return obj
    
    text = get_page_text(url)
    summary = summarize_text(text,words)
    
    new = SummaryModel(url=url, summary=f"sumário {summary}")
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def list_summaries(db: Session):
    return db.query(SummaryModel).all()
git config --global user.email "murillomonteirop@gmail.com"
git config --global user.name "oMurillo_"
