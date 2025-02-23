# შექმენით ფუნქცია რომელიც იღებს key-ები და value-ების მასივებს. 
# თქვენი მიზანია დააბრუნოთ ობიექტი შესაბამისი key-value-ბით. 

def function(keys, values):
    if len(keys) == len(values):
        result = {}
        for i in range(len(keys)):
            result[keys[i]] = values[i]
        return print(result)
    else:
        return print("Error: key-ები და value-ები არ ემთხვევა ერთმანეთს")

function(["name","age"],["giorgi",21,177])
function(["name","age","height"],["giorgi",21,177])