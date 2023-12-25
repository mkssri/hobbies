"""
 * 
***
 *
"""

n = 7

m = n//2
for i in range(n):
 for j in range(n):
  if(i<=m):
   t=i
  else:
   #t=2*m-i
   t=n-1-i
   #print("i:{} and t:{}".format(i,t))
  if( j<(m-t) or j>(m+t)):
   print(" ",end="")
  else:
   print("*",end="")
 print("")
