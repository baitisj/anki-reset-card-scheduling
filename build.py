#! /usr/bin/env python
import os
import zipfile

outname='reset-card-scheduling.zip'

def zipdir(path,ziph):
  # ziph is zipfile handle
  for root, dirs, files in os.walk(path):
    for file in files:
      if '.py' in file:
        #ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root,file), os.path.join(path, '..')))
        ziph.write(os.path.join(root, file))

if __name__ == '__main__':
  zipf = zipfile.ZipFile(outname, 'w')
  zipdir('.', zipf)
  
