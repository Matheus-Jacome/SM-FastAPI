from fastapi import FastAPI, HTTPException, Response

app = FastAPI()
users_list = [] 

@app.get("/users")
def get_all_users():
    if len(users_list) == 0:
        return Response(
            "No content",
         status_code=204
         )
    
    return users_list
    
@app.post("/users/{nome}")
def add_new_user(nome:str):
    users_list.append(nome)
    return Response(
        "Usuário adicionado com sucesso!",
        status_code=201
        )

@app.put("/users/{index}/{novo_nome}")
def update_user(index:int, novo_nome: str):
    if index < 0 or index >= len(users_list):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    users_list[index] = novo_nome
    return {"mensagem": "Usuário atualizado com sucesso", "usuarios":users_list}

@app.delete("/users/{index}/{novo_nome}")
def delete_user(index:int, novo_nome: str):
    if index < 0 or index >= len(users_list):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    removido = users_list.pop(index) 
    return{"mensagem": "Usuário removido com sucesso!", "usuario_removido": removido}



# @app.put("/users")
# def adicionar_usuario():
#     pass

# @app.delete("/users")
# def adicionar_usuario():
#     pass
 
