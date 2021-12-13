def IsAnagram(tx1,tx2):
    lntext1=len(tx1)
    lntext2=len(tx2)

    tx1=sorted(tx1)
    tx2=sorted(tx2)

    if lntext1!=lntext2:
        return False
    else:
        for i in range(lntext1):
            if tx1[i]!=tx2[i]:
                return False

    return True


text1 = input("Enter 1.Text =")
text2 = input("Enter 2.Text =")

check=IsAnagram(text1,text2)

if check==False:
    print("The entered text not a anagram.")
else:
    print("The entered text a anagram.")



