vHexMin = ["61", "62", "63", "64", "65", "66", "67", "68", "69", "6A", "6B", "6C", "6D", "6E", "6F", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "7A"]
vCharMin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

vCharMai = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
vHexMai = ["41", "42", "43", "44", "45", "46", "47", "48", "49", "4A", "4B", "4C", "4D", "4E", "4F", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "5A"]

vCharNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
vHexNum = ["30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]


texto = open("braille.txt", "w")
texto.write("v2.0 raw\n")

aux = input("Digite o texto: ")

for i in aux:
	if i.isupper():
		for j in range(len(vCharMai)):
			if i == vCharMai[j]:
				texto.write(vHexMai[j])
				texto.write("\n")
				continue

	elif i.islower():
		for j in range(len(vCharMin)):
			if i == vCharMin[j]:
				texto.write(vHexMin[j])
				texto.write("\n")
				continue
	
	elif i.isspace():
		texto.write("20")
		texto.write("\n")
		continue

	elif i.isdigit():
		for j in range(len(vCharNum)):
			if i == vCharNum[j]:
				texto.write(vHexNum[j])
				texto.write("\n")
				continue
	else:
		print("o caracter {} não esta presente!".format(i))

print("OK!")