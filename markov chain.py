A = [0.33333]
B = [0.33333]
C = [0.33333]


for i in range(1, 100):
    A.append(round(A[i-1] * 0.1 + B[i-1] * 0.6 + C[i-1] * 0.4, 6))
    B.append(round(A[i-1] * 0.5 + B[i-1] * 0.1 + C[i-1] * 0.5, 6))
    C.append(round(A[i-1] * 0.4 + B[i-1] * 0.3 + C[i-1] * 0.1, 6))
   
    
    if abs(A[i] - A[i-1]) >= 0.00001 or abs(B[i] - B[i-1]) >= 0.00001:
        print("{:.5f} {:.5f} {:.5f}".format(A[i],B[i],C[i]))
    else:    
        print("count: {}".format(i))
        break
        
         
    