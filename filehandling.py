# # read
# f = open("new.txt",'r')
# # print(f.read())
# # it take all things by letter

# # read line
# # line = (f.readline())
# lines = (f.readlines())
# # it will take all line by a list
# # print(line)
# print(lines)

# f.close()

# # wri = open("new.txt",'w')
# # # wri.write("add this to txt file")
# # wriLines = ['Hello welcome\n', 'this basics of python\n', 'this file handling methods\n']
# # wri.writelines(wriLines)
# # wri.close()

# # append
# append  = open('new.txt','a')
# append.write("\n Add this Line")
# print("Added succesfully")
# append.close()

# with open("new.txt",'r') as f:
#     print(f.read())


import os

# if os.path.exists("new.txt"):
#     append  = open('new.txt','a')
#     append.write("\n Add this NEW Line")
#     print("Added succesfully")
#     append.close()
# else:
#     print("Not found")

# REMOVE 
# if os.path.exists("new.txt"):
#     os.remove("new.txt")
#     print("Removed")
# else:
#     print("Not found")

# seek
# with open("new.txt",'r') as f:    
#     print(f.seek(6))
#     print(f.tell())
#     print(f.read())
# tell


with open("new.txt",'r') as file:
    data = file.readlines()
    for f in data:
        print(f)