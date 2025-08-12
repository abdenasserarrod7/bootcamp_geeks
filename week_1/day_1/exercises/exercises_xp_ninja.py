# ------ Exercise 1

# x is True
# y is False
# a: 5
# b: 10

# ------ Exercise 2

best = ""
print("Type the longest sentence you can without the letter 'A'. Type 'quit' to stop.")

while True:
    s = input("Your sentence: ")
    if s.lower() == "quit":
        break
    if "a" in s.lower():
        print("❌ Contains 'A'. Try again!")
        continue
    if len(s) > len(best):
        best = s
        print(f"🎉 Congrats! New record: {len(best)} characters.")
    else:
        print(f"Best so far: {len(best)} characters.")



# ------ Exercise 3

paragraph = (
    "Our reliance on single-use plastic water bottles is more than simply wasteful; "
    "it is bad for our environment because of the composition of the bottles themselves "
    "and the chemicals they release as they break down in our landfills. Single-use plastic "
    "water bottles cause dangerous substances to “leach” into the soil and water (Macklin). "
    "The bottles typically don’t begin to break down for one hundred years, or even longer. "
    "As they break down, they release dangerous chemicals like bisphenol-A into the soil. "
    "Bisphenol-A is an endocrine disruptor, i.e., it can affect the levels of hormones within "
    "the human body, creating disease. As these chemicals accumulate in the soil, they eventually sink "
    "into the water table, contaminating the water (O’Connor)."
)

# Your code to analyze the paragraph goes here


import re

chars = len(paragraph)
words = re.findall(r"\b\w+(-\w+)?\b", paragraph)  # includes hyphenated
total_words = len(words)
sentences = re.split(r'[.!?]', paragraph)
sentences = [s for s in sentences if s.strip()]
num_sentences = len(sentences)
unique = set(w.lower() for w in words)
num_unique = len(unique)
non_ws_chars = len(paragraph) - paragraph.count(" ")
avg_words_per_sentence = total_words / num_sentences
non_unique = total_words - num_unique

print(f"Characters: {chars}")
print(f"Words: {total_words}")
print(f"Sentences: {num_sentences}")
print(f"Unique words: {num_unique}")
print(f"Non-whitespace chars: {non_ws_chars}")
print(f"Average words per sentence: {avg_words_per_sentence:.2f}")
print(f"Non-unique words: {non_unique}")


# ------ Exercise 4

# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
