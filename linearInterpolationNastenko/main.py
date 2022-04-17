N= int(input('Введіть кількість елементів масиву '))
array=[]
array1=[]
arrayDiff=0
sum=0
sum1=0
mse=0

for i in range(N): 
  b=float(input('Введіть X '))
  array.append(b)
  sum=sum+array[i]

#СКП=sqrt((SUM((x[i]-x_середнє)^2))/N)
  
average=sum/N 
for i in range(N):
  arrayDiff=(array[i]-average)**(2) 
  array1.append(arrayDiff)
  sum1=sum1+array1[i] 
mse=(sum1/N)**(0.5)
print('Вибірка ', array) 
print ('Середнє квадратичне відхилення = ', mse)

#числа, взяті для порівняння, є випадково обраними
if mse<=3:
  print ('розкид значень є малим')
else:
  if mse>3 and mse<=10:
    print ('розкид значень є середнім')
  else:
    print ('великий розкид значень')
print(' ')

print ('Лінійна інтерполяція')
xs=float(input('Введіть X '))
left=0;
right=0;
min=array[0]
max=array[N-1]
#
if xs<=array[N-1] and xs>=array[0]:
  
  for i in range(N):
    if array[i]<=xs:
      min=array[i]
      left=i
  
  ll = list(range(N-1, 0, -1))
  for i in ll: 
    if array[i]>=xs:
      max=array[i]
      right=i

#
if xs<=array[0]:
  min=xs-1
  left=-1
  
  ll = list(range(N-1, 0, -1))
  for i in ll: 
    if array[i]>=xs:
      max=array[i]
      right=i

if xs>=array[N-1]:
  
  for i in range(N):
    if array[i]<=xs:
      min=array[i]
      left=i
    
  max=xs+1
  right=N     
      
#у=ах+в
kA=(max-min)/(right-left)
kB=min-(kA*left)
y=(xs-kB)/kA
print ("Y = ", y)
    

