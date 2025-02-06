import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime

class StickyNote:
    def __init__(self):
        self.notes = []
        self.window = tk.Tk()
        self.window.title("Sticky Notes")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.window, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Note input
        self.note_input = tk.Text(self.main_frame, height=5, width=40)
        self.note_input.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Buttons
        ttk.Button(self.main_frame, text="Add Note", command=self.add_note).grid(row=1, column=0, pady=5)
        ttk.Button(self.main_frame, text="Delete Selected", command=self.delete_note).grid(row=1, column=1, pady=5)
        
        # Notes list
        self.notes_listbox = tk.Listbox(self.main_frame, height=10, width=50)
        self.notes_listbox.grid(row=2, column=0, columnspan=2, pady=5)
        
        self.load_notes()
        
    def add_note(self):
        note_text = self.note_input.get("1.0", tk.END).strip()
        if note_text:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            note = f"{timestamp}: {note_text}"
            self.notes.append(note)
            self.notes_listbox.insert(tk.END, note)
            self.note_input.delete("1.0", tk.END)
            self.save_notes()
            
    def delete_note(self):
        selection = self.notes_listbox.curselection()
        if selection:
            index = selection[0]
            self.notes_listbox.delete(index)
            self.notes.pop(index)
            self.save_notes()
            
    def save_notes(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)
            
    def load_notes(self):
        try:
            with open("notes.json", "r") as f:
                self.notes = json.load(f)
                for note in self.notes:
                    self.notes_listbox.insert(tk.END, note)
        except FileNotFoundError:
            pass
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = StickyNote()
    app.run()