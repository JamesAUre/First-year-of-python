#idk
def transpose(list):
    n = [[row[i] for row in list] for i in range(len(list[0]))]
    return n

def multiplication(matrix,vector):
    result = []
    for i in range(0,len(matrix)):
        total = 0
        for j in range(0,len(matrix[i])):
            total += matrix[i][j] * vector[j]

        #creating result vector
        result.append(total)

    return result

userlist = []
cols = ['energy','water','protein','carbs','sugar','fats','fibre']
rows = ['apple','orange','broccoli','beef','lamb','bread']

#matrix
nutr_vals=[[229,84.3,0.4,12.0,11.8,0.0,2.3],
           [186,84.3,1,9.5,8.3,0.2,2.1],
           [124,89.6,3.2,2.0,2.0,0.1,4.1],
           [613,70,22.8,0.2,0.0,6.0,0.0],
           [1056,60.2,18.6,0.0,0.0,20.2,0.0],
           [1446,37.6,8.4,43.5,1.5,2.6,6.9]]

#userinput as a vector
for i in range(0,6):
    userlist.append(int(input("Enter: ")))

print (cols)

#matrix and vector used in multiplication
print(multiplication(transpose(nutr_vals),userlist))


