gender = 2
age = 15
if gender == 'male':
    if age < 18:
        print('A boy')
    else:
        print('A man')
elif gender == 'female':
    if age < 18:
        print('A girl')
    else: print('A woman')
else:
    if age < 18:
        print('A child')
    else:
        print('Adult')