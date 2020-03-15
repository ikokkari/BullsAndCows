import bacplayer as bp
import random

# Minimum length of the secret word.
minlen = 5
# Maximum length of the secret word.
maxlen = 15
# How many rounds to play.
rounds = 20
# Seed value for the RNG to generate the secret words.
seed = 888

# Accept the word into the wordlist if its length is within the
# limits and no letter occurs more than once in the word.
def acceptable(word):
    n = len(word)    
    return minlen <= n <= maxlen and len({c for c in word}) == n

# Count how many bulls and cows the guess contains with respect
# to the secret word.
def count_bulls_and_cows(guess, secret):
    bulls, cows = 0, 0
    for (c1, c2) in zip(guess, secret):
        if c1 == c2:
            bulls += 1
        else:
            cows += 1 if c1 in secret else 0                
    return (bulls, cows)
    
# Play one round of the game until the player correctly guesses
# the secret word, or the number of guesses exceeds mercy limit.
def play_one_round(secret, mercy = 20):
    guesses_so_far, guess = [], ''
    print(f"[{secret}]: ", end = '')
    while secret != guess and mercy > len(guesses_so_far):
        guess = bp.guess(len(secret), guesses_so_far)
        (bulls, cows) = count_bulls_and_cows(guess, secret)
        print(f"{guess} ", end = '')        
        guesses_so_far.append((guess, bulls, cows))
    print('')
    return len(guesses_so_far)

# Play the game for the given number of rounds.
def play(words, seed, rounds = 50):
    total, rng = 0, random.Random(seed)
    while rounds > 0:
        secret = rng.choice(words)
        total += play_one_round(secret)
        rounds -= 1
    print(f"{total} {bp.student_id()} {bp.author()}")
    
with open('words_alpha.txt', encoding="utf-8") as f:
    words = [x.strip() for x in f if acceptable(x.strip())]    
    print(f"BACRunner Python with seed={seed}.")
    bp.initialize_wordlist(words[:])
    play(words, seed, rounds)