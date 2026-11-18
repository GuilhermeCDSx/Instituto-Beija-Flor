from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

# Cria as tabelas no banco automaticamente para testes locais
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Instituto Beija-Flor API", version="1.0.0")

# Monta os arquivos estáticos (PWA front-end)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "API do Instituto Beija-Flor em funcionamento online."}

@app.post("/assistidos/", response_model=dict)
def criar_assistido(assistido: schemas.AssistidoCreate, db: Session = Depends(get_db)):
    novo_assistido = models.Assistido(**assistido.model_dump())
    db.add(novo_assistido)
    db.commit()
    db.refresh(novo_assistido)
    return {"status": "sucesso", "id_assistido": novo_assistido.id_assistido}

@app.post("/presencas/", response_model=dict)
def registrar_presenca(presenca: schemas.PresencaCreate, db: Session = Depends(get_db)):
    nova_presenca = models.PresencaTurno(**presenca.model_dump())
    db.add(nova_presenca)
    db.commit()
    db.refresh(nova_presenca)
    return {"status": "sucesso", "id_presenca": nova_presenca.id_presenca}

@app.get("/cozinha/painel/{data}/{turno}")
def painel_cozinha(data: str, turno: str, db: Session = Depends(get_db)):
    # Retorna o total de presentes e lista de restrições alimentares do turno
    presentes = db.query(models.PresencaTurno).filter_by(data_chamada=data, turno=turno, status_presenca="presente").all()
    ids_presentes = [p.id_assistido for p in presentes]
    
    assistidos_presentes = db.query(models.Assistido).filter(models.Assistido.id_assistido.in_(ids_presentes)).all()
    
    restricoes = [
        {"nome": a.nome_completo, "restricao": a.descricao_restricao} 
        for a in assistidos_presentes if a.possui_restricao_alimentar
    ]
    
    return {
        "turno": turno,
        "data": data,
        "total_refeicoes": len(assistidos_presentes),
        "dietas_especiais": restricoes
    }