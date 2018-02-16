#6.5 Write code using find() and string slicing
#(see section 6.10) to extract the number at the end of
#the line below. Convert the extracted value to a
#floating point number and print it out.

greeting = 'Hello, world!'

def trocaletra(pos,word,letter):
    new_word_temp = letter + word[pos:]
    new_word= word[0:pos-1] + new_word_temp
    return  new_word

print (trocaletra(2,greeting,'a'))

text = "X-DSPAM-Confidence:    0.8475";
pos=text.find("    ")
print(pos)
text= text[pos:]
text= text.strip()
text=float(text)
print(text)
