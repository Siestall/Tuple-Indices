try:
    text = (input('Text: '),)
    dist = int(input('Distance between elements: '))
    text2 = text[0][::dist]
    print(text2)
except:
    print('Enter integer')