#################################Extracting Sub-Strings###################################
# Extracting Sub-Strings Practice #1
# Extract the first word of the following sentence using slicing, and display it on the screen:
text = "Controlling complexity is the essence of programming"
# Hint: "Controlling" is 11 characters long.
print(text[0:11])

# Extracting Sub-Strings Practice #2
# Take every third character starting from the ninth to the end of the sentence, and print the result.
text2 = "Never trust a computer you can't throw out a window"
print(text2[9:-1:3])

# Extracting Sub-Strings Practice #3
# Reverses the position of all the characters in the following sentence and displays the result on the screen.
text3 = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
print(text3[::-1]) # reverses sentence
##################################### String Methods#################################
# String Methods Practice #1
#slieds 12 -16
# Print the following text in uppercase, using the specific string method:
sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper())
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."

# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
word_list = ["Simple","is","better","than","complex."]
joined_list = " ".join(word_list)
print(joined_list)
# String Methods Practice #3
# Replace in the following sentence:
# "If the implementation is hard to explain, it might be a bad idea."
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.
sentence2 = "If the implementation is hard to explain, it might be a bad idea."
new_sentence = sentence2.replace("hard", "easy").replace("bad","good")
print(new_sentence)
#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.
repetition = "Repetition" * 15
print(repetition)
# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
haiku = "Whitecaps on the bay\nA broken signboard banging\nIn the April wind.\n — Richard Wright, collected in Haiku: This Other World, 1998"
indexHaiku = haiku.find("beach")
hasBeach = False
print(haiku)
print(f"Haiku has beach: {hasBeach}")

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
word = "electroencephalographist"
print(len(word))