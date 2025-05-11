from collections import Counter

def frequency_analysis(text):
    print("\n=== Frequency Analysis ===")
    
    # Keep only alphabetic characters and convert to uppercase
    cleaned = [c.upper() for c in text if c.isalpha()]
    
    total = len(cleaned)
    if total == 0:
        print("No letters to analyze.")
        return

    # Count the frequency of each letter
    freq = Counter(cleaned)

    # Display letters ordered by frequency
    for letter, count in freq.most_common():
        percentage = 100 * count / total
        print(f"{letter}: {count} ({percentage:.2f}%)")
    
    # Suggest comparing with letter frequency
    print("\nCompare with standard frequencies: https://en.wikipedia.org/wiki/Letter_frequency")