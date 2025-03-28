"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    text = "012345"
    result = []
    for char in text:
        result.append(int(char))
    return result

print(fn_hack_6())