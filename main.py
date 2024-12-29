from tkinter import *
import psycopg2

window = Tk()
window.geometry('500x400')
window.title('Registr vozidel')
window.resizable(False, False)



#funkce
#def insert_dat():








#popisek sekce
write_label = Label(text='Vlož údaje o vozidle a majiteli.')
write_label.grid(row=0, column=1)

#spz vozidla
spz_label = Label(text='SPZ vozidla: ')
spz_label.grid(row=1, column=0)
spz_entry = Entry()
spz_entry.grid(row=1, column=1)

#stk vozidla do
stk_label = Label(text='STK do: ')
stk_label.grid(row=2, column=0)
stk_entry = Entry()
stk_entry.grid(row=2, column=1)

#majitel vozidla
owner_car_label = Label(text='Majitel vozidla: ')
owner_car_label.grid(row=3, column=0)
owner_car_entry = Entry()
owner_car_entry.grid(row=3, column=1)

#tlačítko vložit údaje
insert_button = Button(text='Vložit údaje')
insert_button.grid(row=2, column=2)

#popisek sekce
search_label = Label(text='Najít údaje o vozidle a majiteli.')
search_label.grid(row=4, column=1)
#spz vozidla
search_spz_label = Label(text='Zadej SPZ vozidla: ')
search_spz_label.grid(row=5, column=0)
search_spz_entry = Entry()
search_spz_entry.grid(row=5, column=1)
#tlačítko hledání
search_button = Button(text='Hledat údaje')
search_button.grid(row=5, column=2)

window.mainloop()
