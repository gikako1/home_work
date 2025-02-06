# იგივე რაც DAY 50 ვინაიდან უმეტესობამ ვერ გააკეთა, პლიუს ბონუს ამოცანა:
# ბონუსი) შევქმნათ ფუნქცია რომელსაც გადაეცემა მატრიცა (2დ მასივი) (NxN),
#  ჩვენი მიზანია დავაბრუნოთ ორი მასივი, ერთში უნდა იყოს გადმოცემული 
# მასივის რიგების ჯამები, მეორეში კი გადმოცემული მასივის რიადების /რიგების
#  ჯამები. წარმატებები.❤️
def row_column_sums(matrix):
    row_sums = []
    column_sums = [0] * len(matrix[0])  # სვეტების ჯამების დასაწყისი 0-ით
    
    for i in range(len(matrix)):  # ვხვდებით თითოეული რიგის ჯამს
        row_sum = 0
        for j in range(len(matrix[i])):  # თითოეულ ელემენტს ვატყობ
            row_sum += matrix[i][j]
            column_sums[j] += matrix[i][j]  # ამავე დროს ვამატებთ სვეტს
        row_sums.append(row_sum)
    
    return print("Row sums:", row_sums),print("Column sums:", column_sums)
row_sums, column_sums = row_column_sums([[1,2],[2,3]])

