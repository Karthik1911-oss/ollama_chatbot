import ollama 

while True:
    question = input("Enter the query :")

    if question.lower() in ['exit', 'quit']:
        print("bye")
        break

    response = ollama.generate(model='gemma:2b', prompt=question)

    print("Answer:", response['response'])
