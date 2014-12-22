# Open the dictionary files
enable = open("enable1.txt")

# Open all the text files
length4 = open("very_easy.txt",'w') 
length5 = open("easy.txt",'w')
length6 = open("medium.txt",'w')
length7 = open("hard.txt",'w')
length8 = open("very_hard.txt",'w')

files = [length4, length5, length6, length7, length8]


# Read and write those files (5 and 10 include \n)
for i in range(5,10):
    enable.seek(0)
    for a in enable:
        if len(a) == i:
            files[i-4].write(a)
