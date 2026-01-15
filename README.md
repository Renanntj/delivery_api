# 🚀 Delivery API — FastAPI

**Delivery API** é uma API RESTful construída com **FastAPI** para gerenciar um sistema básico de pedidos no contexto de delivery — incluindo cadastro de usuários, autenticação e operações relacionadas a pedidos.  

O projeto foi desenvolvido com foco em **organização, boas práticas e evolução contínua**, servindo tanto como backend funcional quanto como base de estudos.

> 🔄 Este projeto está em **desenvolvimento ativo** e **sujeito a atualizações e melhorias**.

---

## 🚀 Deploy

Esta API está publicada na plataforma Render para fins educacionais e de portfólio.

Base URL:
https://delivery-api-vwyp.onrender.com

Documentação Swagger:
https://delivery-api-vwyp.onrender.com/docs


## 🔍 Visão Geral

A API oferece recursos para:

- gerenciamento de usuários  
- autenticação  
- cadastro e controle de pedidos  
- atualização de status  
- consultas por ID ou listagem geral  

Ela segue os princípios de uma **API REST**, utilizando:

- rotas bem definidas  
- padrões HTTP (GET, POST, PUT, DELETE)  
- respostas estruturadas em JSON  
- validação via **Pydantic Schemas**

---

## 🧱 Tecnologias Utilizadas

- Python
- **FastAPI**
- Uvicorn
- Pydantic
- SQLite (banco `banco.db`)
- Alembic (migrações, se aplicável)

---

## 📡 Endpoints Principais

### 🔐 Autenticação

| Método | Endpoint   | Descrição |
|--------|-----------|----------|
| POST   | `/login`   | Autentica o usuário |
| POST   | `/criar_conta`| Realiza cadastro de usuário |

---

## 📚 Documentação Interativa

A documentação REST é gerada automaticamente pelo FastAPI.

Após iniciar o servidor, acesse:

- `/docs` → Swagger UI  
---

## 📂 Estrutura do Projeto

```
delivery_api/
├── alembic/
├── alembic.ini
├── auth_routes.py
├── dependences.py
├── main.py
├── models.py
├── order_routes.py
├── schemas.py
├── requirements.txt
└── banco.db
```

---

## ▶️ Como Executar o Projeto

1️⃣ Clone o repositório  
```
git clone https://github.com/Renanntj/delivery_api
```

2️⃣ Acesse o diretório  
```
cd delivery_api
```

3️⃣ Crie ambiente virtual  
```
python -m venv venv
```

4️⃣ Ative o ambiente virtual  

Linux/Mac:
```
source venv/bin/activate
```

Windows:
```
venv\Scripts\activate
```

5️⃣ Instale as dependências  
```
pip install -r requirements.txt
```

6️⃣ Execute o servidor  
```
uvicorn main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

---

---

## 📌 Status do Projeto

🟢 Funcional  
🟡 Em evolução contínua  
🔧 Recebendo melhorias e novas features

---

## 🤝 Contribuições

Sinta-se à vontade para:

- abrir issues  
- sugerir melhorias  
- criar pull requests  

---

## 📄 Licença

Licença **MIT** (ou ajuste conforme sua preferência).
