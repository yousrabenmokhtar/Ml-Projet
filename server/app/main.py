from fastapi import FastAPI,UploadFile,File,Form

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API"}

@app.get("/train")
def train():
  return {"message": "Hello Youssra"}


import pandas as pd

from server.app.models.tree import DecisionTreeModel
import io

from sklearn.model_selection import train_test_split

app = FastAPI()

@app.get("/decision")
async def train_decision_tree(
    file: UploadFile = File(...),
    target_column: str = Form("Survived"),  
    max_depth: int = Form(None)  
):
    """
    Entraîne un modèle d'arbre de décision avec le dataset Titanic.
    - file: Fichier CSV contenant les données Titanic.
    - target_column: Colonne cible (par défaut 'Survived').
    - max_depth: Limite optionnelle pour la profondeur de l'arbre.
    """
    
    content = await file.read()
    data = pd.read_csv(io.StringIO(content.decode("utf-8")))

    if target_column not in data.columns:
        return {"error": f"La colonne cible '{target_column}' n'existe pas dans le fichier."}


    X = data.drop(columns=[target_column])
    y = data[target_column]

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeModel(max_depth=max_depth)
    model.train(X_train, y_train)

    evaluation_results = model.evaluate(X_test, y_test)

    return {
        "message": "Modèle d'arbre de décision entraîné avec succès.",
        "evaluation": evaluation_results
    }

