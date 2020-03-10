import time
total=int(time.time())
day=total//(24*60*60)
day_hour=total-day*24*60*60
hour=day_hour//(60*60)
day_min=day_hour-hour*60*60
min=day_min//60
s=day_min%60

print('经过了',day,'天',hour,'小时',min,'分钟',s,'秒')

