from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()

    return text

    # return "This should be a variable that contains your file text as one long string"


def make_chains(text_string):
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

    for i in range(len(text) - 2):
        value = chains.get((text[i], text[i + 1]), [])
        value.append(text[i + 2])
        chains[(text[i], text[i + 1])] = value


        # if value == []:
        #     print ("found an empty value for tuple", word_tuple)
        #     chains[word_tuple] = [add_value]
        # else:
        #     print ("found a non-empty value for tuple", word_tuple, ":", value)            
        #     new_value = chains[word_tuple].append(add_value)
        #     print ("adding value", new_value, "for key", word_tuple)            
        #     chains[word_tuple] = new_value
            

    print chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
