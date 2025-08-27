# Task : Write 10 hobbies in the file with a seperator
# Ask user about their hobby
# print hobby found if hobby is in file else print hobby not found




hobbys=["cricket","vollyball","football","kabardi","chess","tekwando","dandibeo","boxing","ludo","basketball"]

with open ("hobbys.txt","w") as f:
    f.write(",".join(hobbys))
print ("hobbies written in a file:")
user=input("ener your hobby").strip().lower()

with open("hobbys.txt","r")as f:
    data=f.read().strip().split(",")

    if user in data:
        print(f"hobby found ",user)
    else:
        print(f"hobbby {user} is not found")

