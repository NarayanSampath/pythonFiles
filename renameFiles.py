import os
path = 'D:/Vss-1/17-06-19/Agent/com/eg/jtm'
files = os.listdir(path)
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, file.replace('.compile','')))
print('done - '+ str(len(files)))