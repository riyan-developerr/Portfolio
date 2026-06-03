# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch

# model_name = "Qwen/Qwen3-0.6B"

# tokenizer = AutoTokenizer.from_pretrained(model_name)

# model = AutoModelForCausalLM.from_pretrained(
#     model_name,
#     torch_dtype="auto",
#     device_map="auto"
# )

# prompt = "Explain artificial intelligence in simple words."

# inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# outputs = model.generate(
#     **inputs,
#     max_new_tokens=100
# )

# response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# print(response)

from transformers import pipeline
qwen=pipeline(
    "text-generation",
    model="Qwen/Qwen3-0.6B"
)

response=qwen("Explain the importance of sleep",max_new_tokens=150)
print(response[0]["generated_text"])
print(type(response))
