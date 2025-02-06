const { readFileSync, writeFileSync } = require('fs')

let notes = []
const notesFile = './notes.json'

function loadNotes() {
    try {
        notes = JSON.parse(readFileSync(notesFile))
        renderNotes()
    } catch (err) {
        notes = []
    }
}

function saveNotes() {
    writeFileSync(notesFile, JSON.stringify(notes))
}

function renderNotes() {
    const noteList = document.querySelector('.note-list')
    noteList.innerHTML = notes
        .map(note => `
            <div class="note">
                <p>${note.text}</p>
                <small>${note.date}</small>
            </div>
        `).join('')
}

function addNote() {
    const input = document.querySelector('.note-input')
    if (input.value.trim()) {
        notes.push({
            text: input.value,
            date: new Date().toLocaleString()
        })
        saveNotes()
        renderNotes()
        input.value = ''
    }
}

window.addNote = addNote

document.addEventListener('DOMContentLoaded', loadNotes)