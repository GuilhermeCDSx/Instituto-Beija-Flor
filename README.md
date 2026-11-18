# Instituto Beija-Flor (IBF) - Sistema de Gestão de Frequência e Estoque

Repositório oficial do Minimum Viable Product (MVP) desenvolvido para o Instituto Beija-Flor, instituição sem fins lucrativos localizada no bairro Guaraituba, em Colombo, Paraná. O sistema substitui o controle em papel por uma aplicação web responsiva (PWA) voltada à gestão de frequência diária, sinalização de restrições alimentares e controle de estoque por data de validade.

## Sobre o Projeto

O projeto foi estruturado para atender às demandas operacionais do instituto, garantindo agilidade no pátio para os educadores sociais, segurança alimentar para a cozinha e controle gerencial para a coordenação, fundamentando-se nos Objetivos de Desenvolvimento Sustentável (ODS 2 - Fome Zero e Agricultura Sustentável).

### Principais Funcionalidades (RF)
- RF01 - Gestão de Assistidos: Cadastro e consulta de crianças e adolescentes com sinalização de restrições alimentares e alergias.
- RF02 - Chamada Diária por Turno: Registro móvel de presença e ausência com suporte a cache local (PWA) para funcionamento em caso de oscilação de rede.
- RF03 - Painel da Cozinha: Cálculo automático do total de refeições diárias e listagem nominal de dietas especiais para o turno ativo.
- RF04 - Gestão de Estoque: Controle de lotes de alimentos com ordenação por data de validade mais próxima e registro de baixa de consumo.

## Tecnologias Utilizadas

O sistema foi desenvolvido adotando uma Arquitetura Monolítica em Camadas, garantindo simplicidade de manutenção e implantação individual:
- Backend: Python 3.12 com FastAPI 0.115
- Persistência e ORM: PostgreSQL 16 (hospedado no Supabase) com SQLAlchemy 2.0
- Validação: Pydantic 2.8
- Frontend / PWA: HTML5, Bootstrap 5.3 e Service Worker API
- Testes: Pytest 8.3

## Estrutura do Repositório

instituto-beija-flor/
├── main.py            # Inicialização da API, rotas e montagem do PWA
├── database.py        # Configuração da conexão com o PostgreSQL
├── models.py          # Definição das entidades (usuarios, assistidos, presencas, estoque)
├── schemas.py         # Schemas de validação de dados com Pydantic
├── requirements.txt   # Dependências fixadas do projeto Python
└── static/
    └── index.html     # Interface front-end da aplicação

## Como Executar o Projeto Localmente

1. Clone o repositório:
   git clone https://github.com/GuilhermeCDSx/Instituto-Beija-Flor.git
   cd Instituto-Beija-Flor

2. Crie e ative um ambiente virtual:
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Configure as variáveis de ambiente:
   Crie um arquivo .env na raiz informando a URL de conexão do seu banco PostgreSQL:
   DATABASE_URL=postgresql://usuario:senha@localhost:5432/ibf_db

5. Inicie o servidor de desenvolvimento:
   uvicorn main:app --reload

6. Acesse no navegador:
   Abra http://127.0.0.1:8000 para visualizar a aplicação.

## Segurança e Conformidade
- Autenticação segura por perfil com hash de senhas (Argon2id).
- Mitigação de vulnerabilidades alinhada ao OWASP Top 10 (proteção contra SQL Injection e XSS).
- Acessibilidade da interface em conformidade com as diretrizes WCAG 2.1 AA (contraste, áreas de toque mínimas e alertas redundantes por texto, símbolo e cor).

- ## Contribuição
Este repositório é exclusivo para fins acadêmicos.
