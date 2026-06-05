import json
import datetime

class task:
    #contrutor
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.datetime.now().isoformat()
        self.updatedAt = None
    
    def to_dict(self) -> str:
        return  {
            "id" : self.id,
            "description" : self.description,
            "status" : self.status,
            "createdAt" : self.createdAt,
            "updatedAt" : self.updatedAt
        }
        

def add(new_task_description):

    try:
        with open("tasks.json", "r") as arquivo:
            tasks = json.load(arquivo)
    except:
        tasks = []

     # próximo id = maior id existente + 1 (ou 1 se lista vazia)
    next_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = task(next_id,new_task_description)  # passa o id
    
    tasks.append(new_task.to_dict())

    with open("tasks.json", "w") as arquivo:
        json.dump(tasks, arquivo, indent=4, ensure_ascii=False)

#só altera a descrição    
def update(id, new_task_description):
    try: 
        with open("tasks.json", "r") as arquivo:
            tasks = json.load(arquivo)
    except:
        print("você ainda não tem nenhuma tarefa")
    
    for tarefa in tasks:
        if tarefa["id"] == id:
            tarefa["description"] = new_task_description
            tarefa["updatedAt"] = datetime.datetime.now().isoformat()
 
    
    with open("tasks.json", "w") as arquivo:
        json.dump(tasks, arquivo, indent=4, ensure_ascii=False)

def delete(id):
    try: 
        with open("tasks.json", "r") as arquivo:
            tasks = json.load(arquivo)
    except:
        print("você ainda não tem nenhuma tarefa")
    
    for tarefa in tasks:
        if tarefa["id"] == id:
            tasks.remove(tarefa)
    
    with open("tasks.json", "w") as arquivo:
        json.dump(tasks, arquivo, indent=4, ensure_ascii=False)
    
def mark_in_progress(id):
    try:
        with open("tasks.json", 'r') as f:
            tasks = json.load(f)
    except:
        print("você ainda não tem nenhuma tarefa")
    
    for tarefa in tasks:
        if tarefa["id"] == id:
            tarefa["status"] = "in-progress"
    
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def mark_done(id):
    try:
        with open("tasks.json", 'r') as f:
            tasks = json.load(f)
    except:
        print("você ainda não tem nenhuma tarefa")
    
    for tarefa in tasks:
        if tarefa["id"] == id:
            tarefa["status"] = "done"
    
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def lista(status = None):
    try:
        with open("tasks.json", 'r') as f:
            tasks = json.load(f)
    except:
        print("você ainda não tem nenhuma tarefa")
    
    if status ==  None:
        print(*(tarefa["description"] for tarefa in tasks), sep="\n")
    else:
        print(*(tarefa["description"] for tarefa in tasks if tarefa["status"] == status), sep="\n")