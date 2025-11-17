from file_manager import read_notes, write_notes, append_note

def add_note():
    note = input("Enter your note: ").strip()
    append_note(note)
    print("Note added successfully!")

def view_notes():
    notes = read_notes()

    if not notes:
        print("No notes found!")
        return

    print("\n--- All Notes ---")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note.strip()}")
    print("-----------------\n")

def search_notes():
    keyword = input("Enter keyword to search: ").strip().lower()
    notes = read_notes()

    found = False
    for i, note in enumerate(notes, 1):
        if keyword in note.lower():
            print(f"Found in Note {i}: {note.strip()}")
            found = True

    if not found:
        print("No matching notes found.")

def delete_note():
    notes = read_notes()
    view_notes()

    if not notes:
        return

    num = int(input("Enter note number to delete: "))

    if num < 1 or num > len(notes):
        print("Invalid note number!")
        return

    notes.pop(num - 1)
    write_notes(notes)
    print("Note deleted successfully!")

def replace_note():
    notes = read_notes()
    view_notes()

    if not notes:
        return

    num = int(input("Enter note number to replace: "))

    if num < 1 or num > len(notes):
        print("Invalid note number!")
        return

    new_note = input("Enter new note: ").strip()
    notes[num - 1] = new_note + "\n"
    write_notes(notes)
    print("Note replaced successfully!")

def clear_notes():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ").lower()
    if confirm == "yes":
        write_notes([])
        print("All notes cleared!")
    else:
        print("Canceled.")
