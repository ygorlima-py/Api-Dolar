from app import service_req
from fastapi import FastAPI


app = FastAPI()

@app.get("/dolar")
def preco_dolar():
    resposta =  service_req.Requisicao().requisicao_dolar()
    print(resposta)
    return {"preco": resposta}




if __name__ == "__main__":
    preco_dolar()