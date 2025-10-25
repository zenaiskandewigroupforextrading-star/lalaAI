from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained(
    './models',
    model_file='tinyllama.gguf',
    model_type='llama',
    local_files_only=True
)

while True:
    prompt = input("Tanya ke LLM: ")
    if prompt.lower() in ['exit', 'quit']:
        break
    print("Bot:", llm(prompt))
