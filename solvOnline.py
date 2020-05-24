import utilities as util
import mySolPack
import unittest
import sys
import math

class myUnitTestSet(unittest.TestCase):
    @unittest.skip("passed")
    def testLastWordLen(self):
        self.assertEqual(mySolPack.findLenOfLastWord("Hello world"), 5)
        self.assertEqual(mySolPack.findLenOfLastWord("How are you"), 3)
        self.assertEqual(mySolPack.findLenOfLastWord("big b b b b bang"), 4)

    @unittest.skip("passed")
    def testRandmNumUniqAndSort(self):
        while True:
            try:
                num_of_elem = int(input())
                list_of_nums = []
                for i in range(num_of_elem):
                    curr_num = int(sys.stdin.readline()[:-1])
                    list_of_nums.append(curr_num)
                out_arr = mySolPack.randmArrayUniqueAndSort(list_of_nums)
                util.printArr(out_arr)
            except:
                break

    @unittest.skip("passed")
    def testSplitStringPer8(self):
        # 字符串分隔
        while True:
            try:
                strIn = input()
                if strIn is not "":
                    util.printArr(mySolPack.splitStrSpecLen(strIn, 5))
                else:
                    break
            except:
                break

    @unittest.skip("passed")
    def testcvtBase16(self):
        # 进制转换
        while True:
            try:
                strIn = input()
                print(int(strIn, base=16))
            except:
                break

    @unittest.skip("passed")
    def testCalcPrimeNum(self):
        # 质数因子
        while True:
            try:
                util.printArrWSep(mySolPack.calcPrimeNum(int(input())))
            except:
                break

    @unittest.skip("passed")
    def testCalNumOfDiffChar(self):
        # 字符个数统计
        print(mySolPack.calNumOfDiffChar(input()))

    @unittest.skip("passed")
    def testRevertStr(self):
        # 字符串反转
        print(mySolPack.reverseStr(input()))

    @unittest.skip("passed")
    def testSortedList(self):
        # 单词排序
        while True:
            try:
                num_of_words = int(input())
                inList = []
                for i in range(num_of_words):
                    inList.append(input())
                util.printArr(sorted(inList))
            except:
                break

    @unittest.skip("passed")
    def testIntegerStoreSpace(self):
        # int型正整数在内存中存储时1的个数
        outNum = 0
        inNum = int(input())
        while inNum > 1:
            outNum += inNum % 2
            inNum = int(inNum / 2)
        print(outNum + 1)

    @unittest.skip("gave up")
    def testshoppingList(self):
        # 购物单
        budget, num_of_items = [int(it) for it in input().split()]
        goods = []
        for i in range(num_of_items):
            goods.append([int(it) for it in input().split()])
        mySolPack.func_max(budget, num_of_items, goods)

    @unittest.skip("passed")
    def testMovCoord(self):
        # 坐标移动
        curr_coor = [0, 0]
        while True:
            try:
                line = sys.stdin.readline()
                inList = line.split(";")
                for inStr in inList:
                    # if re.compile("^[AWDS][1-9][0-9]?$").fullmatch(inStr) is not None:
                    if len(inStr) <= 3 and inStr[1:].isdecimal():
                        curr_coor = mySolPack.chgCoor(curr_coor, [inStr[0], int(inStr[1:])])
                print("{},{}".format(curr_coor[0], curr_coor[1]))
            except:
                break

    @unittest.skip("passed")
    def testIPCategorize(self):
        # 识别有效的IP地址和掩码并进行分类统计
        A = 0
        B = 0
        C = 0
        D = 0
        E = 0
        err = 0
        pri = 0
        while True:
            inStr = sys.stdin.readline().strip()
            if inStr == "":
                break
            list1 = inStr.split("~")[0]
            list2 = inStr.split("~")[1]
            ip = list1.split('.')
            ms = list2.split('.')
            # check ip
            if mySolPack.check_ip(ip) and mySolPack.isIPMask(ms):
                first_part = int(ip[0])
                sec_part = int(ip[1])
                if 1 <= first_part <= 126:
                    A += 1
                if 128 <= first_part <= 191:
                    B += 1
                if 192 <= first_part <= 223:
                    C += 1
                if 224 <= first_part <= 239:
                    D += 1
                if 240 <= first_part <= 255:
                    E += 1
                if int(ip[0]) == 10 or (int(ip[0]) == 172 and 15 < sec_part < 32) or (
                        first_part == 192 and sec_part == 168):
                    pri += 1
            else:
                err += 1
        print("%s %s %s %s %s %s %s" % (A, B, C, D, E, err, pri))

    @unittest.skip("passed")
    def testValidPassword(self):
        # 密码验证合格程序
        while True:
            try:
                pw_str = sys.stdin.readline().strip()
                if pw_str == "":
                    break
                # check if all rules satisfied
                if len(pw_str) > 8 and mySolPack.strHasCertainChar(pw_str) and mySolPack.hasRepiSubStr(pw_str, 2):
                    print('OK')
                else:
                    print('NG')
            except:
                break

    @unittest.skip("passed")
    def testCvtPassword(self):
        # 简单密码
        while True:
            real_pw = []
            try:
                in_str = sys.stdin.readline().strip()
                if in_str =="":
                    break
                for char in in_str:
                    if 'a'<= char <='z':
                        real_pw.append(mySolPack.cvtRulePhoneKeyboard(char))
                    elif 'A'<= char <='Z':
                        real_pw.append(mySolPack.cvtRuleShiftAlpha2Lower(char))
                    else:
                        real_pw.append(char)
                print(util.convertCharListToStr(real_pw))
            except:
                break

    @unittest.skip("passed")
    def testBottleExchgDrink(self):
        # 汽水瓶
        while True:
            try:
                a = int(input())
                if a != 0:
                    print(a // 2)
            except:
                break

    @unittest.skip("passed")
    def testDeleteRareChars(self):
        # 删除字符串中出现次数最少的字符
        try:
            while True:
                line = sys.stdin.readline().strip()
                if line == '':
                    break
                print(mySolPack.deleteRareCharsOnlineSolv(line))
        except:
            pass

    @unittest.skip("passed")
    def testLongestAcendingSubSet(self):
        # 合唱队
        while True:
            try:
                n = int(input())
                s = list(map(int, input().split()))
                pos_in_increasing = []
                pos_in_decreasing =[]
                pos_in_increasing = mySolPack.deal(s, pos_in_increasing) # traverse increasing order
                pos_in_decreasing= mySolPack.deal(s[::-1], pos_in_decreasing)[::-1] # traverse decreasing order
                num_people = max(pos_in_increasing[i] + pos_in_decreasing[i] for i in range(n))
                print(n-num_people+1)
            except:
                break

    @unittest.skip("passed")
    def testsortArr(self):
        #
        s = list(map(int, input().split()))
        sorted_increasing = mySolPack.randmArrayUniqueAndSort(s)
        pos_in_increasing = mySolPack.deal(s, [])  # traverse increasing order
        print("{} \t {}".format(sorted_increasing, pos_in_increasing))

    @unittest.skip("skipped, difficult and confusing")
    def testDataSetSorting(self):
        # 数据分类处理
        while True:
            try:
                arrI = input().split()[1:]
                arrR = map(str, sorted(map(int, set(input().split()[1:]))))
            except:
                break

    @unittest.skip("passed")
    def testsortStringThreeRules(self):
        # 字符串排序，三个规则
        while True:
            try:
                in_str = input()
                if in_str == '':
                    break
                print(mySolPack.sortStringThreeRules(in_str))
            except:
                break

    @unittest.skip("passed")
    def testAlphaDictionary(self):
        # 查找兄弟单词
        while True:
            try:
                line = input()
                if line == '':
                    break
                splitted = line.split()
                num_of_words = int(splitted[0])
                list_of_words = splitted[1:-2]
                word_to_look_up = splitted[-2]
                candidate_ind = int(splitted[-1])
                if num_of_words != len(list_of_words):
                    print("wrong num of words given in input")
                    break
                list_of_siblings = mySolPack.searchSiblingWords(list_of_words, word_to_look_up)
                print(len(list_of_siblings))
                # if result is non empty, in the result, print only the sibling at index specified
                if candidate_ind <= len(list_of_siblings):
                    print(list_of_siblings[candidate_ind-1])
            except:
                break

    @unittest.skip("passed")
    def testEncodeAndDecode(self):
        # 字符串加解密
        while True:
            try:
                line1 = input()
                if line1 == '':
                    break
                line2 = input()
                if line2 == '':
                    break
                encoded = []
                decoded = []
                for ch in line1:
                    encoded.append(mySolPack.encodeOrDecode(ch, True))
                for ch in line2:
                    decoded.append(mySolPack.encodeOrDecode(ch, False))
                print(util.convertCharListToStr(encoded))
                print(util.convertCharListToStr(decoded))
            except:
                break

    @unittest.skip("thought output should be all upper case, confusing. one case passed")
    def testCombiStrs(self):
        while True:
            try:
                line = input()
                if line == '':
                    break
                combi = util.convertCharListToStr(line.split())
                even, odd = [sorted(it) for it in util.getEvenAndOddDigits(combi)]
                combi = mySolPack.combiTwoStrsAtEvenOdd(even, odd)
                out = []
                for ch in list(combi):
                    out.append(util.cvtBase16Bin2deci(mySolPack.reverseStr(util.cvt2Base16BitForm(ch))).upper())
                print(mySolPack.convertCharListToStr(out))
            except:
                break

    @unittest.skip("passed")
    def testSnakeLayout(self):
        # 蛇形矩阵
        while True:
            try:
                n = int(input())
                row1 = [sum(range(i)) for i in range(1, n + 2)]
                col1 = [i + 1 for i in row1]
                for j in range(n):
                    col1 = [i - 1 for i in col1[1:]]
                    print(' '.join(map(str, col1)))
            except:
                break

    @unittest.skip("passed")
    def testFibonacci(self):
        while True:
            try:
                n = int(input())
                print(util.fibonacci(n))
            except:
                break

    @unittest.skip("passed")
    def testBouncing(self):
        while True:
            try:
                init_h = int(input())
                total = init_h
                for i in range(1, 5):
                    total += 2 * init_h * pow(0.5, i)
                res = float(init_h * pow(0.5, 5))
                print('%g' % total)
                print('%g' % res)
            # %f specify precision
            # %e scientific display num in 10^n
            # %g decide whether to use %e or %f format depending on the num, and keep only 6 digits
            except:
                break

    @unittest.skip("passed")
    def testMaze(self):
        # 迷宫问题
        while True:
            try:
                [a, b] = [int(i) for i in input().split()]
                maze_mat = []
                for i in range(a):
                    maze_mat.append([int(i) for i in input().split()])
                route = mySolPack.maze(num_rows=a, num_cols=b, mat = maze_mat)
                mySolPack.printCoord(route)
            except:
                break

    @unittest.skip("passed")
    def testCalcCombi(self):
        while True:
            try:
                num_of_names = int(input())
                if not num_of_names:break
                for i in range(num_of_names):
                    name = input().lower()
                    if not name.isalpha(): break
                    print(mySolPack.nameDiffWeightCombi(name))
            except:
                break

    @unittest.skip("passed")
    def testCutTextSpecDigits(self):
        while True:
            try:
                a, n = input().split()
                n = int(n)
                if a[n - 1].isalpha():
                    print(a[:n])
                else:
                    print(a[:n - 1])
            except:
                break

    @unittest.skip("skipped, need debugging for large input")
    def testlinearInterpolation(self):
        while True:
            try:
                ind_m, ind_n = [int(i) for i in input().split()]
                num_list = []
                for i in range(int(ind_m)):
                    x, y = [int(j) for j in input().split()]
                    if len(num_list) > 0:
                        if num_list[-1][0] == x:
                            continue
                        elif num_list[-1][0] + 1 < x:
                            num_list = mySolPack.linearInterp(x, y, num_list)
                            num_list.append([x, y])
                        else:
                            num_list.append([x, y])
                    else:
                        num_list.append([x, y])
                for number in num_list:
                    print(number[0], number[1])
            except:
                break

    @unittest.skip("passed")
    def testReadEnglishNumber(self):
        while True:
            try:
                num_to_read = int(input())
                print(mySolPack.readNum2English(num_to_read))
            except:
                break

    @unittest.skip("passed")
    def testWeightList(self):
        while True:
            try:
                n = int(input())
                list_of_weights = list(map(int, input().split()))
                list_of_amounts = list(map(int, input().split()))
                total_weight_list = [0]
                for i in range(n):
                    w_i = mySolPack.totalWeightOfOneWeight(list_of_weights[i], list_of_amounts[i])
                    total_weight_list = mySolPack.updateWeightList(total_weight_list, w_i)
                print(len(total_weight_list))
            except:
                break

    @unittest.skip("passed")
    def testCalcFundOperations(self):
        a = input()
        a = a.replace("{", "(")
        a = a.replace("}", ")")
        a = a.replace("[", "(")
        a = a.replace("]", ")")
        # print(util.calculate(a))
        print(int(eval(a)))

    @unittest.skip("passed")
    def testStringReplace(self):
        while True:
            try:
                short_str = input()
                long_str = input()
                list_of_long_str = list(long_str)
                flag = True
                for ch in list(short_str):
                    if ch not in list_of_long_str:
                        flag = False
                        break
                if not flag:
                    print("false")
                else:
                    print("true")
            except:
                break

    @unittest.skip("passed")
    def testFractionDecompose(self):
        while True:
            try:
                up, down = util.fractionSplit(input())
                print(util.fractionDecompose(up, down))
            except:
                break

    @unittest.skip("passed")
    def testCheckMatOverFlowAndOps(self):
        while True:
            try:
                r, c = list(map(int, sys.stdin.readline().strip().split()))
                max_size = 9
                res = []
                # size of two cells
                if r > max_size or c > max_size:
                    res.append(-1)
                else:
                    res.append(0)
                # row and col indices of two cells
                x1, y1= list(map(int, sys.stdin.readline().strip().split()))
                x2, y2 = list(map(int, sys.stdin.readline().strip().split()))
                if 0 <= x1 < r and 0 <= y1 < c and 0 <= x2 < r and 0 <= y2 < c:
                    res.append(0)
                else:
                    res.append(-1)
                # row index during insertion
                i_r = int(input())
                if 0 <= i_r < r:
                    res.append(0)
                else:
                    res.append(-1)
                # col index during insertion
                i_c = int(input())
                if 0 <= i_c < c:
                    res.append(0)
                else:
                    res.append(-1)
                # unit indices
                q_x, q_y = list(map(int, input().split()))
                if 0 <= q_x < r and 0 <= q_y < c:
                    res.append(0)
                else:
                    res.append(-1)
                for i in res:
                    print(i)
            except Exception as e:
                break

    @unittest.skip("passed")
    def testReplaceStr(self):
        while True:
            try:
                line_num = int(input())
                rules = {}
                for i in range(line_num):
                    key, replacement = mySolPack.str2ruleFormat(input())
                    rules[key] = replacement
                line_tbr = mySolPack.str2ruleFormat(input())
                tb_replaced = line_tbr[1]
                while mySolPack.findWordInRules(tb_replaced, rules):
                    tb_replaced = mySolPack.replaceItInListByList(tb_replaced, rules)
                # print("rules: {}".format(rules))
                final_str= ""
                for it in tb_replaced:
                    final_str += " {} /".format(it)
                print(line_tbr[0] + "="+ final_str[:-1])

            except:
                break

    @unittest.skip("passed, used online solve")
    def testCalcStrDist(self):
        while True:
            try:
                str1 = input()
                if str1 == "":
                    break
                str2 = input()
                # print(mySolPack.calcDistTwoStrs(str1, str2))
                print(mySolPack.calcDistTwoStrsOnline(str1, str2))
            except:
                break

    @unittest.skip("passed")
    def testCvtIP2BinInt(self):
        while True:
            try:
                in_ip = input()
                if in_ip == "":
                    break
                ip_int = int(input())
                list_parts = in_ip.split(".")
                bin_str = ""
                for it in list_parts:
                    bin_str += mySolPack.bin2specLen(mySolPack.cvtDec2Bin(int(it)), 8)
                print(mySolPack.cvtIPBinStr2int(bin_str))
                # part2
                list_parts2 = mySolPack.splitStrSpecLen(bin(ip_int)[2:], 8)
                final_str = ""
                for it in list_parts2:
                    final_str += str(int("0b"+it, 2)) +"."
                print(final_str[:-1])
            except:
                break

    @unittest.skip("passed")
    def testCheckIfTwoIPsInSameNet(self):
        while True:
            try:
                ip_mask = input()
                if ip_mask == "":
                    break
                ip_1 = input()
                ip_2 = input()
                if [mySolPack.check_ip(ip.split(".")) for ip in [ip_mask, ip_1, ip_2]] != [True, True, True] :
                    print("1")
                elif mySolPack.ipBinListAndOp(mySolPack.cvtIP2binList(ip_mask), mySolPack.cvtIP2binList(ip_1)) == mySolPack.ipBinListAndOp(mySolPack.cvtIP2binList(ip_mask), mySolPack.cvtIP2binList(ip_2)):
                    print("0")
                else:
                    print("2")
            except:
                break

    @unittest.skip("passed")
    def testfind7relatedInNumSet(self):
        while True:
            try:
                top_int = int(input())
                print(len(mySolPack.calcAll7relatedNums(top_int)))
            except:
                break

    @unittest.skip("passed")
    def testNamesVotesSort(self):
        while True:
            try:
                line = input()
                if line == "":
                    break
                names = line.split(",")
                print(mySolPack.namesVotesSort(names))
            except:
                break
    @unittest.skip("passed")
    def testSummationLongInt(self):
        while True:
            try:
                str1 = input()
                if str1 == "":
                    break
                str2 = input()
                print(int(str1) + int(str2))
            except:
                break
    @unittest.skip("passed")
    def testGetSmallestKNums(self):
        while True:
            try:
                total_num, k = [int(it) for it in input().split()]
                arr = [int(it) for it in input().split()]
                if len(arr) != total_num:
                    print("wrong num of int given")
                    break
                arr_final = [str(it) for it in sorted(arr)[:k]]
                print(" ".join(arr_final))
            except:
                break

    @unittest.skip("on hold")
    def testDrawPts(self):
        while True:
            try:
                total_num = int(input())
                list_pts = []
                for i in range(total_num):
                    list_pts.append(list(map(int, input().split())))
                print(list_pts)
            except:
                break
    @unittest.skip("passed")
    def testCalcCombiNumFromListStr(self):
        while True:
            try:
                in_str = input()
                if in_str == "":
                    break
                ls_ch = list(in_str)
                if len(ls_ch) >= 8:
                    print("given str is too long")
                    break
                print(len(set(util.getPermutations(list(ls_ch), len(ls_ch)))))
            except:
                break

    @unittest.skip("passed")
    def testCombiAndPermutationFormula(self):
        while True:
            try:
                innum = tuple(map(int, input().split()))
                print(util.calcPermutationNum(innum[0], innum[1]))
            except:
                break

    @unittest.skip("passed")
    def testFindCyclesInGraph(self):
        while True:
            try:
                in_str = input().split(";")
                if in_str == "" or []:
                    break
                list_edges = []
                for edge in in_str:
                    list_edges.append(mySolPack.str2edgeTuple(edge))
                for cycle in mySolPack.findCycleInDirectedGraph2(list_edges):
                    print(cycle)
                # detect if a graph is cyclic
                g = Graph(5)
                g.addEdge(0, 3)
                g.addEdge(0, 2)
                g.addEdge(3, 2)
                g.addEdge(2, 0)
                g.addEdge(1, 3)
                g.addEdge(2, 1)
                if g.isCyclic() == 1:
                    print("Graph is cyclic in nature")
                else:
                    print("Graph is non-cyclic in nature")
            except:
                break

    @unittest.skip("passed")
    def testCalcLogic(self):
        while True:
            try:
                in_str_ls = sys.stdin.readline().strip().split()
                str_ex = ""
                for ch in in_str_ls:
                    str_ex += ch
                print(mySolPack.logicCalculate(str_ex))
            except:
                break

    @unittest.skip("passed")
    def testFindSubGenestr(self):
        while True:
            try:
                in_str = input()
                if in_str == "":
                    break
                min_len_subgene = int(input())
                print(mySolPack.calcGCRatioInGene(in_str))
            except:
                break

    @unittest.skip("passed")
    def testSortStrs(self):
        while True:
            try:
                in_str = input().strip()
                inlist = [it.strip() for it in in_str.split(",")]
                if len(in_str) > 100:
                    break
                if inlist == [] or "":
                    break
                dict_str = {}
                for it in inlist:
                    dict_str[it] = ord(it[-1])
                sorted_dict = {k: v for k, v in sorted(dict_str.items(), key=lambda item: item[1], reverse=True)}
                final_str = ""
                for it in sorted_dict.items():
                    final_str += "," + it[0]
                print(final_str[1:])
            except:
                break

    # @unittest.skip("on hld")
    def testFormulaMinVal(self):
        while True:
            try:
                in_ls = list(map(int, sys.stdin.readline().strip().split()))
                if in_ls == [] or "":
                    break
                num_combi = set(util.getPermutations(in_ls, 3))
                val = math.inf
                for gr in num_combi:
                    curr_val = util.formula(gr[0], gr[1], gr[2])
                    if curr_val < val:
                        val = curr_val
                print(val)
            except:
                break

if __name__ == "__main__":
    unittest.main()