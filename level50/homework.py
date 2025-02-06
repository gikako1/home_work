# 1) შევქმნათ ფუნქცია, რომელიც დააბრუნებს ორი გადაცემული მატრიცის ( 2D მასივის ) ჯამს. მაგ: [[1,3],[1,4]], [[4,1],[2,2]] —> [[5,4],[5,5]]
def add_matrices(matrix1, matrix2):
      return print([[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))])
add_matrices([[1,3],[1,4]],[[2,4],[1,5]])
# 2) შევქმნათ ფუნქცია რომელიც გადაცემულ მატრიცას გაუცვლის რიგებს და სვეტებს
def switch_pos(col,row):
    for i in range(col):
        for j in range(row):
            print(0, end='')
        print()
switch_pos(5,2)