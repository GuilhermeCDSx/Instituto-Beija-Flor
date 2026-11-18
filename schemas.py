from pydantic import BaseModel, EmailStr
from datetime import date

class AssistidoCreate(BaseModel):
    nome_completo: str
    data_nascimento: date
    turno_padrao: str
    nome_responsavel: str
    telefone_emergencia: str
    possui_restricao_alimentar: bool
    descricao_restricao: str | None = None

class PresencaCreate(BaseModel):
    id_assistido: int
    id_usuario_registro: int
    data_chamada: date
    turno: str
    status_presenca: str

class ItemEstoqueCreate(BaseModel):
    nome_alimento: str
    categoria: str
    quantidade_atual: float
    unidade_medida: str
    data_entrada: date
    data_validade: date
    origem_recurso: str
    id_usuario_atualizacao: int