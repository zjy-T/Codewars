def meeting(s):
    s_lower = s.lower()
    list = s_lower.split(';')
    ret = []
    final = ""
    for i in list:
        ret.append(i.split(":"))
    for name in ret:
        name.reverse()
    ret.sort()
    for name2 in ret:
        final += "(" + str(name2[0].upper()) + "," + " " + str(name2[1].upper()) + ")"
    return final
s = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"

print(meeting(s))