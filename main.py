def get_opposite_word(word):
    # Reverse the word to get the "opposite"
    return word[::-1]

def main():
    word = "example"  # You can change this to any word
    opposite_word = get_opposite_word(word)
    print(f"The opposite of '{word}' is '{opposite_word}'")

if __name__ == "__main__":
    main()
