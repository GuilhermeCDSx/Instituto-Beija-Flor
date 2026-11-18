from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, Numeric, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String(150), nullable=False)
    email_login = Column(String(150), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    perfil_acesso = Column(String(50), nullable=False) # educador, cozinha, coordenacao
    status_ativo = Column(Boolean, default=True, nullable=False)

class Assistido(Base):
    __tablename__ = "assistidos"
    id_assistido = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String(150), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    turno_padrao = Column(String(20), nullable=False) # manha, tarde
    nome_responsavel = Column(String(150), nullable=False)
    telefone_emergencia = Column(String(30), nullable=False)
    possui_restricao_alimentar = Column(Boolean, default=False, nullable=False)
    descricao_restricao = Column(String(255), nullable=True)
    status_matricula = Column(String(20), default="ativo", nullable=False)

class PresencaTurno(Base):
    __tablename__ = "presencas_turno"
    id_presenca = Column(Integer, primary_key=True, index=True)
    id_assistido = Column(Integer, ForeignKey("assistidos.id_assistido"), nullable=False)
    id_usuario_registro = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    data_chamada = Column(Date, nullable=False)
    turno = Column(String(20), nullable=False) # manha, tarde
    status_presenca = Column(String(20), nullable=False) # presente, ausente, justificado
    sincronizado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class ItemEstoque(Base):
    __tablename__ = "itens_estoque"
    id_item_estoque = Column(Integer, primary_key=True, index=True)
    nome_alimento = Column(String(150), nullable=False)
    categoria = Column(String(50), nullable=False) # perecivel, nao_perecivel, hortifruti
    quantidade_atual = Column(Numeric(10, 2), nullable=False)
    unidade_medida = Column(String(20), nullable=False) # kg, litro, unidade, pacote
    data_entrada = Column(Date, nullable=False)
    data_validade = Column(Date, nullable=False)
    origem_recurso = Column(String(50), nullable=False) # doacao, compra_edital
    id_usuario_atualizacao = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)