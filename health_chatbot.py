from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DISCLAIMER = """
**Disclaimer**: I am an AI assistant and cannot provide medical advice. 
For serious health concerns, please consult a doctor.
"""


def health_chatbot():
    print("Health Query Chatbot (Type 'quit' to exit)")
    print(DISCLAIMER)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break

        prompt = f"""
        As a medical assistant, provide general information about:
        {user_input}

        Rules:
        1. No diagnoses or treatment plans
        2. Maximum 2 sentences
        3. Always suggest consulting a doctor
        """

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            print("\nBot:", response.choices[0].message.content)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    health_chatbot()