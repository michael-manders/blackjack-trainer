import os

# go through ./images/cards and remove all images that have a 2 at the end of the name and does not begin with number
for filename in os.listdir('./images/cards'):
    if not filename.endswith('2.png') and not filename[0].isdigit() and ("ace" not in filename or "spades" in filename):
        os.remove('./images/cards/' + filename)

# go through and remove 2 from the end of the name
for filename in os.listdir('./images/cards'):
    if filename.endswith('2.png'):
        os.rename('./images/cards/' + filename, './images/cards/' + filename[:-5] + '.png')

# remove jokers
for filename in os.listdir('./images/cards'):
    if filename.endswith('joker.png'):
        os.remove('./images/cards/' + filename)

# print all files in ./images/cards
# print(os.listdir('./images/cards')

# print total number of files in ./images/cards
print(len(os.listdir('./images/cards')))