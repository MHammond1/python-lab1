 Exercise 2

def both_ends(s):
    if len(s) <= 2:
        return ''
    elif len(s) > 2:
        return s[0:2] + s[-2:]
s = input("Enter a word or phrase: ")
print(both_ends(s))