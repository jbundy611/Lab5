"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3


conn = sqlite3.connect('Chainsaw_Juggling_records.sqlite')

#conn.execute('create table records (Name text, country text, record integer)')

#conn.execute('insert into records values ("Janne Mustonen", "Finland", 98)')
#conn.execute('insert into records values ("Ian Stewart", "Canada", 94)')
#conn.execute('insert into records values ("Aaron Gregg", "Canada", 88)')
#conn.execute('insert into records values ("Chad Taylor", "USA", 78)')

#conn.commit()



def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """


    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            conn.close()
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    for row in conn.execute('select * from records'):
        print(row)


def add_new_record():
    name = input('Enter the name of the record holder: ')
    country = input('Enter the country they are from: ')
    record = int(input('Enter their record: '))
    cur = conn.cursor()
    cur.execute('select Name from records where Name=?', (name, ))
    data = cur.fetchall()
    if not data:
        conn.execute('insert into records values (?, ?, ?)', (name, country, record))
        conn.commit()    
    else:
        print("already exists! bringing back to main menu.")
        
    


def edit_existing_record():
    #currently changes everyones record.
    name = input('Enter the name of the record holder you want to edit: ')
    cur = conn.cursor()
    cur.execute('select Name from records where Name=?', (name, ))
    data = cur.fetchall()
    if not data:
        print('Theres no one with that name, sending to main menu.')
    else:
        record = int(input("What did you want to change their record to?: "))
        conn.execute('UPDATE records SET record=?', (record,))



        

def delete_record():
    name = input('Enter the name of the record holder you want to edit: ')
    cur = conn.cursor()
    cur.execute('select Name from records where Name=?', (name, ))
    data = cur.fetchall()
    if not data:
        print('Theres no one with that name, sending to main menu.')
    else:
        cur.execute('delete from records WHERE name=?,' (name, ))


if __name__ == '__main__':
    main()