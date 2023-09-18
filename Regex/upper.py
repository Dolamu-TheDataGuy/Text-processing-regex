import time

def convert() -> str:
    word = input("Please enter the word: ")
    new_word = ""

    start_time = time.time()

    for w in word:
        w = w.lower()
        new_word += w

    end_time = time.time()
    execution_time = end_time - start_time

    return new_word, execution_time

if __name__ == "__main__":
    converted_word, time_taken = convert()

    print("Converted word:", converted_word)
    print("Time taken:", time_taken, "seconds")

    