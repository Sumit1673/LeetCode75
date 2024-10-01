# decode string
def decodeString(s: str) -> str:
    stack = []
    repeat = 0
    string = ""
    for char in s:
        if char == "[":
            stack.append(string)
            stack.append(repeat)
            
            repeat = 0
            string = ""
        elif char =="]":
            num = stack.pop()
            curr_str = stack.pop()           
            string = curr_str + string*int(num)
        elif char.isdigit():
            repeat = repeat*10 + int(char)
        else:
            string += char
    return string

    
s = "3[a2[bc]]"
decodeString(s)
