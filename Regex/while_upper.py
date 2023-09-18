import time

def convert() -> str:
    word = input("Please enter the word: ")
    new_word = ""

    start_time = time.time()
    i = 0
    word_len = len(word)

    while i < word_len:
        new_word += word[i].lower()
        i += 1

    end_time = time.time()
    execution_time = end_time - start_time

    return new_word, execution_time

if __name__ == "__main__":
    converted_word, time_taken = convert()

    print("Converted word:", converted_word)
    print("Time taken:", time_taken, "seconds")

    