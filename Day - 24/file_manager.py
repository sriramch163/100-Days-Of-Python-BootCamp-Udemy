import os

FILE = "notes.txt"

def create_file():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            pass

def read_notes():
    with open(FILE, "r") as f:
        return f.readlines()

def write_notes(notes):
    with open(FILE, "w") as f:
        f.writelines(notes)

def append_note(note):
    with open(FILE, "a") as f:
        f.write(note + "\n")
