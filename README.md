# PROJ_API
Projeto de Api e Microsserviços (Toledo)

Para o desenvolvimento desta API você deve utilizar o framework FastAPI e contemplar os seguintes requisitos:

[1] Crie o endpoint GET /clientes

-Exibir os clientes cadastrados no sistema.

-Caso não exista nenhum cliente cadastrado o endpoint deve retornar um JSON vazio e o status 200.


[2] Crie o endpoint GET /cliente/:id

-Retornar os dados do cliente (id, nome, e-mail, telefone, data nascimento, vip e a data de cadastro) do ID pesquisado.

Se não tiver uma pessoa com o número do id da rota, deve ser retornado o status 404 e uma mensagem informativa no JSON de retorno.


[3] Crie o endpoint POST /cliente

-Adicionar um novo cliente no sistema, informando seu nome, e-mail, telefone, data nascimento e o sistema irá registrar a data e hora de seu cadastro.

-O campo nome é obrigatório e deve ter no máximo 20 caracteres.

-O campo "vip" só aceita 1 caractere (S ou N).


[4] Crie o endpoint PUT /cliente/:id

-Será atualizado os dados do cliente.

-Caso o cliente não seja localizado na posição especificada no id da rota deve ser retornado o status 404 e uma mensagem informativa no JSON de retorno.



[5] Crie o endpoint DELETE /cliente/:id

-Remove o cliente indicado no id.

-Caso o cliente não seja localizado na posição especificada no id da rota deve ser retornado o status 404 e uma mensagem informativa no JSON de retorno;


[6] Disponibilizar sua API na plataforma Deta Cloud (https://www.deta.sh/).


[7] Disponibilizar o código-fonte do projeto em um repositório público no Github.
