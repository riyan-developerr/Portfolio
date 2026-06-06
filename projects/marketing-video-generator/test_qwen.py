from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "Qwen/Qwen3-0.6B"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map="cpu",
    local_files_only=True
)

prompt = "Create a short marketing hook for a luxury perfume."

messages = [
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False
)

inputs = tokenizer(text, return_tensors="pt")

print("Generating...")
with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7
    )

response = tokenizer.decode(
    output[0][inputs["input_ids"].shape[-1]:],
    skip_special_tokens=True
)

print("\nMODEL RESPONSE:")
print(response)