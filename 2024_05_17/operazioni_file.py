# apertura e lettura di un file intero
import os
import tkinter.filedialog as fd


curdir = os.getcwd()
stream = open("funzioni_platform.py", mode="rt", encoding="UTF-8")
txt=stream.read()
stream.close()

p=fd.asksaveasfilename(title="Salva come...", filetypes=[('text','*.txt'),('python','*.py')])
stream=open(p,"w+")
stream.write(txt)
stream.close()
print(stream.encoding)
