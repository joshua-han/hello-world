hours=raw_input('how long')
rate=raw_input('how much per hour')
hours=int(hours)
rate=int(rate)
if hours<40:
    print'pay',hours*rate
else:
    print'pay',40*10+15*(hours-40)
    

