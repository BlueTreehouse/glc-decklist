import sys
from transformations import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <decklist_path>")
        sys.exit(1)
    decklist_path = sys.argv[1]
    
    
    
    text = get_decklist(decklist_path)
    replaced = replacer(text)
    lines = line_maker(replaced)
    join = joiner(lines)
    num = quantity(join)
    print(num)






def get_decklist(filepath):
    with open(filepath) as f:
        return f.read()









main()
