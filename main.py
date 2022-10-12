from fastapi import FastAPI, status, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class FilaCliente(BaseModel):
    id: Optional[int] = 0
    nome: str
    data: str




db_cliente = [
    FilaCliente(id=1, nome='José Antônio', data='21/07/2022'),
    FilaCliente(id=2, nome='José Lopes', data='23/07/2022'),
    FilaCliente(id=3, nome='Roberto Neves', data='26/07/2022'),
    FilaCliente(id=4, nome='Maria Victória', data='29/07/2022'),
    FilaCliente(id=5, nome='Luana Almeida', data='01/08/2022'),
    FilaCliente(id=6, nome='Lucas Sterblich', data='07/08/2022'),
    FilaCliente(id=7, nome='jonathan Lima', data='10/08/2022'),
    FilaCliente(id=8, nome='Clodoaldo Campos', data='11/08/2022'),
    FilaCliente(id=9, nome='Suellen Toffano', data='21/09/2022')
]

@app.get('/')
async def home():
    return {'Mensagem': 'Api de fila de atendimentos by Guilherme'}

@app.get('/fila')
async def exibir_clientes():
    if db_cliente:
        return {'cliente': db_cliente}
    else:
        return{'Mensagen': 'Fila Vazia!'}
            