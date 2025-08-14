import openai

openai.api_key = "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"


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
        You are a friendly medical assistant. Answer the following health-related question clearly and safely.
        DO NOT provide diagnoses or treatment plans. Only offer general information and advise consulting a doctor.

        Question: {user_input}
        Answer: 
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5  # Keeps responses conservative
            )
            print("\nBot:", response.choices[0].message['content'])
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    health_chatbot()