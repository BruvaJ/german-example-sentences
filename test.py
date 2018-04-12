# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
import os
import pickle

GERMAN_ENTRY = 0
ENGLISH_ENTRY = 1

def selectionchange(self,i):
    print("Items in the list are :")

    for count in range(self.cb.count()):
        print(self.cb.itemText(count))
    print("Current index",i,"selection changed ",self.cb.currentText())


def get_note_ids(card_ids):
    nids = set()
    for id in card_ids:
        nids.add(mw.col.getCard(id).nid)
    return nids


def run():
    dict = pickle.load(open(os.path.join(mw.pm.addonFolder(), "deu_eng_final.p"), "rb"))
    searching_for = get_cards()

    ids = get_note_ids(searching_for)

    ## loop the notes, NOT THE CARDS - that would duplicate effort!
    notes = []
    for id in ids:
        note = mw.col.getNote(id)
        notes.append(note)
        example_sentences = 0
        ##### for every row in dictionary
        for row in dict:
            # until 4 sentences found
            if example_sentences > 4:
                break
            if (note['Front'] in row[GERMAN_ENTRY]):
                if(note['testing'] == None):
                    note['testing'] = ''
                note['testing'] += "<br />"
                note['testing'] += row[GERMAN_ENTRY]
                note['testing'] += "<br />"
                note['testing'] += row[ENGLISH_ENTRY]
                note['testing'] += "<br />"
                example_sentences += 1
    ##### flush only at the end. showed an increase in performance
    for note in notes:
        note.flush()
    mw.reset()


def get_cards():
    return mw.col.findCards("tag:german")


def testFunction():
    run()
    mw.combo = combo = QComboBox()
    combo.show()


# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)