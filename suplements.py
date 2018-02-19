import tkinter as tk
from tkinter import filedialog
import time

def get_cumprimento():
	t_verify = int(time.strftime('%X %x %Z')[:2])
	if t_verify > 11:
		return ' <p class=MsoNormal><span style="font-size: \
		10.0pt; font-family: Century Gothic, sans-serif;">Boa tarde</span></p>'
	else:
		return ' <p class=MsoNormal><span style="font-size: \
		10.0pt; font-family: Century Gothic, sans-serif;">Bom dia</span></p>'

def get_messsage(m):
	dia = time.strftime('%d/%m/%Y')
	if int(m) == 1:
		return '''<p class="MsoNormal"><span style="font-size:10.0pt; 
		font-family: Century Gothic, sans-serif"> Seguem Negativas realizadas dia ''' + \
		dia + '''</span></p><p class="MsoNormal">
		<span style="font-size:10.0pt; font-family: 
		Century Gothic, sans-serif">Atenciosamente</span></p>
		'''
	elif int(m) == 2:
		return '''<p class="MsoNormal"><span style="font-size:10.0pt; 
		font-family: Century Gothic, sans-serif"> Seguem PIs realizadas dia ''' + \
		dia + '''</span></p><p class="MsoNormal">
		<span style="font-size:10.0pt; font-family: 
		Century Gothic, sans-serif">Atenciosamente</span></p>
		'''

def get_assinatura():
	assinatura = ''
	with open('...\\AppData\\Roaming\\Microsoft\\Assinaturas\\Assinatura.htm', 'r') as f:
		assinatura += f.readline()
	return assinatura

def get_objetos():
	root = tk.Tk()
	root.withdraw()
	return filedialog.askopenfilenames()