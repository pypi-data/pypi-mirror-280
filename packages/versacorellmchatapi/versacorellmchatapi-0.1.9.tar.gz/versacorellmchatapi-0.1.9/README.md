# VersaCoreLLMChatAPI

A Python library for interacting with VersaCore LLM Chat API.

## Installation

```bash
pip install versacorellmchatapi
```

## Usage

```python
if __name__ == "__main__":

    def handle_chunk(chunk, end=False):
        # Custom handling of each chunk
        if chunk:
            print(chunk, end='', flush=True)
        if end:
            print()  # Print a newline at the end of the stream


    lm_studio_llm_api = VersaCoreLLMChatAPI("lmstudio")
    ollama_llm_api = VersaCoreLLMChatAPI("ollama")
    
    messages = [
        { "role": "system", "content": "You are a useful chatbot." },
        { "role": "user", "content": "write a short story of 2000 words about a funny corgi." }
    ]
    
    lm_studio_response = lm_studio_llm_api.chat_completions(
        messages, 
        model="lmstudio-community/Mistral-7B-Instruct-v0.3-GGUF/Mistral-7B-Instruct-v0.3-Q5_K_M.gguf", 
        temperature=0.7, 
        max_tokens=-1, 
        stream=True,
        callback=handle_chunk
    )
    

    ollama_response = ollama_llm_api.chat_completions(
        messages,
        model="mistral", 
        stream=True,
        callback=handle_chunk  # Use the custom callback to handle streaming chunks
    )

```