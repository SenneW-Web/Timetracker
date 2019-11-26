import sqlite3

file_name = 'Timetracker.sqlite3'
if(os.path.exists(f"{file_name}.db")):
    os.remove(f"{file_name}.db")

conn = sqlite3.connect(f"{file_name}.db")
c = conn.cursor()

c.execute('''CREATE TABLE Tabel(Activiteit, Start_tijd, Stop_tijd)''')

stoppen = input("Wilt u het programma stoppen: ")

while stoppen != "Ja":
    activiteit = input("Geef een activiteit in: ")
    start_tijd = input("Geef een starttijd in: ")
    stop_tijd = input("Geef een stoptijd in: ")
    c.execute("INSERT INTO Tabel VALUES (?, ?, ?)",
              activiteit, start_tijd, stop_tijd)
    stoppen = input("Wilt u het programma stoppen: ")
