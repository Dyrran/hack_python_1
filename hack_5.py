"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    result = result[0] + "00" + result[3] + "1" + result[5] + "@" + result[7]
    return result 

print(fn_hack_5())