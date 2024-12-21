'''
Calculate the result of the expression A > B and C or D, 
using the values in the following table:

A       B       C           D           Result
1       2       True        False       False
10      3       False       False       False
5       1       True        True        True
'''

case1_a = 1
case1_b = 2
case1_c = True
case1_d = False

result_1 = case1_a > case1_b and case1_c or case1_d
print(result_1)

case2_a = 10
case2_b = 3
case2_c = False
case2_d = False

result_2 = case2_a > case2_b and case2_c or case2_d
print(result_2)

case3_a = 5
case3_b = 1 
case3_c = True
case3_d = True
result_3 = case3_a > case3_b and case3_c or case3_d
print(result_3)
