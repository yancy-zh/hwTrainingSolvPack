import utilities as util
import mySolPack
import unittest
import sys
from mySub.findCycleInDirectedGraph import Graph
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
        '''
         •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
        •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
        输入描述:
        连续输入字符串(输入2次,每个字符串长度小于100)
        输出描述:
        输出到长度为8的新字符串数组
        input:
        abc
        123456789
        output:
        abc00000
        12345678
        90000000
        '''
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
        '''
         写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）
        输入描述:
        输入一个十六进制的数值字符串。
        输出描述:
        输出该数值的十进制字符串。
        input:
        0xA
        output:
        10
        '''
        while True:
            try:
                strIn = input()
                print(int(strIn, base=16))
            except:
                break

    @unittest.skip("passed")
    def testCalcPrimeNum(self):
        # 质数因子
        '''
         功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
        最后一个数后面也要有空格
        输入描述:
        输入一个long型整数
        输出描述:
        按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
        input:
        180
        output:
        2 2 3 3 5
        '''
        while True:
            try:
                util.printArrWSep(mySolPack.calcPrimeNum(int(input())))
            except:
                break

    @unittest.skip("passed")
    def testCalNumOfDiffChar(self):
        # 字符个数统计
        '''
        编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。注意是不同的字符
        输入描述:
        输入N个字符，字符在ACSII码范围内。
        输出描述:
        输出范围在(0~127)字符的个数。
        input:
        abc
        output:
        3
        '''
        print(mySolPack.calNumOfDiffChar(input()))

    @unittest.skip("passed")
    def testRevertStr(self):
        # 字符串反转
        '''
        写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
        输入描述:
        输入N个字符
        输出描述:
        输出该字符串反转后的字符串
        '''
        print(mySolPack.reverseStr(input()))

    @unittest.skip("passed")
    def testSortedList(self):
        # 单词排序
        '''
        input:
        输入一行以空格来分隔的句子
        output:
        按字母表顺序排序
        '''
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
        '''
        输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
        输入描述:
        输入一个整数（int类型）
        输出描述:
        这个数转换成2进制后，输出1的个数
        input:
        5
        out:
        2
        '''
        outNum = 0
        inNum = int(input())
        while inNum > 1:
            outNum += inNum % 2
            inNum = int(inNum / 2)
        print(outNum + 1)

    @unittest.skip("gave up")
    def testshoppingList(self):
        # 购物单
        '''
        输入的第 1 行，为两个正整数，用一个空格隔开：N m
        （其中 N （ <32000 ）表示总钱数， m （ <60 ）为希望购买物品的个数。）
        从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q
        （其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
        1000 5
        800 2 0
        400 5 1
        300 5 1
        400 3 0
        500 2 0
        '''
        budget, num_of_items = [int(it) for it in input().split()]
        goods = []
        for i in range(num_of_items):
            goods.append([int(it) for it in input().split()])
        mySolPack.func_max(budget, num_of_items, goods)

    @unittest.skip("passed")
    def testMovCoord(self):
        # 坐标移动
        '''
         开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
        输入：
        合法坐标为A(或者D或者W或者S) + 数字（两位以内）
        坐标之间以;分隔。
        非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
        下面是一个简单的例子 如：
        A10;S20;W10;D30;X;A1A;B10A11;;A10;
        处理过程：
        起点（0,0）
        +   A10   =  （-10,0）
        +   S20   =  (-10,-20)
        +   W10  =  (-10,-10)
        +   D30  =  (20,-10)
        +   x    =  无效
        +   A1A   =  无效
        +   B10A11   =  无效
        +  一个空 不影响
        +   A10  =  (10,-10)
        结果 （10， -10）
        input:
        A10;S20;W10;D30;X;A1A;B10A11;;A10;
        output:
        10,-10
        '''
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
        '''
        请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。  所有的IP地址划分为 A,B,C,D,E
        五类  A类地址1.0.0.0~126.255.255.255;  B类地址128.0.0.0~191.255.255.255;  C类地址192.0.0.0~223.255.255.255;  D类地址
        224.0.0.0~239.255.255.255；  E类地址240.0.0.0~255.255.255.255   私网IP范围是：  10.0.0.0～10.255.255.255  172.16.0.0～172.31.255.255
         192.168.0.0～192.168.255.255  子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
         注意二进制下全是1或者全是0均为非法  注意： 1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，
         计数时可以忽略 2. 私有IP地址和A,B,C,D,E类地址是不冲突的   输入描述:  多行字符串。每行一个IP地址和掩码，用~隔开。  输出描述:
         统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
        '''
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
        '''
        密码要求:
        1.长度超过8位
        2.包括大小写字母.数字.其它符号,以上四种至少三种
        3.不能有相同长度超2的子串重复
        说明:长度超过2的子串
        输入描述:
        一组或多组长度超过2的子符串。每组占一行
        输出描述:
        如果符合要求输出：OK，否则输出NG
        input:
        021Abc9000
        021Abc9Abc1
        021ABC9000
        021$bc9000
        output:
        OK
        NG
        NG
        OK
        '''
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
        '''
         密码是我们生活中非常重要的东东，我们的那么一点不能说的秘密就全靠它了。哇哈哈. 接下来渊子要在密码之上再加一套密码，虽然简单但也安全。
        假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，他通过一种算法把这个密码变换成YUANzhi1987，这个密码是他的名字和出生年份，怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。
        他是这么变换的，大家都知道手机上的字母： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，
        声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。
        输入描述:
        输入包括多个测试数据。输入是一个明文，密码长度不超过100个字符，输入直到文件结尾
        输出描述:
        输出渊子真正的密文
        input:
        YUANzhi1987
        output:
        zvbo9441987
        '''
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
        '''
         有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？
        输入描述:
        输入文件最多包含10组测试数据，每个数据占一行，仅包含一个正整数n（1<=n<=100），表示小张手上的空汽水瓶数。n=0表示输入结束，你的程序不应当处理这一行。
        输出描述:
        对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。
        in:
        3
        10
        81
        0
        :return:
        1
        5
        40
        '''
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
        '''
         实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
        注意每个输入文件有多组输入，即多个字符串用回车隔开
        输入描述:
        字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。
        输出描述:
        删除字符串中出现次数最少的字符后的字符串。
        input:
        abcdd
        :return:
        dd
        '''
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
        '''
         计算最少出列多少位同学，使得剩下的同学排成合唱队形
        说明：
        N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
        合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，   则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。
        你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
        注意不允许改变队列元素的先后顺序
        请注意处理多组输入输出！
        输入描述:
        整数N
        输出描述:
        最少需要几位同学出列
        input:
        8
        186 186 150 200 160 130 197 200
        :return:
        4
        '''
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
        '''
         编写一个程序，将输入字符串中的字符按如下规则排序。
        规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
        如，输入： Type 输出： epTy
        规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
        如，输入： BabA 输出： aABb
        规则 3 ：非英文字母的其它字符保持原来的位置。
        如，输入： By?e 输出： Be?y
        input:
        A Famous Saying: Much Ado About Nothing (2012/8).
        :return:
        A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
        '''
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
        '''
        输入描述:
        先输入字典中单词的个数，再输入n个单词作为字典单词。
        输入一个单词，查找其在字典中兄弟单词的个数
        再输入数字n
        输出描述:
        根据输入，输出查找到的兄弟单词的个数
        input:
        3 abc bca cab abc 1
        :return:
        2
        bca
        '''
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
        '''
        1、对输入的字符串进行加解密，并输出。
        2加密方法为：
        当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
        当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
        其他字符不做变化。
        3、解密方法为加密的逆过程。
        接口描述：
            实现接口，每个接口实现1个基本操作：
        void Encrypt (char aucPassword[], char aucResult[])：在该函数中实现字符串加密并输出
        说明：
        1、字符串以\0结尾。
        2、字符串最长100个字符。
        int unEncrypt (char result[], char password[])：在该函数中实现字符串解密并输出
        说明：
        1、字符串以\0结尾。
            2、字符串最长100个字符。
        输入描述:
        输入说明
        输入一串要加密的密码
        输入一串加过密的密码
        输出描述:
        输出说明
        输出加密后的字符
        输出解密后的字符
        '''
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
        # 字符串合并处理
        '''
         详细描述：
        将输入的两个字符串合并。
        对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标意思是字符在字符串中的位置。
        对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，则对他们所代表的16进制的数进行BIT倒序的操作，并
        转换为相应的大写字符。如字符为‘4’，为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’； 如字符为‘7’，为0111b，则翻转
        后为1110b，也就是e。转换后的字符为大写‘E’。
        in:
        dec fab
        :return:
        5D37BF
        '''
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
        '''
        蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
        样例输入/input
        5
        样例输出/output
        1 3 6 10 15
        2 5 9 14
        4 8 13
        7 12
        11
        '''
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
    def testBallBouncing(self):
        # 求小球落地5次后所经历的路程和第5次反弹的高度
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
        # 名字的漂亮度
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
        # 按字节截取字符串
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
        # 线性插值
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
        # 学英语
        while True:
            try:
                num_to_read = int(input())
                print(mySolPack.readNum2English(num_to_read))
            except:
                break

    @unittest.skip("passed")
    def testWeightList(self):
        # 称砝码
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
        # 四则运算，表达式求值
        a = input()
        a = a.replace("{", "(")
        a = a.replace("}", ")")
        a = a.replace("[", "(")
        a = a.replace("]", ")")
        # print(util.calculate(a))
        print(int(eval(a)))

    @unittest.skip("passed")
    def testStringReplace(self):
        # 字符串是另一个字符串的子串
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
        # 将真分数分解为埃及分数
        while True:
            try:
                up, down = util.fractionSplit(input())
                print(util.fractionDecompose(up, down))
            except:
                break

    @unittest.skip("passed")
    def testCheckMatOverFlowAndOps(self):
        # 二维数组操作
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
        '''
        输入一组数量为n的字符串，格式是“字符串名 = 字符串值”，字符串值中可能包含
        "&{字符串名}“的子串，需要用同一字符串名的字符串值来替换。最后输出内容是输入数据最后一行所有”&{串名}"
        被替换后的串值。

        输入数据
        xxx = sss / ooo / & {ttt} / uuu
        ttt = www
        eee = jjj
        yyy = ggg / ppp / & {xxx} / ttt / & {eee}

        输出数据
        ggg / ppp / sss / ooo / www / uuu / ttt / jjj
        '''
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
        # 挑7
        '''
         输出7有关数字的个数，包括7的倍数，还有包含7的数字（如17，27，37...70，71，72，73...）的个数（一组测试用例里可能有多组数据，请注意处理）
        输入描述:
        一个正整数N。(N不大于30000)
        输出描述:
        不大于N的与7有关的数字个数，例如输入20，与7有关的数字包括7,14,17.
        in:
        20
        :return:
        3
        '''
        while True:
            try:
                top_int = int(input())
                print(len(mySolPack.calcAll7relatedNums(top_int)))
            except:
                break

    @unittest.skip("passed")
    def testNamesVotesSort(self):
        # 员工投票，选明日之星
        '''
        input:
        Lucy,Tom,Jerry,Lucy,Tom,Tom,Tommy,Tommy
        output:
        Tom
        '''
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
        # 高精度的整数加法
        '''
        请设计一个算法完成两个超长正整数的加法。
        接口说明
        input:
        9876543210
        1234567890
        output:
        11111111100
        '''
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
        # 输入n个整数，输出其中最小的k个。
        '''
        in:
        n k
        n integers
        out:
        smallest k numbers
        input:
        5 2
        1 3 5 7 2
        output:
        1 2
        '''
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

    @unittest.skip("passed")
    def testCalcPermutationNumFromListStr(self):
        # 字符串不同的排列数
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
        # 排列组合公式
        while True:
            try:
                innum = tuple(map(int, input().split()))
                print(util.calcPermutationNum(innum[0], innum[1]))
            except:
                break

    @unittest.skip("passed")
    def testFindCyclesInGraph(self):
        # 有向图是否有环
        '''
        input:
        A->B,B->C,C->D,E->A
        output:
        Graph is cyclic in nature
        '''
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
        # 逻辑运算符
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

    # @unittest.skip("passed")
    def testSortStrs(self):
        while True:
            try:
                in_str = input().strip()
                inlist = [it.strip() for it in in_str.split(",")]
                if len(in_str) > 100:
                    break
                if inlist == [] or "":
                    break
                sorted_ls = sorted(inlist, key=lambda it: it[-1], reverse = True)
                final_str = ""
                for it in sorted_ls:
                    final_str += "," + it
                print(final_str[1:])
            except:
                break


    @unittest.skip("on hld")
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
    @unittest.skip("on hld")
    def testPrimeNumPairs(self):
        while True:
            try:
                num = int(input())
                if num % 2 != 0:
                    print("num is not a even num")
                    break
                int_list =[int(it.strip()) for it in input().split()]
                pairs = []
                mySolPack.getPrimePairs(int_list)
                print(pairs)

            except:
                break
if __name__ == "__main__":
    unittest.main()