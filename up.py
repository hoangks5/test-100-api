import os
from random import randint

for i in range(40,700):
    
    for j in range(0, randint(200,500)):
        d = str(i) + ' day ago'
        with open('file.txt','a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="'+d+'" -m "commit"')
os.system('git push -u origin main')