start = 0
lunch = 0
fullDay = 0
end = 0

fullDay = input('How long will you work today? (Enter time in increments of 0.25)')
start = input('What time did you start work today? (Enter time in increments of 0.25)')
lunch = input('How long is your lunch break? (Enter time in increments of 0.25)')

end = float(start) + float(fullDay) + float(lunch)
print('Your day will end at ' + str(float(end) - 12))
