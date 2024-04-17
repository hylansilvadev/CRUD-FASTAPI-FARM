from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Primeiro CRUD em FastAPI",
    docs_url="/"
)

class User(BaseModel):
    nome: str
    idade: int
    

database = []

# CREATE

@app.post(
    '/users',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False
)

def create_new_user(user: User):
    database.append(user)
    return user


# READ

@app.get(
    '/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False
    )

def get_all_users():
    return database


@app.get(
    '/users/{id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False
)

def get_user_by_id(id: int):
    if not id and id > 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Id de usário não permitido"
            )
        
    if not database[id]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario não foi encontrado"
            )
        
    return database[id]


# UPDATE

@app.put(
    '/users/{id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False
)

def update_user_by_id(id: int, user_data: User):
    if not id and id > 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Id de usário não permitido"
            )
        
    if not database[id]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario não foi encontrado"
            )
        
    database[id] = user_data
    
    return user_data


# DELETE

@app.delete(
    '/users/{id}',
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user_by_id(id: int):
    if not id and id > 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Id de usário não permitido"
            )
        
    if not database[id]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario não foi encontrado"
            )
        
    database.pop(id)
    