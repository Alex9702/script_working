import win32com.client as win32
from suplements import *
from tkinter import *

def window(master):
	master.title('Envio de Email')
	Label(text='Escolha 1 - Negativas, 2 - Pis:').grid()
	e = Entry()
	e.grid(row=0, column=1)
	Button(text='Envio de Email', width=10, 
		command=lambda:email(e)).grid(row=1, columnspan=2)

def email(e):
	if e.get() != '1' and e.get() != '2':
		#root.quit()
		return 
	ol = win32.Dispatch('outlook.application')
	mail = ol.CreateItem(0)
	mail.To = 	'email@email.com'
	mail.CC = 'email@email.com'
	mail.Subject = 'teste'
	mail.HTMLBody = get_cumprimento()+ get_messsage(e.get()) + get_assinatura()

	for o in get_objetos():
		mail.Attachments.Add(o)

	mail.Display()
	#root.quit()

root = Tk()
app = window(root)
root.mainloop()