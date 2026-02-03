

def tokenize_text(text):
    tokens = text.split()
    return tokens

text = "Natural Language Processing is interesting."

print("Input Text:")
print(text)

print("\nTokens:")
print(tokenize_text(text))
