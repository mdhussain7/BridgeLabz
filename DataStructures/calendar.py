# Creating a calendar in proportion to the user defined starting date

n = int(input('Enter number of days from 1 to 31: ')) #days in a month
s = input('The first day of the week ex:Sa,M,T,W,Th,F,Su: ') #The date that user wants the month to start
s = s.capitalize()

lis1 = ['Sa','M','T','W','Th','F','Su']
print('{:>3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'.format('Sa','M','T','W','Th','F','Su'))

for i in range(1,n+1):#loop to generate the dates for a month
  if s==lis1[0] and i ==1:#this is to determine how much should the code indent to align to traditional
     # calendar formatting
    print('{:>3}'.format(i),end =' ')
  elif s==lis1[1] and i ==1:
    print(' \n'*4+'{:>3}'.format(i),end =' ')
  elif s==lis1[2] and i ==1:
    print(' \n'*8+'{:>3}'.format(i),end =' ')
  elif s==lis1[3] and i ==1:
    print(' \n'*12+'{:>3}'.format(i),end =' ')
  elif s==lis1[4] and i ==1:
    print('\n '*16+'{:>3}'.format(i),end =' ')
  elif s==lis1[5] and i ==1:
    print('\n '*20+'{:>3}'.format(i),end =' ')
  elif s==lis1[6] and i ==1:
    print('\n '*24+'{:>3}'.format(i),end =' ')
  else:
    print('{:>3}'.format(i),end =' ')#after the indent this is to print the remaining dates

  if s==lis1[0] and i%7==0:  #this is to print a new line in proportion the choosen
     # starting date so as to stay in check with the traditional calendar format
    print("\n")
  elif s==lis1[1] and i%7==6:
    print("\n")
  elif s==lis1[2] and i%7==5:
    print("\n")
  elif s==lis1[3] and i%7==4:
    print("\n")
  elif s==lis1[4] and i%7==3:
    print("\n")
  elif s==lis1[5] and i%7==2:
    print("\n")
  elif s==lis1[6] and i%7==1:
    print("\n")