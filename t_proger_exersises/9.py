"""
Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
"""
time = {'days': 0, 'hours': 0, 'minutes': 0, 'sec': 0}

seconds = 3932 * 24 * 3
time['days'] = int(seconds / (24 * 3600))
seconds -= time['days'] * (24 * 3600)
time['hours'] = (int(seconds / (60 * 60)))
seconds -= time['hours'] * 60 * 60
time['minutes'] = int(seconds / 60)
seconds -= time['minutes'] * 60 
time['sec'] = seconds 
print(time['days'], ':', time['hours'], ':', time['minutes'], ':', time['sec'])

