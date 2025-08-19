file=open("myinfo.txt","a")
line=input('Enter a line of text : ')
file.write(f"{line}\n")
file.close()