# open the file in read mode
file_read = open('ccc.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in append mode
file_write = open('ccc.txt', 'w')
# append in the file
file_write.write("\n File in write mode ....")
file_write.write("Hi! I love Agriculture")
file_write.close()

# open the file in append mode
file_append = open('ccc.txt', 'a')
# append in the file
file_append.write("\n File in append mode ....")
file_append.write("Hi! I lik doing projects")
file_append.close()