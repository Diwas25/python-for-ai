# Variables and dynamic types
model_name = "Mistral"
parameters_billions = 7
context_window = 8192
is_open_source = True

# Type conversion (casting integer to float)
params_float = float(parameters_billions)

# Formatted string (f-string) interpolation
summary = (
    f"Model: {model_name} | "
    f"Parameters: {params_float:.1f}B | "
    f"Max Tokens: {context_window} | "
    f"Open-Source: {is_open_source}"
)

print(summary)
print("Type of context_window:", type(context_window))