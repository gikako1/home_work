word="skIbidi"
print(word)
print(word.upper())#upper() ბრძანება ყველა ასოს ადიდებს.
print(word.lower())#lower.() ბრძანება ყველა ასოს აპატარავებს.
print(word.capitalize())#capitalize() ბრძანება მხოლოდ პირველ ასოს ადიდებს და დანარჩენ ასოებს აპატარავებს.

Wlist=["super gela","rkinis gela","sigma gela","prosta gela"]
#pop ბრძანება ინდექსის მიხედვით აგდებს სიიდან სიის წევრს
print(Wlist.pop(1))
Wlist.pop(2)
print(Wlist)
Wlist.pop(0)
print(Wlist)

#insert ბრძანება ახალ წევრს სვამს სადაც ინდექსით მიუთითებ.
Wlist.insert(0,"skibidi gela")
print(Wlist)
Wlist.insert(1,"prosta gela")
print(Wlist)
Wlist.insert(2,"rkinis gela")
print(Wlist)

#append ბრძანება სიის ბოლოში ამატებს ახალ წევრს
Wlist.append("super gela")
print(Wlist)
Wlist.append("santexnikosi gela")
print(Wlist)
Wlist.append("mwvane gela")
print(Wlist)