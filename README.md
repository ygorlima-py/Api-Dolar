"# API Dólar

Uma API simples para obter a cotação atual do dólar em relação ao real (USD/BRL).

## Endpoints

### GET /dolar

Retorna o preço atual do dólar em reais.

**Exemplo de resposta:**
```json
{
  "preco": 5.1234
}
```

## Tecnologias Utilizadas

- FastAPI
- Python 3.10+
- Requests

## Como executar localmente

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o servidor: `uvicorn main:app --reload`
4. Acesse a API em: `http://localhost:8000/dolar`

## Implantação

Esta API está configurada para implantação no Render." 
