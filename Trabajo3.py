import pandas as pd

# DataFrame inicial
people = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5],
        "iq": [105, 98, 110, 95, 100],
        "friends": [[2, 3], [1], [1, 5], [], [3]],
    }
)

# Diccionario para mapear el IQ por ID
diccionario = dict(zip(people["id"], people["iq"]))

# Función para calcular el IQ promedio de los amigos
def calcular(friend_ids):
    if not friend_ids:
        return float('nan')
    iq_values = [diccionario[fid] for fid in friend_ids if fid in diccionario]
    return sum(iq_values) / len(iq_values)

# Calcular friends_iq
people["friends_iq"] = people["friends"].apply(calcular)

# Calcular social_iq con la fórmula dada
people["social_iq"] = 0.7 * people["iq"] + 0.3 * people["friends_iq"]

# Redondear a 2 decimales
people["social_iq"] = people["social_iq"].round(2)

# Mostrar resultado
print("Personas con su IQ Social:")
print(people[["id", "iq", "friends", "friends_iq", "social_iq"]])
