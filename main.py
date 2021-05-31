def file_read(fname,n,read_all,mode,firstorlast):
  with open(fname,mode) as file:
    if mode == "a":
      file.write("helloNA6")
    if mode == "r":
      i = 0
      file_text = file
      line_ls = []
      words_dict = {}
      if firstorlast == "first" or firstorlast == "last":
        file_text = file.readlines()[-n:]
      # print(file_text)
      # file_text = file.readlines()
      # print(file_text)
      
      for line in file_text:
        if read_all == 0 and firstorlast == "first".lower():
          if i<= n:
            print(line)
            print(i)
          i = i+1
        if read_all == 0 and firstorlast == "last".lower():
          print(line,end='')
          # print(i)
          # i = i+1
        if read_all == 1 and firstorlast == "all".lower():
          # file.read()
          line_ls.append(line)
          words = file.read().split()
          max_len = len(max(words, key=len))
          words_count = len(words)
          print("words_count:", len(words))
          print("words: ", words)
          print("max_len:",max_len)
          max_word= [word for word in words if len(word) == max_len]
          print("maxword",max_word)

          for word in words:
            if word in words_dict:
              words_dict[word] = words_dict[word] + 1 
            else:
              words_dict[word] = 1 
          print("words_dict: ", words_dict)
          # print(count_occ)
            # print(line_ls)
            # line_ls.append(line)
      print("line_ls",line_ls)
  # text = open(fname,"r")
  # print(text)
  return file
  
def file_size(fname):
  import os
  statinfo = os.stat(fname)
  return statinfo.st_size
        
def writelisttofile(fname,mode,lname):
  print(lname)
  with open(fname,mode) as file:
    for c in lname:
      print("c",c)
      file.write("%s\n" % c)
  return file
  
def copyfiletoanotherfilenolibrary(fname,cname):
  with open(fname) as f:
    with open(cname, "w") as f1:
        for line in f:
            f1.write(line)
            
def combinedfile(fname,cname,oname):
  with open(fname) as file1, open(cname) as file2:
    for line1,line2 in zip(file1,file2):
      combined_txt = line1+line2
      print(combined_txt)
      with open(oname, "w") as file3:
        file3.write(combined_txt)

def getrandomline(fname):
  import random
  with open(fname,"r") as file:
    words = file.read().splitlines()
    random_line = random.choice(words)
    return random_line
    
def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]
    return flist
    
def get_word_count(fname):
  file = open(fname,"r")
  line_count = file.read().splitlines()
  # print(line_count)
  word_count= 0
  for word in line_count:
    # print(word)
    word_count = word_count + 1
  return word_count
  
    
def count_words(fname):
   with open(fname) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
       
def combinefileslist(fname,cname):
  combined_list = []
  with open(fname) as file1, open(cname) as file2:
    for (line1,line2) in zip(file1,file2):
      combined_list.append(line1+line2)
  return combined_list
  
def createonefileperletter():
  import string, os
  if not os.path.exists("letters"):
     os.makedirs("letters")
  for letter in string.ascii_uppercase:
     with open(letter + ".txt", "w") as f:
         f.writelines(letter)
    
import string
def letters_file_line(n):
  import os 
  if not os.path.exists("words1.txt"):
    os.makedirs("words1.txt")
  with open("words1.txt", "w") as f:
    alphabet = string.ascii_uppercase
    letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
    f.writelines(letters)
letters_file_line(3) 
    
############## Call Functions ############################### 
 
# file_read('test.txt',15,1,"r","all")
# file_read('test.txt',2,0,"r","last")
# file_size('test.txt')
# print(writelisttofile('test.txt','a','[a,b,c]'))
# copyfiletoanotherfilenolibrary('test.txt','out.txt')
# combinedfile('test.txt','out.txt','combined.txt')
# print(getrandomline('test.txt'))
# isfileclosed('test.txt')
# print(remove_newlines('out.txt'))
# print(get_word_count('test.txt'))
# print(count_words("test.txt"))
# print(combinefileslist("test.txt","out.txt"))
# createonefileperletter()

############## Reference ###################################

# def isfileclosed(fname):
#   # fname.close() would close the file. 
#   file = open(fname,'r')
#   file.close()
#   print(file.closed())

# from shutil import copyfile
# copyfile('test.txt', 'out.txt')
 

