from tkinter import *
import psycopg2
from tkinter import ttk

window = Tk()
window.geometry('500x400')
window.title('Registr vozidel')
window.resizable(False, False)



#funkce
#napojení na databázi a vytvoření tabulky
def create():
  connection = psycopg2.connect(
            dbname = 'evidence',
            user = 'postgres',
            password = 'admin',
            host = 'localhost',
            port = '5432'
  )
  cur = connection.cursor()
  cur.execute('''CREATE TABLE evidenceinfo(
                ID SERIAL,
                SPZ VARCHAR(7),
                BRANDCAR TEXT,
                STK DATE,
                OWN TEXT
  )''')
  connection.commit()
  connection.close()



#funkce na vložení dat do databáze
def insert_data(car_spz, car_brand, car_stk, car_own):
  connection = psycopg2.connect(
            dbname = 'evidence',
            user = 'postgres',
            password = 'admin',
            host = 'localhost',
            port = '5432'
  )
  cur = connection.cursor()
  query ='''INSERT INTO evidenceinfo(spz, brandcar, stk, own) 
              VALUES(%s, %s, %s, %s)'''
  cur.execute(query, (car_spz, car_brand, car_stk, car_own))            
  connection.commit()
  connection.close()
  
  #hledání
def search(spz, own):

   connection = psycopg2.connect(
            dbname = 'evidence',
            user = 'postgres',
            password = 'admin',
            host = 'localhost',
            port = '5432'
  )

   cur = connection.cursor()
   if spz and own:  
    query ='''SELECT * FROM evidenceinfo WHERE spz = %s AND own = %s'''
    cur.execute(query, (spz, own)) 
   elif spz:
    query ='''SELECT * FROM evidenceinfo WHERE spz = %s'''
    cur.execute(query,(spz,))
   elif own:
    query ='''SELECT * FROM evidenceinfo WHERE  own = %s'''
    cur.execute(query, (own,))
   else:
    print('Uveďte spz nebo jméno majitele.')
    connection.close()
    return

   row = cur.fetchall()
   #for r in row:
    # print(row)
   display_search(row)
   connection.commit()
   connection.close()
              
def display_search(data):
  listbox = Listbox(window, width=45, height=1)
  listbox.grid(row=10, column=1)
  listbox.insert(0, data)


#popisek sekce
write_label = Label(text='Vlož údaje o vozidle a majiteli.')
write_label.grid(row=0, column=1)

#spz vozidla
spz_label = Label(text='SPZ vozidla: ')
spz_label.grid(row=1, column=0)
spz_entry = Entry()
spz_entry.grid(row=1, column=1)

#značka vozidla
bran_car_label = Label(text='Název vozidla: ')
bran_car_label.grid(row=2, column=0)
brand_car_entry = Entry()
brand_car_entry.grid(row=2, column=1)

#stk vozidla do
stk_label = Label(text='STK do: ')
stk_label.grid(row=3, column=0)
stk_entry = Entry()
stk_entry.grid(row=3, column=1)

#majitel vozidla
owner_car_label = Label(text='Majitel vozidla: ')
owner_car_label.grid(row=4, column=0)
owner_car_entry = Entry()
owner_car_entry.grid(row=4, column=1)

#tlačítko vložit údaje
insert_button = Button(text='Vložit údaje', command=lambda:insert_data(spz_entry.get(), brand_car_entry.get(), stk_entry.get(), owner_car_entry.get()))
insert_button.grid(row=2, column=2)

#popisek sekce
search_label = Label(text='Najít údaje o vozidle a majiteli.')
search_label.grid(row=5, column=1)
#spz vozidla
search_spz_label = Label(text='Hledat podle SPZ: ')
search_spz_label.grid(row=6, column=0)
search_spz_entry = Entry()
search_spz_entry.grid(row=6, column=1)
search_info_label = Label(text='Nebo')
search_info_label.grid(row=7, column=1)
search_own_label = Label(text='Najít podle majitele')
search_own_label.grid(row=8, column=0)
search_own_entry = Entry()
search_own_entry.grid(row=8, column=1)
#tlačítko hledání
search_button = Button(window, text='Hledat údaje', command=lambda:search(search_spz_entry.get(), search_own_entry.get()))
search_button.grid(row=7, column=2)

window.mainloop()
