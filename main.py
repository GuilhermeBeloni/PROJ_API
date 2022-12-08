from fastapi import FastAPI, status, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


#objeto
class Cliente(BaseModel):
    id: Optional[int] 
    nome: str
    email: str
    telefone: str
    dataNasc: str
    vip: Optional[str]


#bd-local

db_cliente = [
    Cliente(id=1, nome='José Antônio', email='zeantonio@gmai.com', telefone='1796532184', dataNasc='27/10/1996', vip='S'),
    Cliente(id=2, nome='José Lopes', email='lopesze@gmai.com', telefone='1845488165', dataNasc='01/03/1998', vip='S'),
    Cliente(id=3, nome='Roberto Neves', email='betoneves@gmai.com', telefone='4822146528', dataNasc='16/12/78', vip='S'),
    Cliente(id=4, nome='Maria Victória', email='vicmaria@gmai.com', telefone='4321579524', dataNasc='31/07/2001', vip='N'),
    Cliente(id=5, nome='Luana Almeida', email='luaalmeida@gmai.com', telefone='1966321547', dataNasc='12/08/1993', vip='N'),
    Cliente(id=6, nome='Lucas Sterblich', email='lucbitch@gmai.com', telefone='17554213658', dataNasc='02/06/1963', vip='N'),
    Cliente(id=7, nome='jonathan Lima', email='jowlima@gmai.com', telefone='1711451845', dataNasc='27/10/1996', vip='N'),
    Cliente(id=8, nome='Clodoaldo Campos', email='clodo123@gmai.com', telefone='1899654213', dataNasc='14/10/1998', vip='N'),
    Cliente(id=9, nome='Suellen Toffano', email='sulla321@gmai.com', telefone='11482146325', dataNasc='05/02/1987', vip='N')
]


#rotas
@app.get('/')
async def home():
    return {'Mensagem': 'Api de cadastro de atendimento.'}


@app.get('/cliente')
async def exibir_clientes():
    if db_cliente:
        return {'Cliente': db_cliente}
    else:
        return{'Mensagen': 'VAZIO!'}




@app.get('/cliente/{id}')
async def mostrar_cliente(id: int):
    clientes = {'Cliente': [cliente for cliente in db_cliente if cliente.id==id]}
    if id < 9 : 
        return clientes
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Não existe clientes nesta posição!')
        


@app.post('/cliente', status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente: Cliente):
    cliente.id = db_cliente[-1].id + 1
    db_cliente.append(cliente)
    return {'Mensagem': 'Cliente criado!'}




@app.delete('/cliente/{id}')
async def apagar_cliente(id: int):
    cliente = [cliente for cliente in db_cliente if cliente.id == id]  
    db_cliente.remove(cliente[0])
    return {'Mensagem': 'Cliente excluído!'}   
    
         
'''uvicorn main:app --reload'''

