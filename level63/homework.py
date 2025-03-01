# 1) შექმენით ფუნქცია რომელსაც გადმოეცემა ორი მოთამაშის არჩეული მოძრაობა ( rock, paper, scissors ) და აბრუნებს რომელმა მოიგო
def rock_paper_scissors(p1,p2):
    if p1=='rock' and p2=='scissor':
        print("rock wins")
    if p1=='rock' and p2=='paper':
        print("paper wins")
    if p1=='paper' and p2=='scissor':
        print('scissor wins')
    if p1==p2:
        print('draw')
    if p2=='rock' and p1=='scissor':
        print("rock wins")
    if p2=='rock' and p1=='paper':
        print('paper wins')
    if p2=='paper' and p1=='scissor':
        print('scissor wins')
rock_paper_scissors('scissor','paper')
rock_paper_scissors('rock','rock')
rock_paper_scissors('paper','rock')

# 2) შექმენით ფუნქცია რომელსაც გადმოეცემა ორი მასივი სამ სამი ელემენტით.
#  პირველი მოთამაშის [ძალა, სისწრაფე, ინტელიგენტი]
#  და მეორე მოთამაშის [ძალა, სისწრაფე, ინტელიგენტი].
#  თქვენი მიზანია დაადგინოთ რომელი მოიგებს
# ძალა არის 1 ქულა, სისწრაფე 2 ხოლო ინტელიგენტი ამ ორის ჯამს ამრავლებს თავის თავი გაყოფილი 10-ზე.
def fightgame(p1,p2):
    if p1[0]+p1[1]*2+(((p1[0]+p1[1])*p1[2])/10) > p2[0]+p2[1]*2+(((p2[0]+p2[1])*p2[2])/10):
        print('player one wins')
    if p1[0]+p1[1]*2+(((p1[0]+p1[1])*p1[2])/10) < p2[0]+p2[1]*2+(((p2[0]+p2[1])*p2[2])/10):
        print('player two wins')
    if p1[0]+p1[1]*2+(((p1[0]+p1[1])*p1[2])/10) == p2[0]+p2[1]*2+(((p2[0]+p2[1])*p2[2])/10):
        print('draw')

fightgame([1000,2,3],[2,3,4])