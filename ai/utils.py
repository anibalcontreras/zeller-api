from openai import OpenAI
import os
import environ
from zeller.settings import BASE_DIR
from ai.prompts import system_prompt

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
api_key = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=api_key)

def generate_ai_message(client_name, client_has_debts, model="gpt-4o"):
    prompt = system_prompt(client_has_debts, client_name)


    try:
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
        message_content = completion.choices[0].message.content
        return message_content
    
    except Exception as e:
        return "Lo siento, no puedo generar un mensaje en este momento."
