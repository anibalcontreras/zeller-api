from openai import OpenAI
import os
import environ
from zeller.settings import BASE_DIR
from ai.prompts import system_prompt

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
api_key = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=api_key)

def generate_ai_message(client_name, client_has_debts, model="gpt-4o"):
    """
    Genera un mensaje de AI basado en el estado del cliente y en el prompt de introducción.

    :param client_name: Nombre del cliente.
    :param client_has_debts: Booleano que indica si el cliente tiene deudas.
    :param model: Modelo a utilizar.
    :return: El texto generado por el modelo.
    """
    # Generar el mensaje inicial de `system`
    prompt = system_prompt(client_has_debts, client_name)


    try:
        # Crear el contexto de conversación con `system` y `user`
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "¿Qué autos tienen disponibles?"
                        }
                    ]
                }
            ]
        )
        
        # Extraer el contenido del mensaje generado por el `assistant`
        message_content = completion.choices[0].message.content
        return message_content
    
    except Exception as e:
        return "Lo siento, no puedo generar un mensaje en este momento."
