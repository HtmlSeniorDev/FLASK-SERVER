file_name = 'ip_addr.txt' #Put here your file

with open(file_name,'r') as fnr:
    text = fnr.readlines()

text = "".join([line.strip() + ' -p tcp --dport 8080 -j DROP\nl-A INPUT -s ' for line in text])

with open(file_name,'w') as fnw:
    fnw.write(text)