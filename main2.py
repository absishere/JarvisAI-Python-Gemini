import ollama

def get_response(query):
    response = ollama.chat(model='gemma3', messages=[
      {
        'role': 'system',
        'content': 'You are an Advanced Personal Assistant like Jarvis.',
      },
        {
          'role': 'user',
          'content': f"{query}"

        },
    ])
    return response['message']['content']

if __name__ == "__main__":
    while True:
        query = input("User: ")
        reply = get_response(query)
        if any(word in query.lower() for word in ['exit', 'quit', 'shut']):
            print("Jarvis: Understood. Shutting down now.")
            break
        print(f"Jarvis: {reply}")