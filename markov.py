from random import choice
import sys
import twitter
import os

def open_and_read_file(filenames):
    """Takes file path as string; returns text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = ''
    for file in filenames:
        text = text + open(file).read()
    return text

    # return "This should be a variable that contains your file text as one long string"


def make_chains(text_string, n=2):
    """Takes input text as string; returns _dictionary_ of markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    text = text_string.split()
    
    chains = {}

    for i in range(len(text) - n):
        words = []
        for j in range(n):
            words.append(text[i + j])
        words = tuple(words)
        chains[words] = chains.get(words, []) + [text[i + n]]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    
    current_key = choice(chains.keys())
    
    while current_key[0][0].istitle() == False:
        current_key = choice(chains.keys())

    text = " ".join(current_key)

    punctuation = ['.', '?', '!']

    while text[-1] not in punctuation and len(text) < 140:
        if current_key in chains:
            string = choice(chains[current_key])
            text = "{} {}".format(text, string)
            current_key = list(current_key[1:])
            current_key.append(string)
            current_key = tuple(current_key)
    
    if len(text) < 140:
        return text
    else:
        make_text(chains)

def check_text(new_text, original_string):
    """Checks to see if the returned phrase is taken from one source only"""

    if new_text == None:
        return 1

    if new_text in original_string.replace('\n', " "):
        return 1
    else:
        return 2

def tweet(text):

    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    status = api.PostUpdate(text)
    print status.text

input_paths = sys.argv[1:]
#input_path_2 = sys.argv[2]
#n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_paths)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

check = check_text(random_text, input_text)

while True:
    if check_text(random_text, input_text) == 1:
        random_text = make_text(chains)
    else:
        print random_text
        break

#tweet(random_text)

