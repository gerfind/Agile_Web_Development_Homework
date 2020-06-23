Input_list = input().split()


class Player:

    def __init__(self):
        self.hand = []
        self.number = []
        self.color = []
        self.level = 1
        self.cmplist = self.number

    def add_numbers(self):
        for i in self.hand:
            if i[0] == 'J':
                self.number.append(11)
            elif i[0] == 'Q':
                self.number.append(12)
            elif i[0] == 'K':
                self.number.append(13)
            elif i[0] == 'A':
                self.number.append(14)
            else:
                self.number.append(int(i[0]))

    def add_colors(self):
        for i in self.hand:
            self.color.append(i[1])

    def Royale(self):
        '''等级7'''
        if self.color[0] == self.color[1] == self.color[2] == self.color[3] == self.color[4] and self.number[1] - self.number[0] == self.number[2] - self.number[1] == self.number[3] - self.number[2] == self.number[4] - self.number[3] == 1:
            self.level = 7
            self.cmplist = self.number

    def Flush(self):
        '''等级6'''
        if self.color[0] == self.color[1] == self.color[2] == self.color[3] == self.color[4]:
            self.level = 6
            self.cmplist = self.number

    def Spectrum(self):
        '''等级5'''
        if self.number[1] - self.number[0] == self.number[2] - self.number[1] == self.number[3] - self.number[2] == self.number[4] - self.number[3] == 1:
            self.level = 5
            self.cmplist = self.number

    def Threeofakind(self):
        '''等级4并带序列'''
        for i in range(1, 4):
            if self.number[i] == self.number[i-1] == self.number[i+1]:
                pair_point = self.number[i]
                return_list = []
                for i in self.number:
                    if i != pair_point:
                        return_list.append(i)
                while len(return_list) < 5:
                    return_list.append(pair_point)
                self.level = 4
                self.cmplist = return_list

    def Pair(self):
        '''等级2并带序列'''
        for i in range(1, 5):
            if self.number[i] == self.number[i-1]:
                pair_point = self.number[i]
                return_list = []
                for i in self.number:
                    if i != pair_point:
                        return_list.append(i)
                return_list.append(pair_point)
                return_list.append(pair_point)
                self.level = 2
                self.cmplist = return_list

    def Two_Pair(self):
        '''等级3并带序列'''
        returned_list = self.cmplist
        for i in range(1, 3):
            if returned_list[i] == returned_list[i-1]:
                pair_point = returned_list[i]
                return_list = []
                for i in returned_list:
                    if i != pair_point:
                        return_list.append(i)
                return_list.append(returned_list[3])
                return_list.append(returned_list[3])
                return_list.append(pair_point)
                return_list.append(pair_point)
                self.level = 3
                self.cmplist = return_list


Black = Player()
Black.hand = Input_list[1:6]
Black.add_colors()
Black.add_numbers()
Black.number.sort()
Black.cmplist.sort()
Black.Pair()
Black.Two_Pair()
Black.Threeofakind()
Black.Spectrum()
Black.Flush()
Black.Royale()


White = Player()
White.hand = Input_list[7:12]
White.add_colors()
White.add_numbers()
White.number.sort()
White.cmplist.sort()
White.Pair()
White.Two_Pair()
White.Threeofakind()
White.Spectrum()
White.Flush()
White.Royale()


def Choose_winner():
    if Black.level > White.level:
        return 'Black wins'
    elif Black.level < White.level:
        return 'White wins'
    else:
        for i in range(4, 1, -1):
            if Black.cmplist[i] > White.cmplist[i]:
                return 'Black wins'
            elif Black.cmplist[i] < White.cmplist[i]:
                return 'White wins'
        return 'Tie'


print(Choose_winner())
