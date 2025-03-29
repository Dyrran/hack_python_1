"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    rlist = []
    rchar = ""

    for letter in result:
        rlist.append(change_char(letter))

    result = rlist
    return result

def change_char(chr):
    match chr:
        case "O":
            return "0"
        case "I":
            return "1"
        case "A":
            return "@"
        case default:
            return chr

print(fn_hack_10())