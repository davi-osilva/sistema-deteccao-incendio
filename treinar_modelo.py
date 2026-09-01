import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

dados = pd.read_csv("equipamentos.csv")

X = dados[
    [
        "temperatura",
        "vibracao",
        "horas_uso",
        "dias_desde_manutencao",
        "falhas_anteriores"
    ]
]

y = dados["risco"]

modelo = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

modelo.fit(X, y)

joblib.dump(modelo, "modelo_risco.pkl")

print("Modelo salvo com sucesso!")