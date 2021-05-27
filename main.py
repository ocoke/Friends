import requests as req

file = open("./list.txt")

for line in file.readlines():
    domain = line.strip('\n')
    url = 'http://image.thum.io/get/width/1024/crop/768/allowJPG/noanimate/wait/5/maxAge/12/https://{}'.format(domain)
    print(domain)
    try:
        res =  req.get(url)
        with open('{}.jpg'.format(domain), "wb") as file:
            file.write(res.content)
    except:
        print("Error.")
    

file.close()
