
def add_note():
  note = input("Enter note: ")                        #this line collects user input
  with open("notepad.txt", "a") as file:  #this adds new info to the file without deleting existing content
    file.write(note + "\n")               #this line ensures the new input is always on a new line
    
    
def view_note():
  try:
    with open("notepad.txt", "r") as file:
      print(file.read())
  except FileNotFoundError:
    print("No notes on the Notepad")


while True:
  choice = input("1. Add Note 2. View Notes 3. Exit: ")
  
  if choice== "1":
    add_note()
    
  elif choice== "2":
    view_note()
  
  else:
    break
     
