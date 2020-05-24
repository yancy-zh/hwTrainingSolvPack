import numpy as np
from mySub.utilities import LinkedList, minWithIndex, convertCharListToStr, getFileNameLast16, calcCharFreqInStr, sortDictByValue, delAllOccurrencesFromList, delCharsFromStr
import mySub.utilities as util
from typing import List
import math
import bisect
import networkx as nx

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

   """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    sum = 0
    indices = np.arange(len(nums))
    for i in np.arange(len(nums)):
        x = nums[i]
        y = target -x
        remainInd = indices.tolist()
        remainInd.remove(i)
        for j in remainInd:
            if nums[j] == y:
                return [i, j]

def ReverseIntWORepetition(inInt: int) -> int:
    return int(reduceCharacters(str(reverseInt(inInt))))

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    palindrome is an int that is identical to its reversed form
    """
    if x < 0:
        return False
    if reverseInt(x) == x:
        return True
    else:
        return False

def commonPrefix(left:str, right:str) -> str:
    minLen = min(left.__len__(), right.__len__())
    for i in np.arange(minLen):
        if (left[i] != right[i]):
            return left[:i]
    return left[:minLen]

def longestCommonPrefix(strs: List[str]) -> str:
    if strs == None or strs.__len__()==0:
        return ""
    return __longestCommonPrefix(strs, 0, strs.__len__()-1)

def __longestCommonPrefix(strs:List[str], l:int, r:int) -> str:
    if l==r:
        return strs[l]
    else:
        mid = np.divmod(l +r, 2)[0]
        lcpLeft = __longestCommonPrefix(strs, l, mid)
        lcpRight = __longestCommonPrefix(strs, mid + 1, r)
        return commonPrefix(lcpLeft, lcpRight)

def isValid(s: str) -> bool:
    # The stack to keep track of opening brackets
    stack = []
    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(",
               "}": "{",
               "]": "["}

    # For every bracket in the expression.
    for char in s:
        # If the character is an closing bracket
        if char in mapping:
            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # we have an opening bracket, simply push it onto the stack
            stack.append(char)
    # the input string contains valid parenthesis if the stack is empty
    return not stack

def numJewelsInStones(J: str, S: str) -> int:
    # check how many stones are also Jewelries
    counter = 0
    for i in S:
        counter += 1 if i in J else 0
    return counter

def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    num_of_rows = matrix.__len__()
    lucky_numbers = []
    lucky_vals = []
    non_lucky_numbers = []
    for row_ind in range(0, num_of_rows):
        curr_row = matrix[row_ind]
        # get the min of each row
        tuple_min= minWithIndex(curr_row)
        lucky_numbers.append(tuple_min)
    print("mins of rows is: {}".format(lucky_numbers))

    for tuple_it in lucky_numbers:
        for row_ind in range(0, num_of_rows):
            curr_row = matrix[row_ind]
            # get element at specific index where lucky number locates
            if curr_row[tuple_it[0]] > tuple_it[1]:
                # this element can not be a lucky number because another element in the same column is larger
                # exclude this tuple from list of candidate lucky numbers
                non_lucky_numbers.append(tuple_it)
                break

    # whatever tuple that is in the list "lucky_numbers" but not in the list "non_lucky_numbers" should be the final
    # set of lucky numbers
    for lucky in lucky_numbers:
        if lucky not in non_lucky_numbers:
            lucky_vals.append(lucky[1])
    print("lucky number set is: {}".format(lucky_vals))
    return lucky_vals

def reverse(inSentence: str)-> str:
    outList = []
    splited = inSentence.split(' ')
    for i in list(range(splited.__len__()-1, -1, -1)):
        outList.append(splited[i])
        outList.append(" ")
    return convertCharListToStr(outList)[:-1]

def getEvenDigitsNumbers(nums: List[int]) -> int:
    out_list_of_numbers = []
    for i in range(nums.__len__()):
        if len(str(nums[i])) % 2 == 0:
            out_list_of_numbers.append(nums[i])
    return len(out_list_of_numbers)

def maxSubArray(nums: List[int]) -> int:
    max_sum = -math.inf
    if nums.__len__() < 1:
        return -1
    if nums.__len__() == 1:
        max_sum = nums[0]
    else:
        for i in range(0, nums.__len__()):
            for j in range(i+1, nums.__len__()+1):
                print("current sum at [{}, {}] is:{}".format(i, j, sum(nums[i:j])))
                if sum(nums[i:j]) > max_sum:
                    max_sum = sum(nums[i:j])
    return max_sum

def simpleErrorRecorder():
    hashmap = {}
    err_list = []
    while True:
        input_str = input()
        if input_str == '':
            break
        # extract file name, err line number from a string
        temp = input_str.split()
        # the first element of the list is the file name, note that only the last 16 digits of the file name is recorded
        # the second element of the list is the line number
        record_key = "{} {}".format(getFileNameLast16(temp[0]), int(temp[1]))
        if record_key not in hashmap:
            hashmap[record_key] = 1
            err_list.append(record_key)
        else:
            hashmap[record_key] += 1
    for it in err_list[-8:]:
        print("{} {}".format(it, hashmap[it]))

def findLenOfLastWord(word: str):
    splitted = word.split(" ")
    return len(splitted[-1])

"""
functions that support the solutions 
"""
def reduceCharacters(inStr: str) -> str:
    stack = []
    for i in range(inStr.__len__()):
        # print("idx: {} val: {}".format(i, inStr[i]))
        if stack is not None and inStr[i] not in stack:
            stack.append(inStr[i])
    return convertCharListToStr(stack)

def reverseInt(x):
    rev = 0
    TAG_NEG = 0
    if x < 0:
        x = abs(x)
        TAG_NEG = 1
    INT_MAX = pow(2, 31) - 1
    INT_MIN = -pow(2, 31)
    while x != 0:
        # pop operation
        pop = x % 10
        x = divmod(x, 10)[0]
        if rev > INT_MAX/10 or (rev == INT_MAX/10 and pop > 7):
            return 0
        if rev < INT_MIN/10 or (rev == INT_MIN/10 and pop < -8):
            return 0
        rev = rev * 10 + pop
    if TAG_NEG == 1:
        rev = -rev
    return rev

def reverseIntWOSign(inInt: int) -> str:
    rev = 0
    INT_MAX = pow(2, 31) - 1
    len_of_int = str(inInt).__len__()
    while inInt != 0:
        # pop operation
        pop = inInt % 10
        inInt = divmod(inInt, 10)[0]
        if rev > INT_MAX/10 or (rev == INT_MAX/10 and pop > 7):
            return "out of bound"
        rev = rev * 10 + pop
    # add 0 to the beginning of the integer
    if str(rev).__len__() < len_of_int:
        rev_str = str(rev).zfill(len_of_int)
    else:
        rev_str = str(rev)
    return rev_str

def rmDuplicatesFromSortedArray(nums: List[int]) -> int:
    i = 0
    while i < nums.__len__():
        # record if value at i equals value at j
        j = i + 1
        while nums[i] == nums[j]:
            j += 1
    return i

def randmArrayUniqueAndSort(arr_of_num: list) -> list:
    return sorted(list(set(arr_of_num)))

def splitStrSpecLen(strIn:str, specLen: int) -> list:
    len_of_str = len(strIn)
    quotient = int(len_of_str / specLen)
    if len_of_str % specLen != 0:
        strIn = strIn.rjust(int((quotient + 1) * specLen), '0') #pad zeros to the left if length not satisfied
        return [strIn[i: i + specLen] for i in range(0, len(strIn), specLen)]
    else:
        return [strIn[i: i+specLen] for i in range(0, len(strIn), specLen)]

def calcPrimeNum(inNum: int) -> list:
    arr_of_prime_num = []
    i = 2
    while inNum !=1:
        if inNum % i == 0:
            arr_of_prime_num.append(i)
            inNum = int(inNum / i)
        else:
            i += 1
    return arr_of_prime_num

def calNumOfDiffChar(inStr: str) -> int:
    charList = list(inStr)
    return len(set(charList))

def reverseStr(inStr: str)->str:
    outStr = ""
    list_of_str = list(inStr)
    for i in range(len(list_of_str)-1, -1, -1):
        outStr = outStr + list_of_str[i]
    return outStr

def cvtDec2Bin(inNum: int):
    return str(bin(inNum))[2:]

def bin2specLen(bin: str, len: int):
    return bin.rjust(len, "0")

def func_max(N, m, goods):
    a = [[0] * (N + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, N + 1):
            if goods[i - 1][0] <= j:  # if price leq j
                a[i][j] = max(a[i - 1][j], a[i - 1][j - goods[i - 1][0]] + goods[i - 1][0] * goods[i - 1][1])
    print(int(a[m][N]))

def chgCoor(last_coor: list, coor_pair: list) -> list:
    if coor_pair[0] == "A":
        last_coor[0] -= coor_pair[1]
    elif coor_pair[0] == "D":
        last_coor[0] += coor_pair[1]
    elif coor_pair[0] == "S":
        last_coor[1] -= coor_pair[1]
    elif coor_pair[0] == "W":
        last_coor[1] += coor_pair[1]
    return last_coor

def isIPMask(ip: list)-> bool:
    validms = ['254', '252', '248', '240', '224', '192', '128', '0']  # 8bit
    #valid mask is the ip that after converted to binary, pad in zeros on the left and shows: continous 1s followed by zeros
    if len(ip) != 4:
        return False
    if ip[0] == '255':
        if ip[1] == '255':
            if ip[2] == '255':
                if ip[3] in validms:
                    return True
                else:
                    return False
            elif ip[2] in validms and ip[3] == '0':
                return True
            else:
                return False
        elif ip[1] in validms and ip[2] == ip[3] == '0':
            return True
        else:
            return False
    elif ip[0] in validms and ip[1] == ip[2] == ip[3] == '0':
        return True
    else:
        return False

def check_ip(ip:list):  # check if ip is valid
    if len(ip) != 4 or '' in ip:
        return False
    for i in ip:
        if int(i) < 0 or int(i) > 255:
            return False
    return True

def strHasCertainChar(in_str: str) -> bool:
    chars= list(in_str)
    num_lower = 0
    num_upper = 0
    num_numeric = 0
    num_spec = 0
    for char in chars:
        if 'a'<=char<='z' :
            num_lower=1
        elif 'A'<=char<='Z':
            num_upper=1
        elif '0'<=char<='9':
            num_numeric=1
        else:
            num_spec=1
    if (num_lower + num_upper + num_numeric + num_spec) >= 3:
        return True
    else:
        return False

def hasRepiSubStr(in_str: str, len_of_sub: int)-> bool:
    for i in range((len(in_str) - (len_of_sub+1))):
        if in_str[i:i + len_of_sub+1] in in_str[i + 1:]:
            return False
    return True

def cvtRuleShiftAlpha2Lower(charUpper: str) -> str:
    if charUpper != "Z":
        return chr(ord(charUpper.lower()) + 1)
    else:
        return "a"

def cvtRuleShiftAlphaSwitchCase(char: str, isEncode: bool) -> str:
    if isEncode:
        if char.islower():
            if char != "z":
                return chr(ord(char)+1).upper()
            else:
                return "A"
        else:
            if char != "Z":
                return chr(ord(char)+1).lower()
            else:
                return "a"
    else:
        if char.islower():
            if char != "a":
                return chr(ord(char)-1).upper()
            else:
                return "Z"
        else:
            if char != "A":
                return chr(ord(char)-1).lower()
            else:
                return "z"

def cvtRuleShiftNum(char: str, isEncode: bool) -> str:
    if isEncode:
        if char != "9":
            return chr(ord(char)+1)
        else:
            return "0"
    else:
        if char != "0":
            return chr(ord(char)-1)
        else:
            return "9"

def sortStrByLowercase(in_str: list) -> list:
    in_str.sort(key = lambda x:x.lower())
    return in_str

def cvtRulePhoneKeyboard(charLower:str) -> str:
    if charLower in 'abc':
        return '2'
    elif charLower in 'def':
        return '3'
    elif charLower in 'ghi':
        return '4'
    elif charLower in 'jkl':
        return '5'
    elif charLower in 'mno':
        return '6'
    elif charLower in 'pqrs':
        return '7'
    elif charLower in 'tuv':
        return '8'
    elif charLower in 'wxyz':
        return '9'

def deleteRareChars(in_str: str) -> str:
    chars_freq_hashmap = calcCharFreqInStr(in_str)
    sorted_hashmap = sortDictByValue(chars_freq_hashmap, False)
    min_freq = min(sorted_hashmap.values())
    in_list_of_char = list(in_str)
    for k, v in sorted_hashmap.items():
        if v == min_freq:
            in_list_of_char = delAllOccurrencesFromList(in_list_of_char, val=k)
        else:
            break
    return convertCharListToStr(in_list_of_char)

def deleteRareCharsOnlineSolv(in_str: str) -> str:
    chars_freq_hashmap = calcCharFreqInStr(in_str)
    sorted_hashmap = sortDictByValue(chars_freq_hashmap, False)
    min_num = min(sorted_hashmap.values())
    to_delete_char = list()
    for k in sorted_hashmap.keys():
        if sorted_hashmap[k] == min_num:
            to_delete_char.append(k)
    return delCharsFromStr(to_delete_char, in_str= in_str)

def deal(l,res):
    b = [9999]*len(l)
    b[0] = l[0]
    res.append(1)
    for i in range(1,len(l)):
        pos = bisect.bisect_left(b,l[i])
        res.append(pos+1)
        b[pos]=l[i]
    return res

def DataSetSorting(num: str, list_to_comp: list):
    singleRes, count = "", 0
    totalNum = 0
    remaining_elems = ""
    for i, v in enumerate(list_to_comp):
        if num in v:
            singleRes += str(i) + " " + v + " "
            totalNum += 2
            count += 1
    if count:
        singleRes = num + " " + str(count) + " " + singleRes
        totalNum += 2
    remaining_elems += singleRes
    return totalNum, remaining_elems

def sortStringThreeRules(in_str: str) -> str:
    # rule 1&2: alphabetic order, keep ori order if both lower and upper present
    alpha_list = []
    non_alpha = [0] * len(in_str)
    for i, v in enumerate(in_str):
        if v.isalpha():
            alpha_list.append(v)
        else:
            non_alpha[i] = v
    alpha_list = sortStrByLowercase(alpha_list)
    for i, v in enumerate(non_alpha):
        if not v: # empty char means space saved for alphas
            non_alpha[i] = alpha_list[0] # insert alpha char keeping original seq
            alpha_list.pop(0)
    return convertCharListToStr(non_alpha)

def searchSiblingWords(word_list: list, word_to_look_up: str) -> list:
    result = []
    for word in word_list:
        if util.isSibling(word_to_look_up, word):
            result.append(word)
    return sorted(result)

def encodeOrDecode(in_str: str, flag: bool) -> str:
    if in_str.isalpha():
        return cvtRuleShiftAlphaSwitchCase(in_str, flag)
    elif in_str.isdigit():
        return cvtRuleShiftNum(in_str, flag)
    else:
        return in_str

def combiTwoStrsAtEvenOdd(even: list, odd: list) -> str:
    s=""
    if len(even) != len(odd):
        raise Exception("Two strings have diff length!")
    for i in range(len(even)*2):
        if i%2 ==0:
            s+= even[0]
            even.pop(0)
        else:
            s+= odd[0]
            odd.pop(0)
    return s

def ballBoucing():
    while True:
        try:
            n = int(input())
            total = n
            for i in range(1, 5):
                total += 2 * n * (0.5) ** i
            res = float(n * (0.5) ** 5)
            print('%g' % total)
            print('%g' % res)
        # %f 格式化定点数，可指定精度
        # %e 科学计数法计数
        # %g 根据值的大小采用%e或%f，但最多保留6位有效数字
        except:
            break

def printCoord(LU):
    for i in LU:
        print('(%d,%d)' % (i[0], i[1]))

def maze(num_rows, num_cols, mat):
    v = [[0 for i in range(num_cols)] for j in range(num_rows)]  # visiting record, a mat that has the same size of input.
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # directions: down, up, left, right
    c = [1, 1, 3, 0]  # cost
    steps = []  # step
    steps.append([0, 0])  # begin at (0,0)
    v[0][0] = 1  # (0,0)has been visited
    i, j = steps[-1]  # init position
    k = 0
    while k < 4: # trying four directions
        x = i + direction[k][0] # x coordinate
        y = j + direction[k][1] # y coordinate
        if x >= 0 and y >= 0 and x < num_rows and y < num_cols and mat[x][y] == 0 and v[x][y] == 0: # coordinates doesn't go over the net
            steps.append([x, y])
            v[x][y] = 1
            i = x
            j = y
            k = -1
        if x == num_rows - 1 and y == num_cols - 1: # coordinates reach the borders
            break
        if k == 3:
            steps.pop() # get the next step
        k += 1 # try the next direction
    return steps

def nameDiffWeightCombi(name: str):
    # calc biggest combi of total weight in a alpha str, where each char has a diff weight
    result = 0
    c = set(list(name))
    d = []
    for j in c:
        d.append(name.count(j))
    d.sort(reverse=True)
    for k in range(len(d)):
        result = result + d[k] * (26 - k)
    return result

def linearInterp(x, y, num_list):
    # num_list each item [x, y] stores values, [x y].
    # last_y, y are values of the second point. last_x , x are indices
    last_x, last_y = num_list[-1][0], num_list[-1][1]
    step = math.trunc((y-last_y)/(x-last_x))
    for num in range(1, x - last_x):
        # insert into the data set the interpolated values
        num_list.append([last_x + num, last_y + step * num])
    return num_list

def cvtNum2English(n):
    m1 = 'one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
    m2 = 'twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')
    if(n<20):
        return m1[n-1:n]
    if(n<100):
        return [m2[n//10-2]] + cvtNum2English(n % 10)
    if(n<1000):
        return [m1[n//100-1]] + ['hundred'] + ['and'] + cvtNum2English(n % 100)
    else:
        for w,p in enumerate(('thousand','million','billion'),1):
            if(n<1000**(w+1)):
                return cvtNum2English(n // (1000 ** w)) + [p] + cvtNum2English(n % 1000 ** w)

def readNum2English(num: int):
    return ' '.join(cvtNum2English(num)) or "zero"

def totalWeightOfOneWeight(weight: int, numOfWeight: int) -> list:
    return [weight * n for n in range(numOfWeight + 1)]

def updateWeightList(weightList: list, weight_list_of_newWeight:list) -> list:
    return list(set([a+b for a in weight_list_of_newWeight for b in weightList]))

def str2ruleFormat(in_str: str):
    key = in_str.split("=")[0].strip()
    replacement = [delCharsFromStr(["&", "{", "}"], it).strip() for it in in_str.split("=")[1].split("/")]
    return key, replacement

def replaceItInListByList(tb_replaced: list, rules: dict) -> list:
    new_list = []
    for word in tb_replaced:
        if word in rules.keys():
            new_list.extend(rules[word])
        else:
            new_list.append(word)
    return new_list

def findWordInRules(tb_replaced: list, rules: dict) -> bool:
    flag = False
    for word in tb_replaced:
        if word in rules.keys():
            flag = True
            break
    return flag

def getCommonSubStr(str1: str, str2: str) -> tuple:
    n = 0 # common str length
    common = ""
    for i in range(len(str1)):
        if str1[i - n:i + 1] in str2:
            common = str1[i - n:i + 1]
            n += 1
    return n, common

def calcDistTwoStrs(str1: str, str2: str)-> int:
    n, common = getCommonSubStr(str1, str2)
    if str1 in str2 or str2 in str1:
        return abs(len(str1) - len(str2))
    else:
        return len(str1) + len(str2) - 2 * n

def calcDistTwoStrsOnline(a,b):
    m, n = len(a),len(b)
    dp = list(range(n+1))
    for i in range(1,m+1):
        pre = dp[:]
        dp[0] = i
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                dp[j] = pre[j-1]
            else:
                dp[j] = min(pre[j],dp[j-1],pre[j-1])+1
    return dp[-1]

def cvtIPBinStr2int(ipBinStr: str) -> int:
    return int("0b" + ipBinStr, base=2)

def cvtIP2binList(ip_str: str) -> list:
    list_parts = ip_str.split(".")
    list_bins = []
    for it in list_parts:
        list_bins.append(bin2specLen(cvtDec2Bin(int(it)), 8))
    return list_bins

def binStrAnd(bin_str1: str, bin_str2: str) -> str:
    if len(bin_str1) != len(bin_str2):
        return "strs len not equal"
    res = ""
    for i in range(len(bin_str1)):
        res += str(int(bin_str1[i]) & int(bin_str2[i]))
    return res

def ipBinListAndOp(list_bin_1: list, list_bin_2: list) -> list:
    res = []
    for i in range(4):
        res.append(binStrAnd(list_bin_1[i], list_bin_2[i]))
    return res

def checkIsNum7Related(num: int) -> bool:
    if "7" in str(num):
        return True
    elif num == 0:
        return False
    elif num % 7 == 0:
        return True
    else:
        return False

def calcAll7relatedNums(top_int: int) -> list:
    list_7related = []
    for it in range(top_int+1):
        if checkIsNum7Related(it):
            list_7related.append(it)
    return list_7related

def namesVotesSort(names: list) -> str:
    votes = {}
    has_err = False
    for name in names:
        if name.isalpha() and name[0].isupper() and name[1:].islower():
            if name in votes:
                votes[name] += 1
            else:
                votes[name] = 1
        else:
            has_err=True
            break
    if has_err:
        return "error.0001"
    votes = util.sortDictByValueMultiRules(votes, False)
    return list(votes.keys())[0]

# travellers, bees problem, num of cycles
def findCycleInDirectedGraph1(list_nodes: list, list_edges: list):
    # Create Directed Graph
    gr = nx.DiGraph()
    # Add a list of nodes:
    gr.add_nodes_from(list_nodes)
    # Add a list of edges:
    gr.add_edges_from(list_edges)
    # Return a list of cycles described as a list of nodes
    return list(nx.simple_cycles(gr))

def findCycleInDirectedGraph2(list_edges: list):
    # edges = [('A', 'B'),('C', 'D'),('D', 'C'),('C', 'D')]
    G = nx.DiGraph(list_edges)
    return nx.simple_cycles(G)

def str2edgeTuple(in_str: str) -> tuple:
    pure_str = in_str.strip()
    return tuple([pure_str[0].strip(), pure_str[-1].strip()])

def logicCalculate(in_str: str) -> str:
    # 原文链接：https: // blog.csdn.net / qq_41586251 / java / article / details / 105373806
    k = 0
    while len(in_str) != 1:
        in_str = in_str.replace('!1', '0')
        in_str = in_str.replace('!0', '1')

        in_str = in_str.replace('1&0', '0')
        in_str = in_str.replace('0&1', '0')
        in_str = in_str.replace('1&1', '1')
        in_str = in_str.replace('0&0', '0')

        in_str = in_str.replace('1|1', '1')
        in_str = in_str.replace('0|1', '1')
        in_str = in_str.replace('1|0', '1')
        in_str = in_str.replace('0|0', '0')

        in_str = in_str.replace('(1)', '1')
        in_str = in_str.replace('(0)', '0')
        k += 1
        if k > 20:
            break
    return in_str

def calcFreqOfChar(in_str: str, ch: str) -> int:
    cnt = 0
    for it in in_str:
        if it == ch:
            cnt+=1
    return cnt

def calcGCRatioInGene(in_str: str):
    frequencies = {"G": 0 , "C": 0}
    for key in frequencies.keys():
        frequencies[key] = calcFreqOfChar(in_str, key)
    part1 = sum(frequencies.values())
    return part1/len(in_str)
