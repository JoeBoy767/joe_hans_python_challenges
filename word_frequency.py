def word_frequency(text):
    """Returns a dictionary with the frequency of each word in the input text."""
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')  # Normalize the word
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency
if __name__ == "__main__":
    try:
        with open("frequency_text.txt", "r", encoding="utf-8") as f:
            sample_text = f.read()
    except FileNotFoundError:
        print("Error: 'frequency_text.txt' not found.")
        exit(1)

    freq = word_frequency(sample_text)

    # Print the dictionary
    print("Word Frequency Dictionary:")
    print(freq)

    # Sort by most frequent first
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Print results
    print("Sorted Word Frequencies:")
    for word, count in sorted_freq:
        print(f"{word}: {count}")

    # Save to file
    output_file = "word_frequency_output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for word, count in sorted_freq:
            f.write(f"{word}: {count}\n")
