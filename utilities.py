from typing import List, Tuple
import ntpath
import re
import itertools
import math

# supplementary functions
def convertCharListToStr(s):
    str1 = ""
    return str1.join(s)

def convertListOfStrToListOfInt(list_of_str: List[str]) -> List[int]:
    list_of_int = []
    for i in range(list_of_str.__len__()):
        list_of_int.append(int(list_of_str[i]))
    return list_of_int

def parseInputPairs(input: str) -> List[int]:
    return convertListOfStrToListOfInt(input.split(" "))

def printDictAsMultiLines(inData: dict):
    for key in sorted(inData):
        print("{} {}".format(key, inData[key]))

def getFileNameFromPath(fileFullPath: str) -> str:
    fileName = ntpath.basename(fileFullPath)
    if fileName.__len__() > 16:
        fileName = fileName [-16:-1]
    return fileName

def getFileNameLast16(fileFullName: str) -> str:
    if '\\' in fileFullName:
        name = fileFullName.split('\\')[-1][-16:]
    else:
        name = fileFullName[-16:]
    return name

def printArr(arr: list):
    for ele in arr:
        print(ele)

def printArrWSep(arr: list):
    strOut = ""
    for ele in arr:
        strOut = strOut + str(ele) + " "
    print(strOut[:-1])

def sortDictByValue(in_dict:dict, decreasing: bool) -> dict:
    return {k: v for k, v in sorted(in_dict.items(), key=lambda item: item[1], reverse=decreasing)}

def sortDictByValueMultiRules(in_dict:dict, decreasing: bool) -> dict:
    return {k: v for k, v in sorted(in_dict.items(), key=lambda item: (-item[1], item[0].lower()), reverse=decreasing)}

def sortDictByValueDecreasing(in_dict:dict) -> dict:
    return {k: v for k, v in sorted(in_dict.items(), key=lambda item: item[1], reverse=True)}

def calcCharFreqInStr(in_str: str) -> dict:
    frequencies = {}
    for char in in_str:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

def delAllOccurrencesFromList(in_list: List[str], val: str) -> list:
    return list(filter(lambda a: a != val, in_list))

def delCharsFromStr(to_be_deleted: list, in_str: str) -> str:
    final_string = ''
    for ch in in_str:
        if ch not in to_be_deleted:
            final_string += ch
    return final_string

def isSibling(x: str, y: str) -> bool:
    # y is x's sibling if y is any other combination of chars in x, but y is not identical to x
    if len(x) != len(y) or x == y:
        return False
    x = list(x)
    y = list(y)
    if set(x) != set(y):
        return False
    for i in set(x):
        if x.count(i) != y.count(i):
            return False
    return True

def getEvenAndOddDigits(in_str: str):
    even = []
    odd = []
    for i, v in enumerate(in_str):
        if i%2 ==0:
            even.append(v)
        else:
            odd.append(v)
    return [even, odd]

def cvt2Base16BitForm(char: str):
    # note that char is only one digit
    m = '0x' + char
    m16 = int(m, 16)
    hexBin = str(bin(m16))[2:]
    return hexBin.rjust(4, "0")

def cvtBase16Bin2deci(char: str):
    return str(hex(int("0b" + char, 2)))[2:]

def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

# calc combination number
def calcFactorial(n:int) ->int:
    # copyright: https: // blog.csdn.net / python_tty / java / article / details / 53115322
    # n 的阶乘
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return n * calcFactorial(n - 1)

def calcCombinationNum(n: int, m: int) -> int:
    # copyright: https: // blog.csdn.net / python_tty / java / article / details / 53115322
    # select from m items from n total items, how many combinations? (ignore sequence)
    if n==m:
        return 1
    first = calcFactorial(n)
    second = calcFactorial(m)
    third = calcFactorial((n - m))
    return first // (second * third)

def calcPermutationNum(n: int, m: int) -> int:
    first = calcFactorial(n)
    second = calcFactorial((n - m))
    return first // second

def getCombinations(list_items: list, num_select: int) -> list:
    # get all combinations when selecting "num_select" number of items from a list "list_items"
    return list(itertools.combinations(list_items, num_select))

def getPermutations(list_items: list, num_select: int) -> list:
    # get all permutations (sequences, sortings) when selecting "num_select" number of items from a list "list_items"
    return list(itertools.permutations(list_items, num_select))

def calculate(s):
    s=s.replace("+-","-").replace("--","+").replace("*-","a").replace("/-","b")
    if s[0]=="-":s="0"+s
    fu=re.findall(r"[*+-/ab]",s)[::-1]
    mum=list(map(int,re.split(r'[*+-/ab]',s)))[::-1]
    l,ll,lll=[],["+","-"],["*","/"]
    for i in range(len(fu)-1,-1,-1):
        if fu[i] =="a":
            mum.insert(i,-mum.pop(i+1)*mum.pop(i))
            del fu[i]
        elif fu[i] =="b":
            mum.insert(i,-mum.pop(i+1)/mum.pop(i))
            del fu[i]
        elif fu[i] =="*":
            mum.insert(i,mum.pop(i+1)*mum.pop(i))
            del fu[i]
        elif fu[i] =="/":
            mum.insert(i,mum.pop(i+1)/mum.pop(i))
            del fu[i]
    for i in range(len(fu)-1,-1,-1):
        if fu[i] =="+":mum.insert(i,mum.pop(i+1)+mum.pop(i))
        elif fu[i] =="-":mum.insert(i,mum.pop(i+1)-mum.pop(i))
    return str(int(mum[0]))

def fractionSplit(in_str: str):
    a = in_str.split('/')
    up = int(a[0])
    down = int(a[1])
    return up, down

def fractionStandardize(up: int, down: int)->str:
    return '1/' + str(down // (up - 1))

def fractionDecompose(up: int, down: int):
    res = ''
    while up != 1:
        if down % (up - 1) == 0:
            res = res + fractionStandardize(up, down) + '+'
            up = 1
        else:
            q = down // up
            res = res + '1/' + str(q + 1) + '+'
            up = up - down % up
            down = down * (q + 1)
            if down % up == 0:
                down = down // up
                up = 1
    res = res + '1/' + str(down)
    return res

def isPrimeNum(num: int) -> bool:
    i = 2
    while i <=  int(math.sqrt(num)):
        if num % i == 0:
            return False
        i+= 1
    return True