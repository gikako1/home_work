# შევქმნათ შემდეგი ფუნქციები:
# 1) ფუნქცია რომელსაც გადაეცემა სვეტი და რიგი (row, col) და გამოპრინტავს თითოეული ელემენტის პოზიციას სვეტი-სვეტ ,
#  მაგ: ( 2, 2 ) --->  row: 1 col:1, row: 1 col:2, row: 2 col: 1, row:2 col: 2;
def print_positions(rows, cols):
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            print(f"row: {row} col: {col}")
print_positions(5,2)
# 2) ფუნქცია რომელიც ქმნის გამრავლების ტაბულას 1-10 და აბრუნებს მათ 2D მასივის ფორმაში ანუ ასეთში:
#   [  [1,2,3...],  [2,4,6...],  [3,6...]...  ]

def multiplication_table():
    return [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(multiplication_table())

