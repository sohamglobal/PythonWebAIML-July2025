file=open("emp.csv","r")
data=file.readline()
while data:
    print(data.split(',')[1]+" | "+data.split(',')[4])
    data=file.readline()


file.close()