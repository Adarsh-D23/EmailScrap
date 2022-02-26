import re
import json

try:
    with open("websiteData.txt", encoding='utf8') as f:
        text = f.read()
        rel = dict()
        words = text.split()


except FileNotFoundError:
    text = None


def count(mail):
    count = 0
    for i in range(0,len(words)-1):
        if (mail == words[i]):
            count=count+1

    return count

def check_email(email):
    n1=email.find('@')
    text1=email[:n1]
    pattern1="[a-zA-Z0-9]+\.+[a-zA-Z0-9]"
    if (re.search(pattern1, text1) or len(text1)>=8):
        return 'Human'
    else:
        return 'Non Human'



for word in words:
    pattern= "[a-zA-Z0-9]+@+[a-zA-Z0-9]"
    if re.search(pattern, word):
        division=check_email(word)
        num=count(word)
        rel.update({word:{'Occurance': num, 'EmailType': division}})

result= json.dumps(rel, indent=1)
print(result)

with open("result.json", "w") as outfile:
    json.dump(rel, outfile, indent=4)


