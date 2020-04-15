# Bulls And Cows With Words
The classic game of [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) but this time played with English words that have no repeated characters, instead of the symmetric space of plain old integers with no repeated digits.

A fun, educational and interesting programming exercise that offers something for everybody in a CS1/CS2 course so that some kind of rudimentary version of the player is reasonably straightforward to get started with, but the various parts and decisions can be endlessly optimized and streamlined for gradual but measurable improvement that motivates the students to think about the next possible optimization step.

The task is to write a player agent that guesses the secret word based on how many bulls (right letter in right place) and cows (right letter in wrong place) each previous guess contained. Given this information, which words are still possible words as the secret word? Which one of these remaining words would be the most powerful guess to reveal new information about the secret word?

The student should write functions listed in the specification document into file `bacplayer.py` if working in Python 3, or `BACImplementation.java` if working in Java 8. The functionality of methods will be the same in both cases.

Note that the same pseudorandom `seed` values will always produce the same secret words for everybody within the same language, regardless of the underlying computer platform. However, the same seed will produce different secret words in the current versions of testers written in Python and Java.

The instructor's current best private model solution needs about 4.7 guesses per secret word on average, when the secret words chosen have lengths between 5 and 15, inclusive. Surely this can be improved, but by how much? What is the true entropy of this problem? The student who can answer these questions best and prove this by earning the lowest score among all student submissions earns the ceremonial title of "The Fastest Gun East of Mississauga".

Wordlist `words_alpha.txt` taken from [dwyl/english-words](https://github.com/dwyl/english-words).
