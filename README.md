# BullsAndCows
Game of Bulls and Cows played with English language words instead of integers.

A fun, educational and interesting programming exercise that offers something for everybody in the CS1/CS2 course. The task is to write a player that guesses the secret word based on how many bulls (right letter in right place) and cows (right letter in wrong place) each previous guess contained. Given this information, which words are still possible words as the secret word, and which one of these remaining words would be the most powerful guess to reveal new information about the secret word?

The student should write functions in the specifcation PDF file into file `bacplayer.py` if working in Python 3, or `BACImplementation.java` if working in Java 8. The functionality of methods will be the same in both cases.

Note that the pseudorandom seeds values will always produce the same secret words for everybody within the same language. However, the same seed will produce different secret words in Python and Java.

The instructor's current best private model solution makes about 4.9 misses per secret word on average, with secret words chosen between lengths 5 and 15, inclusive. Surely this can be beaten, but by how much? 

Wordlist `words_alpha.txt` taken from [dwyl/english-words](https://github.com/dwyl/english-words).
