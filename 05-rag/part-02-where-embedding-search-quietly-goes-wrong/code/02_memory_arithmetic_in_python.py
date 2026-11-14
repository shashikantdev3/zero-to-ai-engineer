"""Zero to AI Engineer · RAG and Vector Search · Part 2 of 26
Slide: Memory Arithmetic in Python
Run: python 02_memory_arithmetic_in_python.py
"""
# Memory = vectors x dimensions x bytes
n = 1_000_000

def gb(dims, bytes_each):
    return round(n * dims * bytes_each / 1e9, 2)

print("float32 1536:", gb(1536, 4))
# truncated to 512 dimensions
print("float32 512:", gb(512, 4))
print("int8 1536:", gb(1536, 1))
# binary: one bit is an eighth of a byte
print("binary 1536:", gb(1536, 1 / 8))
