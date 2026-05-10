"""
Задание 2.3 — карринг и частичное применение (PyMonad).

"""

from pymonad.tools import curry


#  2.3.1: две строки → сцепление; 


@curry(2)
def concat_str(a: str, b: str) -> str:
    """Каррированное сцепление двух строк."""
    return a + b

greet_name = concat_str("Hello, ")


#  2.3.2: приветствие, знак после него, имя, заключительный знак

@curry(4)
def format_greeting(greet: str, first_punct: str, final_punct: str, name: str) -> str:
    return f"{greet}{first_punct} {name}{final_punct}"

first_step_greet = format_greeting

if __name__ == "__main__":

    
    print(greet_name("Nick")) 

    final_greet = first_step_greet("Hello")(",")("!")
    print(final_greet("Nick")) 
