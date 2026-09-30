# Backend — NutriElo

API do NutriElo em Python (framework a definir — FastAPI é a sugestão, mas a estrutura serve também para Flask).

## Estrutura

```
backend/
├── app/
│   ├── api/
│   │   └── routes/    # Endpoints (auth, usuarios, ongs, pontos_distribuicao...)
│   ├── core/          # Configurações, variáveis de ambiente, segurança
│   ├── db/            # Conexão com o banco / cliente do Supabase
│   ├── models/        # Modelos das tabelas do banco
│   ├── schemas/       # Validação de entrada/saída (ex.: Pydantic)
│   └── services/      # Regras de negócio
├── tests/             # Testes automatizados
└── requirements.txt   # Dependências Python
```

## Rodando localmente

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # preencha com as chaves do Supabase
```
