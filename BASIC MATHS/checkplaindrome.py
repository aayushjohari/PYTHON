def palindrome():
    number = int(input("Enter a number to reverse: "))
      
    reverse =0
    dup = number
    while number>0:
        ld = number%10
       
        reverse = (reverse *10) + ld
        number= number//10

    if dup == reverse:
            return True
    else:
            return False
   
if __name__=="__main__":
   
      print(palindrome())

