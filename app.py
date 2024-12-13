
import math

b ="HELLO WORLD!"
'''
Copy a array
'''
#try {a = b[2:0]}
a = b[0:-1]
# tim 1 ky tu trong chuoi
indexOfSign = a.find('!')
# -1 index = 11 index
IsEqualAtElevenAndMinus_One= b[11] == b[-1]
#print(a, indexOfSign, IsEqualAtElevenAndMinus_One)
# replace:
#print(a.replace('L', '#'))
# in operator:
CompanyMember = ['nguyễn văn a','Nguyen Văn B','Nguyen Tuan Kiet']
#Name = input('Your Name is: ' )
IsMember = False
# for FullName in CompanyMember:
#     if Name in FullName:
#         IsMember=True
if (IsMember):
    print('You are kaishain !!!')
else:
    print('You are not in this Company')   
# Viet hoa chu cai dau moi tu    
print(CompanyMember[0].title())
print(CompanyMember[0].upper())  
print(CompanyMember[0].lower())

# Mathetica Operators:
decimal = 1.5
x = 2 
y = 3
# exp:
exp = x**y
# div
div_result =  y//x
# Order in Expression: 
# 1. exp
# 2. multiplication or division
# 3. add or substraction

# Template string:
price = 10**6 # M$
SaleOffTenPercent = (1-0.1) * price
print(f"Your payment is {SaleOffTenPercent}$")
