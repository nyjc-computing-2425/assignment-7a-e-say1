# Write a function to convert numbers to text numerals

def text_numeral(num: int) -> str:
    """
    This function takes in a positive integer less than 100, num, and returns a string representing num in a text format

    Parameters
    ----------
    num: int
        positive integer less than 100 that you want to convert into text
    
    
    """
    num_word = {1: "one", 2: "two", 3:"three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13:"thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

    numbers = list(num_word.keys())
    max_num = max(numbers)
    done = False
    words = []
    count = 0
    while done is False:
        if num >= max_num:
            num = num - max_num
            words.append(num_word.get(max_num))
            count += 1
        elif num == 0:
            words = " ".join(words)
            done = True
        elif num < max_num:
            max_num = numbers[numbers.index(max_num) - 1]
    return words  
