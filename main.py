'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n<2:
    return False
  else:
    for i in range(2,n//2+1):
    if n%i==0:
      return False
  return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  p=1
  for i in lst:
  i=int(input("Dati numarul: "))
      p=p*i
  return p
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x!=y:
    if x>y: x-y
    else y=y-x
      print("cmmdc=",x)
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  
  
def main():
  # interfata de tip consola aici

if __name__ == '__main__':
  main()
