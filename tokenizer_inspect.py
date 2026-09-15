import inspect
from tensorflow.keras.preprocessing.text import Tokenizer

# Get the source code string
source_code = inspect.getsource(Tokenizer)

# Write to a file named 'tokenizer_source.py'
with open("tokenizer_source.py", "w", encoding="utf-8") as f:
    f.write(source_code)

print("Saved source code to tokenizer_source.py")
