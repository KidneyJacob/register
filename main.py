from tkinter import *
import psycopg2

window = Tk()
window.geometry('500x400')
window.title('Registr vozidel')
window.resizable(False, False)



#funkce
def create():
#napojení na databázi a vytvoření tabulky
  connection = psycopg2.connect(
            dbname = 'evidence',
            user = 'postgres',
            password = 'admin',
            host ='localhost',
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




def insert_data(car_spz, car_brand, car_stk, car_own):
  connection = psycopg2.connect(
            dbname = 'evidence',
            user = 'postgres',
            password = 'admin',
            host ='localhost',
            port = '5432'
  )
  cur = connection.cursor()
  query ='''INSERT INTO evidenceinfo(spz, brandcar, stk, own) 
              VALUES(%s, %s, %s, %s)'''
  cur.execute(query, (car_spz, car_brand, car_stk, car_own))            
  connection.commit()
  connection.close()

insert_data('5AY2470', 'Fiat Tipo', '21.5.2025', 'Jan Novak')






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
insert_button = Button(text='Vložit údaje')
insert_button.grid(row=2, column=2)

#popisek sekce
search_label = Label(text='Najít údaje o vozidle a majiteli.')
search_label.grid(row=5, column=1)
#spz vozidla
search_spz_label = Label(text='Zadej SPZ vozidla: ')
search_spz_label.grid(row=6, column=0)
search_spz_entry = Entry()
search_spz_entry.grid(row=6, column=1)
#tlačítko hledání
search_button = Button(text='Hledat údaje')
search_button.grid(row=6, column=2)

window.mainloop()
