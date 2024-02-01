#嘉宾名单3-4.py
#3-4:
guest_list = ['Dad','Mom','sister'];
print (f"Hello {guest_list[0]},Would you like to have the dinner with me?")
print (f"Hello {guest_list[1]},Would you like to have the dinner with me?")
print (f"Hello {guest_list[2]},Would you like to have the dinner with me?")

#3-5
print (f"Oh,I'm just hear that My {guest_list[0]} can't come to have the dinner")
guest_list[0]='Yibin'

print (f"Hello {guest_list[0]},Would you like to have the dinner with me?")
print (f"Hello {guest_list[1]},Would you like to have the dinner with me?")
print (f"Hello {guest_list[2]},Would you like to have the dinner with me?")

#3-6
print ("Oh,I have just be told that there is a bigger table and I can invite tree more guest")

guest_list.insert(0,'CJ')
guest_list.insert(3,"CJY")
guest_list.append("Yellow red")

for i in range(0,6):
  print (f"Hello {guest_list[i]},Would you like to have the dinner with me?")
#3-7
print("Oh,everyone,I have just get a bad news,I can't get a big table\n\t\tso I can just invite two friends")

for i in range (0,4):
   name = guest_list.pop();
   print (f"I'm sorry that I can't invite you,{name}")
for i in range (0,2):
	print (f"I'm glad that I can still invite you to have the dinner with me,{guest_list[i]}")
num = len(guest_list)
print (f"Tonight I have invite {num} guest come to have the dinner together")