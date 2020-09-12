#..TO DETERMINES THE FREQUENCY OF OCCURRENCE OF PARTICULAR CHARACTERBIN THE STRING



string="computer engineering"
count=0
for i in string:
    if i=='e':
        count=count+1
print("count of e in is:"+str(count))
