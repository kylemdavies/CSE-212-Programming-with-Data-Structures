def mystery_1(text):
    stack=[]
    for letter in text:
        stack.append(letter)
        
    result=""
    while len(stack)>0:
        result += stack.pop()
    return result

mystery_1("racecare")
