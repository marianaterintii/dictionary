## Notes app
from os import system
from datetime import datetime


#   * add new notes (order
#   * show all notes
#   * delete note

#   * timer

notes = [
    {  "text": "table 1, 2 soups",
       "when": "17:8",
    },
    {  "text": "bill to table 2",
       "when": "17:10",
    
    },
    {  "text": "call mom",
       "when": None
    }

]

def cls ():
  system ("cls")

def showNotes(pnotes):
    now = datetime.now() #get current time
    h, m = now.hour, now.minute
    for note in pnotes:
        warning = ""
        if note["when"] != None:
            fragments = note["when"].split(":")
            nh, nm = int(fragments[0]), int(fragments[1])
            if h == nh and nm - m < 5 :
                warning = "( 5 or less min left !!!)"
        print(f"{note['text']} {warning}")
  


def addNote (pnotes):
  text = input ("enter text: ")
#HW: ask user for the note position
  place = int (input ("which position to add and time?: ")) - 1
  if place >= 0 and place <= len(notes): 
    pnotes.insert ( place, {"text": text, "when": "18:45"}) # tb de indicat si ora in input????
  else:
    print("something wrong")
  #pnotes.append({ "text": text})

def deleteNote(pnotes):
  idx = int(input("which one to delete: ")) - 1
  pnotes.pop(idx)

print()

#######################################

cls()
addNote(notes)
deleteNote(notes)
showNotes(notes)

print()