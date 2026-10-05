mp = {
    'A': 'A',
    'E': '3',
    'H': 'H',
    'I': 'I',
    'J': 'L',
    'L': 'J',
    'M': 'M',
    'O': 'O',
    'S': '2',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': '5',
    '1': '1',
    '2': 'S',
    '3': 'E',
    '5': 'Z',
    '8': '8'
}
def sol(s):
    
    ss=s[::-1]
    ssss=""
    for c in ss:
        ssss+=mp.get(c,'.');
    sss=""
    for c in s:
        sss+=mp.get(c,'@');
    if s==ssss and ss==s:
        print(s,end="")
        print(" -- is a mirrored palindrome.",end="\n\n")
        return
    if s==ssss:
        print(s,end="")
        print(" -- is a mirrored string.",end="\n\n")
        return
    if s==ss:
        print(s,end="")
        print(" -- is a regular palindrome.",end="\n\n")
        return
    print(s,end="")
    print(" -- is not a palindrome.",end="\n\n")
    return
    
while True:
    try:
        s=str(input().strip());
    except EOFError:
        break
    sol(s)