def generateRow(n):
    ans = 1
    row = [1]
    for i in range(1,n):
        ans = ans * (n-i)
        ans = ans//i

        row.append(ans)

    return row
    

def pascalTriangle(n):
    triangle = []
    for i in range(1,n+1):
        triangle.append(generateRow(i))

    return triangle

print(pascalTriangle(5))
