x = "hello"
y = "heil"
z = "hello"
c = "Agnes i Senga"


def check_equal(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    if str1 == str2:
        return True
    else:
        return False

#print(check_equal(x, y))


def reversed_word(string):
    reversedlist = []
    strlist = list(string)
    length = len(string)
    x = 0
    while len(reversedlist) != length:
        x -= 1
        reversedlist.append(strlist[x])


    return "".join(reversedlist)

#print (reversed_word("Morna Jens"))

def check_palindrome(string):
    gnirts = reversed_word(string).lower()
    if string.lower() == gnirts:
        return True
    else:
        return False

#print(check_palindrome(c))

def contains_string(string1, string2):
    if string2 in string1:
        hvor = string1.find(string2)
        return True, hvor
    else:
        hvor = string1.find(string2)
        return False, hvor

print(contains_string("pepperkake", "per"))
print(contains_string("pepperkake", "pær"))
