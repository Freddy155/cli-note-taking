# CLI Note-Taking App

A simple command-line note-taking app written in Python. This application allows you to create, list, view, edit, and save your notes, providing a straightforward way to manage your information from the command line.

## Features

- Create and save notes with titles and content.
- List all saved notes, displaying their titles.
- View the content of a specific note.
- Edit existing notes as if writing them from scratch.
- Save notes to a file for persistent storage.

## Prerequisites

To run this application, you need:

- Python 3.x installed on your system.
- A terminal or command prompt to execute the app.

## Usage

1. Clone this repository to your local machine.

```bash
git clone https://github.com/Freddy155/cli-note-taking.git
```
2. Navigate to the repository directory.

```bash
cd cli-note-taking
```

3. Run the app.

```bash
python app.py
```

4. Follow the on-screen instructions to create, list, view, edit, and save your notes.

How it Works
------------

-   When you create a note, you provide a title and content. These notes are stored in memory while the app is running.

-   The app allows you to list all saved notes, displaying their titles.

-   You can view the content of a specific note by selecting it from the list.

-   Editing a note shows you the current content and lets you modify it as if writing it from scratch.

-   To ensure your notes are not lost, you can save them to a file when you choose to save and quit the application.

Data Persistence
----------------

Notes are saved to a file named `notes.json` in the same directory as the `notes_app.py` script. This ensures that your notes are retained even if you close the application.

