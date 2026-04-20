def word_counter():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as f:
            text = f.read()
            words = text.split()

            print("Total words: ", len(words))

            word_freq = {}
            for word in words:
                word= word.lower()
                word_freq[word] = word_freq.get(word, 0) + 1

            print("\nWord Frequencyn :")
            for word, count in word_freq.items():
                print(word, ":",count)
        
    except FileNotFoundError:
        print("File not found!")

word_counter()