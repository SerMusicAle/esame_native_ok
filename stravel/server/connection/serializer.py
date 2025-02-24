#serializer.py -----------------------------------------------------------
import json

def serialize_to_json(data):
    """
    Serializza un oggetto Python in una stringa JSON.

    :param data: L'oggetto Python da serializzare (es. dizionario).
    :return: Stringa JSON.
    """
    try:
        json_data = json.dumps(data)
        return json_data
    except (TypeError, ValueError) as e:
        print(f"Error serializing data to JSON: {e}")
        return None

def deserialize_from_json(json_data):
    """
    Deserializza una stringa JSON in un oggetto Python.

    :param json_data: La stringa JSON da deserializzare.
    :return: Oggetto Python (es. dizionario).
    """
    try:
        data = json.loads(json_data)
        return data
    except (TypeError, ValueError) as e:
        print(f"Error deserializing JSON data: {e}")
        return None

# Esempio di utilizzo
if __name__ == "__main__":
    # Esempio di dati da serializzare
    data_to_serialize = {
        "username": "test_user",
        "password": "secure_password"
    }

    # Serializzazione
    json_data = serialize_to_json(data_to_serialize)
    print("Serialized JSON:", json_data)

    # Deserializzazione
    deserialized_data = deserialize_from_json(json_data)
    print("Deserialized Data:", deserialized_data)
    