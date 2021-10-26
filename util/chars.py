#mycharorder = 'AaàáâBbCcDdEeéFfGgHhIiìíîJjKkLlMmNnOoòóôPpQqRrSsTtUuúVvXwXxYyZz'
mychars = (
("A", 0), ("a", 1), ("à", 2), ("á", 3), ("â", 4),
("B", 0), ("b", 1),
("C", 0), ("c", 1),
("D", 0), ("d", 1),
("E", 0), ("e", 1), ("é", 2),
("F", 0), ("f", 1),
("G", 0), ("g", 1),
("H", 0), ("h", 1),
("I", 0), ("i", 1), ("ì", 2), ("í", 3), ("î", 4),
("J", 0), ("j", 1),
("K", 0), ("k", 1),
("L", 0), ("l", 1),
("M", 0), ("m", 1),
("N", 0), ("n", 1),
("O", 0), ("o", 1), ("ò", 2), ("ó", 3), ("ô", 4),
("P", 0), ("p", 1),
("Q", 0), ("q", 1),
("R", 0), ("r", 1),
("S", 0), ("s", 1),
("T", 0), ("t", 1),
("U", 0), ("u", 1), ("ú", 2),
("V", 0), ("v", 1),
("W", 0), ("w", 1),
("X", 0), ("x", 1),
("Y", 0), ("y", 1),
("Z", 0), ("z", 1),
)
def gettagindex(mystr):
    indexes = []
    for x in mystr:
        letterindex = 0
        got = 999
        for c in mychars:
            if x in c[0]:
                got = letterindex
                break
            else:
                letterindex += 1
        indexes.append(got)
    return indexes
      
assert gettagindex("Ab") < gettagindex("ab")
assert gettagindex("a") < gettagindex("B")
assert gettagindex("áb") < gettagindex("ba")
assert gettagindex("ab") < gettagindex("bá")
assert gettagindex("á") < gettagindex("â")
assert gettagindex("â") < gettagindex("B")
assert gettagindex("é") < gettagindex("í")
assert gettagindex("é") < gettagindex("w")
