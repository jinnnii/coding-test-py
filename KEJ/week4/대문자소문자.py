
def solution(my_string):
    result=''
    for i in my_string:
        ch = i.lower() if i.isupper() else i.upper()
        result+=ch
    return result

def _solution(my_string):
    return my_string.swapcase()