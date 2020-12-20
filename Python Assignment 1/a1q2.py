# take input from user of thier first and last name then print them in reverse order

a=input("Enter your first name ")
b=input("Enter your last name ")

ans=a[::-1]+" "+b[::-1]            #here we use [::-1] to reverse the string and we individually reverse both a and b strings

ans=ans[::-1]                      # here we again reverse the string as we now want to reverse the name and surname 

print(ans)


#example
# a=dev  b=singh
# at first we will reverse it a will become a=ved  and b will become b=hgnis
# now we will concatenate a and b in ans, ans = ved hgnis
# now in order to get answer we will reverse it once again:
# ans = singh dev, now print it