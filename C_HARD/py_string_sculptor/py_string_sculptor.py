def string_sculptor(text: str) -> str:
    if text == "": 
        return ""
    text =  text.lower()
    l_text = list(text)
    length = len(l_text)
    i = 0
    up = False
    while i < length:
        if l_text[i] in "abcdefghijklmnopqrstuvwxyz": 
            if up == True: l_text[i] = l_text[i].upper()  #reassigned the change
            if up == False: up =  True
            else: up = False
        elif l_text[i] == " ": up = False
        i += 1
        
    return "".join(l_text)

if __name__ == "__main__":
	print(string_sculptor("hello"))
	print(string_sculptor("Hello World"))
	print(string_sculptor("abc123def"))
	print(string_sculptor("Python3.9!"))
	print(string_sculptor(""))