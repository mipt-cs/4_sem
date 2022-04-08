import os

for bs in range(1,1024,2):
  for md in range(1,128,8):
    os.system("build/pgo-1 "+str(bs)+ " " + str(md))
    print("Trained for ", "build/pgo-1 "+str(bs)+ " " + str(md))
