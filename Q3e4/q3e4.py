from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

contador_id = 4
alunos_df = pd.DataFrame(
    {
        "id": [1,2,3],
        "nome": ["Roberto", "Eduardo", "Evynne"],
        "curso": ["ES", "ES", "ES"],
        "IRA": [5.7, 6.3, 7.3]
    }
)

class Aluno(BaseModel):
    nome: str
    curso: str
    IRA: float

@app.post("/alunos")
def criar_aluno(aluno: Aluno):
    
    global alunos_df, contador_id
    
    novo_aluno = {
        "id": contador_id,
        "nome": aluno.nome,
        "curso": aluno.curso,
        "IRA": aluno.IRA
    }
    
    alunos_df = alunos_df._append(novo_aluno, ignore_index = True)
    contador_id = contador_id + 1
    return {
        "mensagem": "Aluno criado com sucesso!",
        "aluno": novo_aluno
    }

@app.get("/alunos")
def listar_alunos():
    return alunos_df.to_dict(orient = "records")