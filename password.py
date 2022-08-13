import random
lowercase="abcdefghijklmnopqrstuvwyxyz"
uppercase=lowercase.upper()
number="0123456789"
symbols="!@#$%^&*()+=-~`.,?/';\"\;"
use_for = uppercase+lowercase+symbols+number
#length_for_pass=input("value\n")
length_for_pass=int(input("Value \n "))
#length_for_pass1=10#
password="".join(random.sample(use_for,length_for_pass))
print("Generated PAss:",password)
                 