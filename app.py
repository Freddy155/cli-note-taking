import json
import os

def add_note(notes, note_title, note_content):
    note = {"title": note_title, "content": note_content}
    notes.append(note)
    print("Note added successfully.")

def list_notes(notes):
    if not notes:
        print("No notes available.")
    else:
        print("Your Notes:")
        print("------------")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note['title']}")

def view_note_content(notes, note_index):
    if note_index < 1 or note_index > len(notes):
        print("Invalid note index.")
    else:
        note = notes[note_index - 1]
        print(f"Title: {note['title']}")
        print("Content:")
        print(note['content'])

def edit_note(notes, note_index):
    if note_index < 1 or note_index > len(notes):
        print("Invalid note index.")
    else:
        note = notes[note_index - 1]
        print(f"Editing note: {note['title']}")
        current_content = note['content']
        print("Current Content:")
        print(current_content)
        new_content = input("Enter the new content (or press Enter to keep the existing content): ")

        if new_content:
            note['content'] = new_content

        print("Note edited successfully.")

def save_notes(notes, filename):
    with open(filename, 'w') as file:
        json.dump(notes, file)

def load_notes(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            notes = json.load(file)
            return notes
    else:
        return []

def main():
    notes_filename = "notes.json"
    notes = load_notes(notes_filename)

    while True:
        print("Options:")
        print("1. Add a note")
        print("2. List notes")
        print("3. View note content")
        print("4. Edit note")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            note_title = input("Enter the note title: ")
            note_content = input("Enter the note content: ")
            add_note(notes, note_title, note_content)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            note_index = int(input("Enter the index of the note you want to view: "))
            view_note_content(notes, note_index)
        elif choice == "4":
            note_index = int(input("Enter the index of the note you want to edit: "))
            edit_note(notes, note_index)
        elif choice == "5":
            save_notes(notes, notes_filename)
            print("Notes saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
