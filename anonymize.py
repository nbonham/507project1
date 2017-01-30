import re
import random

## is instruction # is my comment

##Open the mbox.txt file. [Note: you will need to copy mbox.txt into your working directory and commit it to your repository. See Addendum #1 for more details.] - DONE
fhand=open("mbox.txt")
uniqueEmails = []
anonCodes = []
count = 0
test = 0

## access email addresses using regular expressions - DONE
# look for @ where the first character is blank space or >, then next character is a letter
# should also contain a . to weed out things like apache
# put all unique emails into a list
# need to account for this 200712122109.lBCL9iKA007051@nakamura.uits.iupui.edu
for line in fhand:
    line = line.rstrip()
    x = re.findall('[\s|<]([a-zA-Z]\S+@\S+[\.]+\S+[a-zA-Z])', line)
    if len(x) > 0 :
        xStr = x[0]
        if xStr not in uniqueEmails :
            uniqueEmails.append(xStr)
#print(uniqueEmails)
fhand.close()

## For each email address*, assign a unique random ID. - DONE
# generate list of random codes
countEmails = len(uniqueEmails)
#print(countEmails)

while count < countEmails :
    rando = random.randint(10000,99999)
    if rando in anonCodes :
        continue
    else :
        rando = "%%"+str(rando)+"%%"
        anonCodes.append(rando)
        count += 1
#print(anonCodes)

# use the uniqueEmails and anonCodes lists to create a dictionary that maps a unique email to the given anon code
mapping = dict(zip(uniqueEmails,anonCodes))
#print(mapping)
#print(type(uniqueEmails))
#print(type(anonCodes))


## Replace each email address with the anon ID surrounded by %% and %% (these are to make it easy to identify the anonymized address locations). See example below. - DONE
## Write to a new file: mbox-anon.txt - DONE
#https://docs.python.org/2/library/re.html
# repoen file and also open a new file to write to
fhand=open("mbox.txt",'r')
fwrite=open('mbox-anon.txt','w')

#go through the mbox file, look for emails and then use the previously created mapping dictionary to replace the emails with their associated anon codes
#write new lines to a new file, if there is no email in the line then just write the original line
for line in fhand:
    line = line.rstrip()
    #print(line)
    x = re.findall('[\s|<]([a-zA-Z]\S+@\S+[\.]+\S+[a-zA-Z])', line)
    if len(x) > 0 :
        xStr = x[0]
        newline = line.replace(xStr,mapping.get(xStr)) + "\n"
        #print(mapping.get(xStr))
    else :
        newline = line + "\n"

    fwrite.write(newline)

fhand.close()
fwrite.close()

## Write the mapping from anon ID to email address to another file: mbox-anon-key.txt - DONE
keyMappings = open('mbox-anon-key.txt',"w")

for k in mapping :
    line = mapping[k][2:7] + "=" + k + "\n"
    keyMappings.write(line)

keyMappings.close()
