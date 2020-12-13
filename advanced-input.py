import pyinputplus as pyip

if __name__ == "__main__":
    first_number = pyip.inputNum(prompt="Enter a number: ")
    print(first_number)

    import pyinputplus as pyip
    response = pyip.inputNum('Enter num: ', min=4)
    print(response)
    response = pyip.inputNum('Enter num: ', greaterThan=4)
    print(response)
    # Pretty self explanatory
    response = pyip.inputNum('>', min=4, lessThan=6)
    print(response)
    # This allows the user to input ""
    response = pyip.inputNum(blank=True)
    print(response)
    # Limit gives us a finite number of retries
    response = pyip.inputNum(limit=2)
    print(response)
    # Timeout gives us a timelimit
    response = pyip.inputNum(timeout=10, default="Bitch")
    print(response)
    # This allows the user to input string based on a regexp
    response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
    response = pyip.inputNum(blockRegexes=[r'[02468]$'])
    print(response)
    # We def our custom validation function 
    def adds_to_ten(numbers):
        numbersList = list(numbers)
        for i, digit in enumerate(numbersList):
            numbersList[i] = int(digit)
        if sum(numbersList) != 10:
            raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
        return int(numbers) 
    # We pass it as a parameter to pyip inputCustom
    response = pyip.inputCustom(adds_to_ten)
    print(response)
    


