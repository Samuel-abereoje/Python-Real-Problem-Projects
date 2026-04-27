import json
from datetime import datetime
import os

FILE_NAME = "notes.json"


def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


def add_note():
    notes = load_notes()
    
    note_text = input("Enter note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note = {
        "id": len(notes) + 1,
        "text": note_text,
        "created_at": timestamp
    }
    
    notes.append(note)
    save_notes(notes)
    
    print("Note added successfully!")


def view_notes():
    notes = load_notes()
    
    if not notes:
        print("No notes yet.")
        return
    
    print("\n Your Notes:")
    for note in notes:
        print(f"[{note['id']}] {note['text']} ({note['created_at']})")


def delete_note():
    notes = load_notes()
    
    if not notes:
        print("No notes to delete.")
        return
    
    view_notes()
    note_id = int(input("Enter ID to delete: "))
    
    notes = [note for note in notes if note["id"] != note_id]
    
    # Reassign IDs (clean structure)
    for i, note in enumerate(notes, start=1):
        note["id"] = i
    
    save_notes(notes)
    print("Note deleted.")


def search_notes():
    notes = load_notes()
    keyword = input("Enter keyword: ").lower()
    
    results = [note for note in notes if keyword in note["text"].lower()]
    
    if not results:
        print("No matching notes found.")
        return
    
    print("\n Search Results:")
    for note in results:
        print(f"[{note['id']}] {note['text']} ({note['created_at']})")


# ---------- MAIN LOOP ----------
def main():
    while True:
        print("\n==== NOTE MANAGER ====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Search Notes")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()