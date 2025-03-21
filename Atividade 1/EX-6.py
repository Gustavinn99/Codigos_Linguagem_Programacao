primos = []
num =2
while len (primos) < 100:
       num_primo = True
       for i in range(2, int (num**0.5) +1):
         if num % i ==0:
            num_primo = False
            if num_primo:
             primos.append(num)
             num+=2
            break
print(primos)
