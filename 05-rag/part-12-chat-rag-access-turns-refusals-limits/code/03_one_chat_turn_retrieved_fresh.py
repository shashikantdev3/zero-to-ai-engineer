"""Zero to AI Engineer · RAG and Vector Search · Part 12 of 26
Slide: One chat turn, retrieved fresh
Run: python 03_one_chat_turn_retrieved_fresh.py
"""
def chat_turn(st, msg, user):
    q = rewrite_standalone(
        st.summ, st.recent[-4:], msg)
    chunks = retrieve(q, user=user)
    answer = generate(
        st.summ, st.recent[-4:], chunks, msg)
    st.recent.append((msg, answer))
    if len(st.recent) > 6:
        old = st.recent[:-4]
        st.summ = summarise(st.summ, old)
        st.recent = st.recent[-4:]
    return answer
