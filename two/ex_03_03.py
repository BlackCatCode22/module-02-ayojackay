score = input('Pick a score between 0.0 and 1.0')
try:
    fscore = float(score)
except:
    print('Only floating numbers')
    quit()

if fscore >= 0.9:
    print('Your grade is A')
elif 0.8 <= fscore < 0.9:
    print('Your grade is B')
elif 0.7 <= fscore < 0.8:
    print('Your grade is C')
elif 0.6 <= fscore < 0.7:
    print('Your grade is D')
elif fscore < 0.6:
    print('Your grade is F')
