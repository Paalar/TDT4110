def read_from_filename(filename):
    f = open(filename, "r")
    #read = f.read()
    return f

def remove_symbols(text):
    specialChar = [",", ".", "'"]
    textList = []
    for i in text:
        textList.append(i)
    for u in textList:
        for j in specialChar:
            if u == j:
                textList.remove(u)
    textList = "".join(textList).lower()
    return textList

#print(read_from_filename("BIBLE.txt"))

#print(remove_symbols("Hey, it's me. You your you're"))
lor = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eleifend elit quam, id fermentum nulla blandit a. Cras sit amet metus rutrum, elementum odio non, interdum lectus. Vestibulum id varius arcu, quis finibus ligula. Suspendisse in nunc semper, tempus neque non, sollicitudin magna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Quisque lobortis luctus nisl in blandit. Proin scelerisque vel libero ut sodales. Nullam rhoncus lorem eros, eu tincidunt mi sodales ac. Nullam suscipit varius urna et aliquet. In sit amet bibendum nibh. Mauris interdum, metus non convallis dapibus, tellus nisl tempus tortor, sed malesuada quam ligula iaculis diam."
#print (remove_symbols(lor))

def count_words(filename):
    f = read_from_filename(filename)
    removed = remove_symbols(f)
    filelist = list(removed)
    newlist = []
    newerlist = []
    for i in filelist:
        newlist.append(i)
        if i == " ":
            newerlist.append("".join(newlist))
            newlist = []
    return newerlist

#print(count_words("lorem.txt"))
#print(count_words("BIBLE.txt"))
def main():
    x = read_from_filename("BIBLE.txt")
    f = remove_symbols(x)
    return f

print(main())
