import test

searching_for = test.get_cards()
nids = test.get_note_ids(searching_for)

for nid in nids:
   note = mw.col.getNote(nid)
   note['testing'] = ''
   note.flush()
mw.reset()