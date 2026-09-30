# Frontend — NutriElo

Interface web do NutriElo (React ou Next.js — a definir).

## Estrutura

```
frontend/
├── public/            # Arquivos estáticos (favicon, imagens públicas)
└── src/
    ├── assets/        # Imagens, ícones e fontes importados pelo código
    ├── components/    # Componentes reutilizáveis (Button, Input, Card...)
    ├── pages/         # Telas da aplicação (Login, Cadastro, Home...)
    ├── hooks/         # Hooks customizados (useAuth, useFetch...)
    ├── services/      # Comunicação com a API do backend
    └── styles/        # Estilos globais e temas
```

## Como iniciar o projeto

Escolham uma das opções e rodem **dentro desta pasta** (`frontend/`):

```bash
# Next.js (usa src/app/ para as rotas no lugar de src/pages/)
npx create-next-app@latest . --src-dir

# React com Vite
npm create vite@latest . -- --template react
```

> O gerador pode reclamar que a pasta não está vazia; é só confirmar.
> As pastas acima são uma sugestão — ajustem conforme o framework escolhido.

O protótipo em HTML/JS da tela de login/cadastro está em [`docs/prototipos/login-cadastro`](../docs/prototipos/login-cadastro).
