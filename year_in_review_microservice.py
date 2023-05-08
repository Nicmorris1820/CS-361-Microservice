import time
with open ('microservice.txt','r') as infile:
    line_start = infile.readline()
    while line_start == "":
        time.sleep(2)
        line_start = infile.readline()
count = 0
with open ('movies.txt','r') as infile:
    for line in infile:
        data = line.strip().split(',')
        title,rating,date = data
        year = date.split('/')[-1]
        if year == line_start:
             count +=1
with open('microservice.txt', 'w') as outfile:
    outfile.write(str(count))
