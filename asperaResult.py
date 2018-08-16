import os
import glob

userInput = input('Enter the path to find the pass and fail status:')

files = glob.glob(os.path.join(userInput, '*.txt'))

for fle in files:
   with open(fle) as f:
    f.readline()
      
    for line in f:
        
          if 'Total file transfer passed' in line:
              print(line)
          if 'Total file transfer failed' in line:
              print(line)
f.close()
             
