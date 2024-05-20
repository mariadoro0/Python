from tkinter import messagebox, filedialog

nomefile = filedialog.askopenfilename(filetypes=(("file di testo", "*.txt"), ("tutti i file","*.*"),("file python", "*.py")))
print(nomefile)

res=messagebox.showinfo("Info","Ciao mondo!")
print(res)
#crea un popup

info=messagebox.askquestion("Domanda","Sei sicuro?")
print(info) #restituisce yes o no

war=messagebox.showwarning("Attenzione","Polli volanti in arrivo")
print(war)

err=messagebox.showerror("NO NO","Cazzi amari!")
print(err)

cos=messagebox.askyesnocancel("Cose","Che succede?")
print(cos)