import json
import os

BRANCHES_FILE_PATH = os.path.join(os.path.dirname(__file__), "branches.json")

def system_prompt(client_has_debts, client_name):    
    with open(BRANCHES_FILE_PATH, "r") as f:
        branches_data = json.load(f)

    # Crear el saludo y el listado de autos y sucursales
    greeting = f"Eres un asistente virtual de la automotora Kaufmann que atiende a sus clientes. Eres amable y pareces humano. Recuerda que el nombre del cliente es {client_name}. Llamalo solo por su nombre, no apellido"
    catalog = "\n".join([f"{branch}: " + "; ".join(f"{car['brand']} {car['model']} ({car['type']})" for car in cars) for branch, cars in branches_data.items()])

    if client_has_debts:
        message = (
            "Dile al cliente que debido a su situación actual, puede explorar el catálogo completo de autos disponibles, "
            "pero no tendrá acceso a opciones de financiamiento hasta que regularice sus pagos. "
            "Recuerda mencionar que, al ponerse al día, puede ser considerado para financiamiento en el auto que más le guste, "
            "Puede contactarse contigo llamando al  +56 9 1234 5678. para recibir mas información de como regularizar pagos"
        )
    else:
        message = (
            "Hazle saber al cliente que, debido a su historial financiero positivo, tiene opciones de financiamiento disponibles "
            "para adquirir el auto que prefiera. Asegúrate de recordarle que esta es una ventaja especial para él por su buen comportamiento financiero."
        )

    prompt = (
        f"{greeting}\n"
        "Aquí tienes el catálogo de autos en nuestras sucursales:\n"
        f"{catalog}\n"
        f"{message}\n"
    )
    
    return prompt
