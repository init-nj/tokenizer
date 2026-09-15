import inspect
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

source_code = inspect.getsource(TextVectorization)
with open("textvectorization_source.py", "w", encoding="utf-8") as f:
    f.write(source_code)

print("Saved source code to text_vectorization_source.py")
	
	
