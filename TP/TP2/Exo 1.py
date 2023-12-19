def inverse_mot(x) :
    y = reversed(list(x))
    y = ''.join(y)
    return y

def palindrome(x) :
    palindrome = True
    y = inverse_mot(x)
    if x != y :
        palindrome = False
    return palindrome

x = input('Entrez un mot :\n')
y = palindrome(x)
if y == True :
    print(x, 'est un palindrome')
else :
    print(x, "n'est pas un palindrome")