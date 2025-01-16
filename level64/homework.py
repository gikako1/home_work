# 1. **შექმენით ფუნქცია: "გადავიდეთ თუ არა ტესტში"**  
#/ ფუნქციას გადაეცით შეფასებები და დამწერები. ტესტის ჩაბარება მოხდება თუ ერთ-ერთი მათგანი აკმაყოფილებს მოთხოვნებს.
def Did_you_pass(points,student):
    if points>=80:
        print(student + " has passed the test!")
    elif points<=80:
        print(student + " did not pass the test.")
Did_you_pass(12,"giorgi")
Did_you_pass(80,"giorgi")
# 2. **შექმენით ფუნქცია: "შეგვიძლია თუ არა გასვლა გარეთ"**  
#/ საჭიროა ამინდი იყოს კარგი ან დრო საკმარისი იყოს, და ჩვენ მზად ვიყოთ გასასვლელად.
#*P.S აქ მხოლოდ შეიძლება sunny, cloudy, windy, rainy, და stormy ამინდების გამოყენება
def should_i_go_out(weather,time):
    if weather=="sunny":
        print("yes, you can go out.")
    elif weather=="stormy":
        print("no, you can't go out.")
    elif weather=="cloudy"and time<=18:
        print("yes, you can go out.")
    elif weather=="windy"and time<=18:
        print("yes, you can go out.")
    elif weather=="windy"and time>18:
        print("no, you can't go out.")
    elif weather=="rainy"and time<=18:
        print("if you have an umbrella, yes, you can go out.")
    elif weather=="rainy"and time>18:
        print("if you have an umbrella, yes, you can go out.")
should_i_go_out("sunny",18)
should_i_go_out("stormy",18)
# 3. **შექმენით ფუნქცია: "გადავდგათ თუ არა ნაბიჯი"**  
#/ საჭიროა ბარიერი არ იყოს და წასასვლელი სივრცე ხელმისაწვდომი იყოს, ან მეორე მხარეს სიგნალი მოდიოდეს.
def should_i_go(barrier,zebra,traffic_lights):
    if barrier==False and zebra==True and traffic_lights==True:
        print("yes, you may walk.")
    elif barrier==True and zebra==True and traffic_lights==True:
        print("no, you may not walk.")
    elif barrier==False and zebra==False and traffic_lights==True:
        print("no, you may not walk.")
    elif barrier==False and zebra==True and traffic_lights==False:
        print("no, you may not walk.")
should_i_go(False,True,True)
should_i_go(True,True,True)
# 4. **შექმენით ფუნქცია: "უნდა ავიღოთ თუ არა ნივთი"**  
#/ საჭიროა ნივთი ხელმისაწვდომი იყოს და მისი წაღება დასაშვები იყოს, ან სხვა ადამიანს არ სურდეს მისი გამოყენება.
def take_or_not(availability,permit,demand):
    if availability==True and permit==True or demand==False:
        print("yes, you may take.")
    elif demand==True:
        print("no, you may not take.")
take_or_not(True,False,True)
take_or_not(False,False,False)
# 5. **შექმენით ფუნქცია: "უნდა გავიხსენოთ თუ არა ინფორმაცია"**  
#/ საჭიროა დავალება იყოს აქტუალური ან ინფორმაცია ჯერ კიდევ საჭირო იყოს, და დრო გვქონდეს მის დასამუშავებლად.
def remember_or_not(expired,needed,time):
    if (expired==False or needed==True) and time==True:
        print("yes, you have to remember.")
    else: print("no, you don't have to remember.")
remember_or_not(False,True,True)
remember_or_not(True,False,True)
# 6. **შექმენით ფუნქცია: "უნდა დავიძინოთ თუ არა"**  
#/ საჭიროა დრო იყოს გვიანი და ადამიანი დაღლილი იყოს, ან მეორე დღეს ადრიანად ადგომა საჭირო იყოს და შუქი გამორთული იყოს.
def sleep_or_not(time,tired,early,lights):
    if ((time==24 or (time>=1 and time<6)) and tired==True) or ((early==True) and lights==False):
        print("you should sleep.")
    else:print("no you don't have to sleep.")
sleep_or_not(24,True,True,False)
sleep_or_not(24,False,True,False)
sleep_or_not(24,False,False,False)
# 7. **შექმენით ფუნქცია: "უნდა წავიდეთ თუ არა წვეულებაზე"**  
#/ საჭიროა მეგობრები თანახმა იყვნენ წასვლაზე და მეორე დღეს სამუშაო არ იყოს, ან წვეულება ახლოს ტარდებოდეს.
def party_or_not(friends,work_next_day,close_to_me):
    if (friends==True and work_next_day==False) or close_to_me==True:
        print("yes, you may party.")
    else:print("no, you may not party.")
party_or_not(True,False,True)
party_or_not(True,True,True)
party_or_not(True,True,False)
# 8. **შექმენით ფუნქცია: "უნდა დავრჩეთ თუ არა სახლში"**  
#/ საჭიროა ამინდი იყოს წვიმიანი ან თოვლიანი, და გეგმები არ არსებობდეს, რომელიც გარეთ გასვლას საჭიროებს.
def should_i_go_or_not(rain,snow,plans):
    if (rain==True or snow==True) and plans==False:
        print("no, you shouldn't go out.")
    else:print("yes, you may go out")
should_i_go_or_not(True,True,False)
should_i_go_or_not(True,True,True)
# 9. **შექმენით ფუნქცია: "უნდა გავიდეთ სირბილზე თუ არა"**  
#/ საჭიროა ამინდი იყოს მშრალი და სპორტული ფეხსაცმელი ხელმისაწვდომი იყოს, ან მეგობარი მზად იყოს სირბილისთვის.
def run_or_not(weather_dry,running_shoes,friend):
    if (weather_dry==True and running_shoes==True) or friend==True:
        print("yes, you should go running.")
    else:print("no, you may not go running.")
run_or_not(True,True,True)
run_or_not(True,False,False)
# 10. **შექმენით ფუნქცია: "უნდა ვუყუროთ თუ არა ფეხბურთს"**  
#/საჭიროა დღე იყოს შაბათი ან კვირა და სხვა საქმეები არ გვქონდეს, ან თამაში ჩვენი საყვარელი გუნდის იყოს.
#/( ყველაზე კარგი ვარიანტია თუ შექმნით თითოეულისთვის ფუნქციას შესაბამისი რაოდენობის არგუმენტებით და ამ პრინციპით დაწერთ )
def football(weekend,plans,fav_club):
    if (weekend==True and plans==False) or fav_club==True:
        print("yes, you may watch football.")
    else:print("no you may not watch football.")
football(True,False,True)
football(False,False,False)