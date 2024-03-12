v_year = int(input('What year is the vehicle? '))

if v_year <=1879:
    message='Must be a Carl Benz, with few safety features'
    print(message+'.', end=" ")
if v_year <=1969:
    message='Few safety features'
    print(message+'.', end=" ")
if v_year >=1970:
    message1='Probably has seat belts'
    print(message1+'.', end="")
if v_year >=1990:
    message2='Probably has antilock brakes'
    print(message2+'.', end=" ")
if v_year >=2000:
    message3='Probably has airbags'
    print(message3+'.', end=" ")
