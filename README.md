# 🏋️ API Fitness

API para registrar e acompanhar treinos, exercícios, refeições e avaliações físicas do usuário.

> 🚧 Projeto em desenvolvimento

## 🛠️ Tecnologias
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- JWT
- bcrypt (passlib)

## ✅ Funcionalidades
- Cadastro e login com senha criptografada e autenticação JWT
- Cada usuário acessa apenas os próprios dados
- CRUD de exercícios e treinos, com associação de exercícios a treinos
- Registro de execuções de exercícios, avulsas ou vinculadas a um treino
- Avaliações físicas com cálculo automático de IMC e recomendação por objetivo
- CRUD de refeições

## 🔜 Próximos passos
- Estimativa de calorias e macros das refeições com IA
- Sugestões de treino com IA
- Revisão de validações e tratamento de erros
- App mobile consumindo a API

## ▶️ Como rodar
1. Clone o repositório e entre na pasta do projeto
2. Crie e ative o ambiente virtual:
    python -m venv venv
    venv\Scripts\activate

3. Instale as dependências:
pip install -r requirements.txt

4. Copie o arquivo `.env.example` para `.env` e preencha a `SECRET_KEY`

5. Inicie o servidor:
uvicorn app.main:app --reload

6. Acesse a documentação das rotas em `http://localhost:8000/docs`

## 📚 O que aprendi
- (escreva aqui)
- (escreva aqui)
- (escreva aqui)