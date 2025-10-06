from ollama import Client
import time

client = Client() 

# constants
MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

def ask_ollama(question: str, model: str = MODEL_LLAMA, temperature: float = 0.0):
    if not question or not question.strip():
        raise ValueError("Question must be a non-empty string")
    
    messages = [
        {"role": "system", "content": "You are an AI Assistant just like LLM OpenAI and Claude"},
        {"role": "user", "content": question}
    ]

    try:
        response = client.chat(
            model=model,
            messages=messages,
            stream=True,#if stream is False then we would be getting the final answer from the Client
            options={"temperature": temperature}
        )
        start = time.time()
        print(f"Start time is {start}")
        full_answer = ""
        for chunk in response:  #Why chunk is added because its a steamline access where we have a inbuilt "message" key in client of ollama and that has a "content" and thereby  stream=True
            if "message" in chunk and "content" in chunk["message"]:
                text = chunk["message"]["content"]
                print(text, end="", flush=True)  # live output
                full_answer += text
        end = time.time()
        diff = end - start #added just to find out how many seconds does ollama takes to respond
        print(f"\nThe time difference is {diff}\n")
        print(f"The current time is {time.localtime()}\n") # this provides the real current time if confugured in the system OS
        # print("\n\nFinal Answer:\n", full_answer)

    except Exception as e:
        print(f"An exception occurred: {e}")


ask_ollama("What is 5*5")