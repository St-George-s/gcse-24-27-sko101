
# Extension Task J
# Mor-se Coding   
# Create a program that allows you to enter a string and encode it into Morse code, using   ‘ . ‘ and ‘ - ‘ notation. Spaces between words should be replaced with the “|” (pipe) character.  
# Use a normal space for gaps between each character. 
# Optional Extensions:  
# Develop your program to translate from Morse to alphanumeric, using the standards above 

# Not fixed by teacher
user_sSentence = input("Enter a sentence: ")
user_sSentence.upper()
standardAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W,", "X", "Y", "Z", " ", ". "]
morseAlphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", " ", " | "]
for counter1 in range(len(user_sSentence)):
    for counter2 in range(0, 28):
        if user_sSentence[counter1] == standardAlphabet[counter2]:
            user_sSentence[counter1] = morseAlphabet[counter2]
print(user_sSentence)

# Fixed by teacher
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
         ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
         ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
         "--..", "|"]   # pipe replaces spaces between words
sentence = input("Enter a sentence: ").upper()
output = ""
for letter in sentence:
    found = False
    for counter in range(len(alphabet)):
        if letter == alphabet[counter]:
            output = output + morse[counter] + " "
            found = True
            break    # stop searching once matched
    if found == False:
        output = output + "? "   # for unknown characters
print(output)
