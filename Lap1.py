from docx import Document

with open('Lap1.txt', 'r') as file:
    n = int(file.readline().strip())
    #lines = file.read()
    #print("after strip: ",file.readline())
    numbers = list(map(int, file.readline().split()))

#mylist = []

print(numbers[0])
print(f"Numbers: {numbers}")

def FindLagestSumVI(numbers):
    i =0,j=0,k=0,LSum= 0
    while i<n:
        TempSum = 0
        while j<n:

            while k>=i and k<=j:
                TempSum+=numbers[k]
        if TempSum > LSum:
            LSum= TempSum
        
            
