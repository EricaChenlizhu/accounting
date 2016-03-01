import os
home='row//text'
txtName='会计'
names=os.listdir(home)

def writeFile(index,name,content):
    global txtName
    file=open('%s.txt'%txtName,'a',encoding='utf8')
    file.write(name+'\n')
    if len(index)==1:
        file.write('====\n')
    elif len(index)==2:
        file.write('----\n')
    elif len(index)==3:
        file.write('~~~~\n')
    file.write(''.join(content)+'\n')
    file.close()

for name in names:
    address=home+'//'+name
    file=open(address,'r',encoding='utf8')
    content=file.readlines()
    file.close()

    index,name=tuple(name.strip('.txt').split(' '))
    index=index.split('.')
    print(index)
    writeFile(index,name,content)