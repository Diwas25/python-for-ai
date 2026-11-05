raw_prompt = "   Hello World! Welcome to Python for AI.   \n"

# 1. Clean whitespace from edges
cleaned_prompt = raw_prompt.strip()

# 2. Case normalization
lower_prompt = cleaned_prompt.lower()

# 3. Punctuation removal via replacement
normalized_text = lower_prompt.replace("!", "").replace(".", "")

# 4. Tokenize by whitespace into words
tokens = normalized_text.split()

print("Original :", repr(raw_prompt))
print("Cleaned  :", normalized_text)
print("Tokens   :", tokens)