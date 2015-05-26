
#!/usr/bin/python
#coding:utf-8


import random


class poker:
    color = 0    #1：红心   2：方块     3：梅花     4：黑桃
    number = 1
    
    def __init__(self, c, n):
        self.color = c
        self.number = n
        
       
    def make(self, c, n):
        self.color = c
        self.number = n
        
    def show(self):
        if self.color == 1:
            print '红心',
        if self.color == 2:
            print '方块',
        if self.color == 3:
            print '梅花',
        if self.color == 4:
            print '黑桃',
        if self.number == 14:
            print 'A' + ' ',
        elif self.number == 13:
            print 'K' + ' ',
        elif self.number == 12:
            print 'Q' + ' ',
        elif self.number == 11:
            print 'J' + ' ',
        else:
            print self.number,
            print ' ',

class PokerArray:
    array = []
    poker = poker(1, 14)
    publicArray = []
    playOneArray = []
    playTwoArray = []
    end = 51
    def __init__(self):
        
       
        for i in range(1, 5):
            for j in range(2, 15):
                self.poker = poker(i, j)
                self.array.append(self.poker)
    
         
  
    def sendPublicPorks(self):
        for i in range(0, 5):
            index = random.randint(0, self.end)
            self.publicArray.append(self.array[index])
            del self.array[index]
            self.end -= 1
        return self.publicArray

                
    def sendPlayOnePorks(self):
        for i in range(0, 2):
            index = random.randint(0, self.end)
            self.playOneArray.append(self.array[index])
            del self.array[index]
            self.end -= 1
        return self.playOneArray
    
    def sendPlayTwoPorks(self):
        for i in range(0, 2):
            index = random.randint(0, self.end)
            self.playTwoArray.append(self.array[index])
            del self.array[index]
            self.end -= 1
        return self.playTwoArray            
            
    
class Match():
    pokers = [];
    

    def __init__(self, p1, p2, p3, p4, p5):
        self.pokers.append(p1)
        self.pokers.append(p2)
        self.pokers.append(p3)
        self.pokers.append(p4)
        self.pokers.append(p5)
        
    def randomCreate(self):
        for i in range(0, 5):   
                self.pokers[i]= poker(random.randint(1, 4), random.randint(2, 14))
                self.pokers[i].show()   
                
    def sort(self):
        print 'sort begin------------------'
        for i in range(0, 4):
            j = i + 1
            while(j < 5):
                if self.pokers[i].number < self.pokers[j].number:
                    temp = self.pokers[i]
                    self.pokers[i] = self.pokers[j]
                    self.pokers[j] = temp
                j += 1
        for m in range(0, 5):
            self.pokers[m].show()
    
                
                    
                    
        
    def isFirstKind(self):
        print '1'
        
        
    def isSixthKind(self):
        if (self.pokers[0].number == (self.pokers[1].number + 1))and(self.pokers[1].number == (self.pokers[2].number + 1))and(self.pokers[2].number == (self.pokers[3].number + 1))and(self.pokers[3].number == self.pokers[4].number + 1):
            #print '顺子'
            return True
        else:
            return False
            
    def isFifthKind(self):
        if (self.pokers[0].color == self.pokers[1].color):
            if (self.pokers[1].color == self.pokers[2].color):
                if (self.pokers[2].color == self.pokers[3].color):
                    if (self.pokers[3].color == self.pokers[4].color):
                        #print '同花'
                        return True
                    else:
                        #print '不是同花'
                        return False
                else:
                    #print '不是同花'
                    return False
            else:
                #print '不是同花'
                return False
        else:
            #print '不是同花'
            return False
      
    def isSecondeKind(self):
        if ((self.isFifthKind() ) and (self.isSixthKind() )):
            #print '同花顺'
            return True
        else:
            return False
    def matchSame(self):
       
        mixArray = []
        flag = 0
        fatalNumber = 0
        sameOne = [0, 0] 
        sameTwo = [0, 0]
        level = 0
        print 'begin matchSame'
        for i in range(0, 5):
            #self.pokers[i].show()
            #print self.pokers[i].number
            j = i + 1
            while(j < 5):
                if (self.pokers[i].number == self.pokers[j].number):
                    
                    if (sameOne[1] == self.pokers[j].number):
                        sameOne[0] += 1
                                                
                    elif sameOne[0] != 0:
                        
                        if(sameTwo[1] == self.pokers[j].number):
                            sameTwo[0] += 1 
                        elif sameTwo[0] != 0:
                            print ''
                        else:
                            
                            sameTwo[1] = self.pokers[j].number  
                            sameTwo[0] = 2
   
                    else:
                        sameOne[1] = self.pokers[j].number
                        sameOne[0] = 2                        
  
                    flag += 1
                j += 1
        if sameOne[0] == 4:
            sameOne[0] = 3
        if sameTwo[0] == 4:
            sameTwo[0] = 3        
        if flag == 6:
            level = 8
            if self.pokers[0].number == sameOne[1]:
                fatalNumber = sameOne[i]
            else:
                fatalNumber = self.pokers[4].number
        if flag == 4:
            level = 7
            if sameOne[0] == 3:
                fatalNumber = sameOne[1]
            else:
                fatalNumber = sameTwo[1]
            
        if flag == 3:
            level = 4
            if self.pokers[0].number == sameOne[1]:
                fatalNumber = self.pokers[3].number
            else:
                fatalNumber = self.pokers[0].number
        
        if flag == 2:
            level = 3
            if ((self.pokers[0].number != sameOne[1])and(self.pokers[0].number != sameTwo[1])):
               
                fatalNumber = self.pokers[0].number
            else:
                fatalNumber = self.pokers[4].number
                
        if flag == 1:
            level = 2
            if self.pokers[0].number != sameOne[1]:
                fatalNumber = self.pokers[0].number
            else:
                fatalNumber = self.pokers[2].number
                 
        if flag == 0:
            level = 1
            fatalNumber = self.pokers[0].number
            if self.isSixthKind():
                level = 5
                flag = -1
            if self.isFifthKind():
                level = 6
                flag = -2
            if self.isSecondeKind():
                flag = -3
                level = 9
                if self.pokers[0].number == 14:
                    flag = -4
                    level = 10
        mixArray.append(flag)
        mixArray.append(sameOne)
        mixArray.append(sameTwo)
        mixArray.append(fatalNumber)
        mixArray.append(level)
        mixArray.append(self.pokers)
        print 'match is end'
        return mixArray

def showResult(resultBox):
    result = resultBox
    flag = result[0]
    sameOne = result[1]
    sameTwo = result[2]
    fatalNumber = result[3]
    pokers = resultBox[5]
    
    if flag == 6:
        print 'four bar:四张%d'%(sameOne[1])
    elif flag == 4:
        print 'hu lu: %d个%d, %d个%d'%(sameOne[0], sameOne[1], sameTwo[0], sameTwo[1])
    elif flag == 3:
        print 'three bar:三张%d'%(sameOne[1])
    elif flag == 2:
        print 'double que 一对%d 一对%d'%(sameOne[1], sameTwo[1])
    elif flag == 1:
        print 'One que 一对%d %d最大'%(sameOne[1],fatalNumber) 
    elif flag == 0:
        print '高牌: %d最大:'%fatalNumber
    elif flag == -1:
        print '顺子: %d大'%fatalNumber
    elif flag == -2:
        print '同花: %d'%fatalNumber
    elif flag == -3:
        print '同花顺: %d'%fatalNumber
    elif flag == -4:
        print '皇家同花顺'    
    for i in range (0, 5):
        pokers[i].show()
    print '\n'

def showWin(result):
    win = 0
    level = result[0][4]
    fatalNmuber1 = result[0][3]
    fatalNmuber2 = result[1][3]
    OneNumber1 = result[0][1][1]
    OneNumber2 = result[0][2][1]
    TwoNumber1 = result[1][1][1]
    TwoNumber2 = result[1][2][1]
    pokers1 = result[0][5]
    pokers2 = result[1][5]
    if result[0][4] > result[1][4]:
        win = 1
    elif result[0][4] < result[1][4]:
        win = 2
    else:
        if ((level == 10)or(level == 9)or(level == 6)or(level == 5)):
            if fatalNmuber1 > fatalNmuber2:
                win = 1
            elif fatalNmuber1 < fatalNmuber2:
                win = 2
            else:
                win = 0
        elif level == 8:
            if OneNumber1 > TwoNumber1:
                win = 1
            elif OneNumber1 < TwoNumber1:
                win = 2
            else:
                if fatalNmuber1 > fatalNmuber2:
                    win  = 1
                elif fatalNmuber1 < fatalNmuber2:
                    win = 2
                else:
                    win = 0
        elif level == 7:
            if OneNumber1 > TwoNumber1:
                win = 1
            elif OneNumber1 < TwoNumber1:
                win = 2
            else:
                if OneNumber2 > TwoNumber2:
                    win = 1
                elif OneNumber2 < TwoNumber2:
                    win = 2
                else:
                    win = 0
        elif level == 4:
            if OneNumber1 > TwoNumber1:
                win = 1
            elif OneNumber1 < TwoNumber1:
                win = 2
            else:
                if fatalNmuber1 > fatalNmuber2:
                    win = 1
                elif fatalNmuber1 < fatalNmuber2:
                    win = 2
                else:
                    win = 0
        
        
                
                
            
                
            
    





        elif level == 3:
    
            if OneNumber1 > TwoNumber1:
                win = 1
            elif OneNumber1 < TwoNumber1:
                win = 2
            else:
                if OneNumber2 > TwoNumber2:
                    win = 1
                elif OneNumber2 < TwoNumber2:
                    win = 2
                else:
                    if fatalNmuber1 > fatalNmuber2:
                        win = 1
                    elif fatalNmuber1 < fatalNmuber2:
                        win = 2
                    else:
                        win = 0                    
        elif level == 2:
            if OneNumber1 > TwoNumber1:    
                win = 1
            elif OneNumber1 < TwoNumber1:
                win = 2
            else:
                if fatalNmuber1 > fatalNmuber2:
                    win  = 1
                elif fatalNmuber1 < fatalNmuber2:
                    win = 2
                else:
                    win = 0            
            
        elif level == 1:
            for i in range(0, 4):
                if pokers1[i].number > pokers2[i].number:
                    win = 1
                    break;
                elif pokers1[i].number < pokers2[i].number:
                    win = 2
                    break;
                else:
                    win = 0
                         
    if win == 1:
        print 'play1 win'
    elif win == 2:
        print 'play2 win'
    else:
        print 'The Same！！'

poker1 = poker(2, 3)
poker2 = poker(1, 5)
poker3 = poker(2, 2)
poker4 = poker(2, 14)
poker5 = poker(2, 13)    
    
myPoker = PokerArray()
PublicPorks = myPoker.sendPublicPorks()
PlayOnePorks = myPoker.sendPlayOnePorks()
PlayTwoPorks = myPoker.sendPlayTwoPorks()

result = []

playerNumber = (int)(input('play1 or play2:'))
if playerNumber == 1:
    
    print 'Public Porks is:'
    for i in range(0, 5):
        PublicPorks[i].show()
    
    print '\nYour Porks is:'
    for i in range(0, 2):
        PlayOnePorks[i].show()  
        
    print '\nPlease PickPorks:'
    
    playOnePickArray = []
    pickCount = 0
    while(pickCount < 3):
        index = (int)(raw_input('pick Pork %d: '%(pickCount + 1)))
        index -= 1
        if (index in playOnePickArray):
            print 'no same Pork, pick again'
        else:
            playOnePickArray.append(index)
            PlayOnePorks.append(PublicPorks[index])
            pickCount += 1
        
    print 'Now Your Porks is:'
    for i in range(0, 5):
        PlayOnePorks[i].show()
    
    print '\n'
    
    matchPlayOne = Match(poker1, poker2, poker3, poker4, poker5)
    
    matchPlayOne.pokers = PlayOnePorks
    matchPlayOne.sort()
    print '\n'
    
    resultOne = matchPlayOne.matchSame()
    result.append(resultOne)

go = (int)(input('press 1 to go on:'))
if go == 1:
    print 'go！'
    
for i in range(0, 15):
    print '\n'
    
playerNumber = (int)(input('play1 or play2:'))    
if playerNumber == 2:
            
    print 'Public Porks is:'
    for i in range(0, 5):
        PublicPorks[i].show()
        
    print '\nYour Porks is:'
    for i in range(0, 2):
        PlayTwoPorks[i].show()  
            
    print '\nPlease PickPorks:'
        
    playTwoPickArray = []
    pickCount = 0
    while(pickCount < 3):
        index = (int)(raw_input('pick Pork %d: '%(pickCount + 1)))
        index -= 1
        if (index in playTwoPickArray):
            print 'no same Pork, pick again'
        else:
            playTwoPickArray.append(index)
            PlayTwoPorks.append(PublicPorks[index])
            pickCount += 1
            
    print 'Now Your Porks is:'
    for i in range(0, 5):
        PlayTwoPorks[i].show()        

    matchPlayTwo = Match(poker1, poker2, poker3, poker4, poker5)
    
    matchPlayTwo.pokers = PlayTwoPorks
    matchPlayTwo.sort()
    print '\n'
    
    resultTwo = matchPlayTwo.matchSame()
    result.append(resultTwo)
  

password = (int)(input('Enter the password to see result:')) 
if password == 123456:
    print 'play1 result:'
    showResult(result[0])
    print 'play2 result:'
    showResult(result[1])
    showWin(result)
        
    
    
    
    

#print 'Public Porks is:'
#for i in range(0, 5):
    #PublicPorks[i].show()

#print '\nPlayOne\'Porks is:'
#for i in range(0, 2):
    #PlayOnePorks[i].show()
    
#print '\nPlayTwo\'Porks is:'
#for i in range(0, 2):
    #PlayTwoPorks[i].show()

#print '\nTime to PlayOne InsertPickPorks:'

#playOnePickArray = []
#pickCount = 0
#while(pickCount < 3):
    #index = (int)(raw_input('pick Pork %d: '%(pickCount + 1)))
    #index -= 1
    #if (index in playOnePickArray):
        #print 'no same Pork, pick again'
    #else:
        #playOnePickArray.append(index)
        #PlayOnePorks.append(PublicPorks[index])
        #pickCount += 1
    
#print 'Now PlayOne\'Porks is:'
#for i in range(0, 5):
    #PlayOnePorks[i].show()

#print '\n'


    
#if match1.isSecondeKind():
    #if match1.poker1.number  == 14:
        #print '皇家',
    #print  '同花顺'
        