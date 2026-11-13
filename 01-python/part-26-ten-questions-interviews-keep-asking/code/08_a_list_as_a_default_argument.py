"""Zero to AI Engineer · Python · Interview Quiz
Slide: A list as a default argument
Run: python 08_a_list_as_a_default_argument.py
"""
def add_msg(msg, history=[]):
    history.append(msg)
    return history
print(add_msg("a"))
print(add_msg("b"))
print(add_msg.__defaults__)
