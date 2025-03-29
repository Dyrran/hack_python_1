"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    
    looplimit = 0
    position = 1
    rsize = len(result)

    while looplimit < rsize:
        result.insert(position, "@")
        looplimit += 1
        position += 2
    
    return result