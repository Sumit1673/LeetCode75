import re

def average_word_length(sentence : str) -> float :
    """ # For a given sentence, return the average word length. 
        # Note: Remember to remove punctuation first.

    Args:
       sentence : str = sentence whose avg length to be calculated
       returns:
        float: avg length
    """
    try:
    #     words = sentence.split(" ")
    #     total_len = 0
    #     for word in words:
            
    #         for i in '-.,"!':
    #             if i in word:
    #                 word = word.replace(i, "")
    #         total_len += len(word)
    #     return total_len/len(words)
    # except:
    #     print("Check your input")

        filtered = ''.join()

def average_word_length_regex(sentence : str) -> float :
    """ # For a given sentence, return the average word length. 
        # Note: Remember to remove punctuation first.

    Args:
       sentence : str = sentence whose avg length to be calculated
       returns:
        float: avg length
    """
    try:
        pass
    except:
        print("Check your input")

if __name__ == '__main__':
    print(average_word_length('Hi all, my name is Tom...I am originally from Australia.'))
    