def IsPalindrome(text):
    revstring=text[::-1]

    if revstring==text:
        return True
    else:
        return False

string = input('Enter the text : ')
reversestring=string[::-1]
check=IsPalindrome(string)

print('\nEntered text = %s' % (string))
print('The reverse of the entered text = %s' % (reversestring))

if check==True:
    print('\nThe entered text is palindrome')
else:
    print('\nThe entered text is not palindrome')