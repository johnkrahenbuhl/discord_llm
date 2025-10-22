import lmstudio as lms

# Ensure LM Studio server is running on the specified host and port
SERVER_API_HOST = "localhost:1234" 


with lms.Client() as client:
    model = client.llm.model("openai/gpt-oss-20b")
    result = model.respond("Who are you, and what can you do?")
    print(result)
