import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# 1. Carregar dados
df = pd.read_csv("churn_dataset.csv")

# 2. Separar features e target
X = df[['idade', 'tempo_contrato', 'uso_mensal', 'suporte_chamados']]
y = df['cancelou']

# 3. Dividir dados (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Padronizar features para KNN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Treinar KNN com k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# 5. Avaliar acurácia no conjunto de teste
y_pred = knn.predict(X_test_scaled)
accuracy_5 = accuracy_score(y_test, y_pred)
print(f"Acurácia para k=5: {accuracy_5*100:.2f}%")

# 6. Testar k = 1, 3, 5, 7, 9 e comparar
k_values = [1,3,5,7,9]
accuracies = {}

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    preds = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, preds)
    accuracies[k] = acc
    print(f"k={k}: Acurácia = {acc*100:.2f}%")

# Perguntas para reflexão
best_k = max(accuracies, key=accuracies.get)
print(f"\nMelhor valor de k: {best_k} com acurácia de {accuracies[best_k]*100:.2f}%")

print("""
- O modelo errou mais com valores pequenos de k, que são mais suscetíveis a ruídos e overfitting.
- Valores maiores de k tendem a suavizar as previsões, reduzindo erros por ruído porém podendo causar underfitting.
- Mudar o parâmetro k altera o equilíbrio entre viés e variância: k pequeno tem baixa tendência (baixo viés) e alta variância; k grande tem alto viés e baixa variância.
""")
