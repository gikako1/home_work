#1 შექმენით ფუნქცია რომელიც მომხმარებელს შეაყვანინებს ტექსტს, თუ მომხმარებელს ეს ტექსტი უკვე შეყვანილი ექნება მირჩეს პროგრამა 
def text_entry_program():
    entered_texts = set()
    
    while True:
        user_input = input("Please enter some text (or type 'exit' to quit): ")
        
        if user_input in entered_texts:
            print("You've already entered that text. Goodbye")
            break

        entered_texts.add(user_input)
        print("Text added! Enter something else.")

text_entry_program()

#2 შექმენით პროგრამა რომელიც მომხმარებლის შეტანილი რიხცვს დაუმატებს ერთ ერთს სანამ მოცემული რიცხვი არ შედგება 0-ებისგან
#  ( პირველი რიცხვუს გარდა ), მაგ: 156–> 200, 5678 —> 6000…





#3 მომხმარებელს შეაყვანინეთ პაროლი. სანამ სწორ პაროკს არ შეიყვანს (12348765 ), იქამდე გააგრძელეთ კითხვა
def password(pw):
    for attempt in pw:
        attempt=str(input())
        if attempt != pw:
            print("Wrong try again!")
            continue
        if  attempt == pw: 
            print("Correct")
            break
password("nigga")