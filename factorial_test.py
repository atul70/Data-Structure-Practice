def factorial(data):
    result = 0
    if data <= 1:
        #print('Factorial is ==> ', '1' )
        return 1
    else:
      return  data * factorial(data-1)


    #return result

print('factorial is ==> ',factorial(3))






