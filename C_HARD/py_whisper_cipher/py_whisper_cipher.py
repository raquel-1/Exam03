ma = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mi = "abcdefghijklmnopqrstuvwxyz"

coder_ma = {val: x + 1 for x, val in enumerate(ma)}
coder_mi = {val: x + 1 for x, val in enumerate(mi)}
decoder_mi = {val: x for x, val in coder_mi.items()}
decoder_ma= {val: x for x, val in coder_ma.items()}

def whisper_cipher(text: str, shift: int) -> str:
	hola = ""
	for char in text:
		if coder_ma.get(char, None) is not None:
			hola += decoder_ma[(coder_ma[char] + shift)%26]
		elif coder_mi.get(char, None) is not None:
			hola += decoder_mi[(coder_mi[char] + shift)%26]
		else:
			hola += char
	return hola
		


if __name__ == "__main__":
	print(whisper_cipher("hola como estas", 15))