import random as r
import string

def passValuation (password):
    upperLetter = string.ascii_uppercase
    lowerLetter = string.ascii_lowercase
    numbers = string.digits
    specials  = string.punctuation
    score = 0
    hasUpper = any(1 if c in upperLetter else 0 for c in password)
    hasLower = any(1 if c in lowerLetter else 0 for c in password)
    hasNumber = any(1 if c in numbers else 0 for c in password)
    hasSpecial = any(1 if c in specials else 0 for c in password)

    charPresence = [hasUpper, hasLower, hasNumber, hasSpecial]
    pass_length = len(password)

    with open ('commonPasswords.txt', 'r') as f: 
        common = f.read().splitlines()

    if password in common:
        score = 0
        #print(f"The password is in a commond list password, change it immmediatly! Your score is {score} / 7")
        return -1 
    else:
        score += 1 

    if pass_length > 8:
        score += 1
    if pass_length > 12:
        score += 1
    if pass_length > 17: 
        score += 1
    if pass_length > 20:
        score += 1

    #print(f"Your Password has {pass_length} character. You got {score}/ 7 points")


    if sum (charPresence) > 1:
        score += 1
    if sum (charPresence) > 2:
        score += 1
    if sum (charPresence) > 3:
        score += 1 
        
    #print(f"Your Password has {str(sum(charPresence))} different character types. You got {score} / 7 points")

    if score < 4: 
        print(f"The password score is  {score}/7 it's very weak! Change it ASAP! ")
        return score
    elif score == 4: 
        print(f"The password is {score}/7 it's weak! Change it ASAP! ")
        return score
    elif score > 4 and score < 6:
        print(f"The password is {score}/7 it's pretty strong! ")
        return score
    elif score >= 6: 
        print(f"The password is {score}/7 it's very robust!")
        return score


def generatePassword(minLen, maxLen, amount, upper, lower, digit, spec): 
    upperLetter = string.ascii_uppercase
    lowerLetter = string.ascii_lowercase
    numbers = string.digits
    specials  = string.punctuation

    password = ""
    all = ""

    if upper:
        all += upperLetter
    if lower: 
        all += lowerLetter
    if digit: 
        all += numbers
    if spec:
        all += specials


    for i in range(amount):
        length = r.randrange(minLen, maxLen)
        password = "".join(r.sample(all, length))
        score = passValuation(password)
        print(f"{password}   |   {str(score)}/7")



