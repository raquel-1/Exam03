def echo_validator(text: str) -> bool:
    if not text: return False
    
    clean_text = [char.lower() for char in text if char.isalpha()]
    
    if not clean_text: return False
    
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("hello"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator(""))
