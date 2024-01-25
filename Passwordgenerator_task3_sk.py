#Welcome to the Python Random Password Generator- Task-3 By Swetankan Kumar Sinha (Batch-A28)

#importing necessaty modules
import random
import string

#welcome Message
print("Welcome to the Python Random Password Generator !!")

len=0
#all characters datasets
lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
digits=string.digits
special=string.punctuation
combined=lowercase+uppercase+digits+special

while True:
   try:
    len=int(input("Enter the length of your password\n"))
    #shuffling characters
    passs = random.sample(combined,len)
    password="".join(passs)
    print(f"The password of length {len} is {password}")
    ans=input("Do you want to generate a new password(y/n): ").strip().lower()
    if ans!="y":
     break
   except Exception as e:
     print("Error: Invalid Input or",e,"\nPlease Try again.")
print ("Thanks for using this Password generator")