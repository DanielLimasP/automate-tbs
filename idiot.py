import pyinputplus as pyip

if __name__ == "__main__":
    prompt = "Want to know how to keep an idiot busy for hours? "
    while True:
        response = pyip.inputYesNo(prompt)
        if response == "no":
            print("Thanks, have a fantastic day.")
            break
        
