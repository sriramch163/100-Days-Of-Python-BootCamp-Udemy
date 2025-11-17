from file_manager import create_file
from actions import add_note, view_notes, search_notes, delete_note, replace_note, clear_notes

def menu():
    create_file()

    while True:
        print("""
===== NOTES MANAGER =====
1. Add Note
2. View Notes
3. Search Notes
4. Delete Note
5. Replace Note
6. Clear All Notes
7. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            replace_note()
        elif choice == "6":
            clear_notes()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    menu()
