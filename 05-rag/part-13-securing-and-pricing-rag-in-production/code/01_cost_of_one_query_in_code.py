"""Zero to AI Engineer · RAG and Vector Search · Part 13 of 26
Slide: Cost of one query in code
Run: python 01_cost_of_one_query_in_code.py
"""
def rag_cost(k, chunk_tokens, system_tokens,
             history_tokens, out_tokens,
             in_price_m, out_price_m):
    input_tokens = (system_tokens
                    + k * chunk_tokens
                    + history_tokens + 50)
    total = (input_tokens * in_price_m
             + out_tokens * out_price_m)
    return total / 1_000_000
# halving k from 10 to 5, 500-token chunks
saved = (10 - 5) * 500
print(saved, "input tokens saved per query")
