def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  pig_latin_words = []
  
  for word in words:
    # Create the pig latin word and add it to the list
    if word.isalpha():
        pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)
    else:
        pig_latin_words.append(word)
  
  # Turn the list back into a phrase
  say = " ".join(pig_latin_words)
  return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
