def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def generate_twins(end):
   for i in range(end):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
         print(f"{(i,j)}")

generate_twins(1000)
