import itertools

def solve_cryptarithmetic():
    word1 = "SEND"
    word2 = "MORE"
    word3 = "MONEY"
    
    letters = set(word1 + word2 + word3)
    
    if len(letters) > 10:
        print("Too many unique letters, can't solve.")
        return

    for perm in itertools.permutations(range(10), len(letters)):

        letter_to_digit = dict(zip(letters, perm))
        
        num1 = int("".join(str(letter_to_digit[letter]) for letter in word1))
        num2 = int("".join(str(letter_to_digit[letter]) for letter in word2))
        num3 = int("".join(str(letter_to_digit[letter]) for letter in word3))
        

        if num1 + num2 == num3:
            print(f"Solution found!")
            print(f"{word1} + {word2} = {word3}")
            print(f"Mapping: {letter_to_digit}")
            print(f"{num1} + {num2} = {num3}")
            return
    
    print("No solution found.")

solve_cryptarithmetic()
