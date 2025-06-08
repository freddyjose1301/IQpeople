import pandas as pd

# Crear el DataFrame inicial
people = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5],
        "iq": [105, 98, 110, 95, 100],
        "friends": [[2, 3], [1], [1, 5], [], [3]],
    }
)

# Crear un diccionario para mapear el IQ por ID
iq_dict = dict(zip(people["id"], people["iq"]))

# Función para calcular el IQ promedio de los amigos
def get_friends_iq(friend_ids):
    if not friend_ids:
        return float('nan')
    iq_values = [iq_dict[fid] for fid in friend_ids if fid in iq_dict]
    return sum(iq_values) / len(iq_values)

# Calcular friends_iq
people["friends_iq"] = people["friends"].apply(get_friends_iq)

# Calcular social_iq con la fórmula dada
people["social_iq"] = 0.7 * people["iq"] + 0.3 * people["friends_iq"]

# Redondear a 2 decimales
people["social_iq"] = people["social_iq"].round(2)

# Mostrar el resultado
print("People with Social IQ:")
print(people[["id", "iq", "friends", "friends_iq", "social_iq"]])
