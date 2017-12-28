def min_to_hours(mins):
    hours = mins/60
    return hours

print(min_to_hours(69))
print(min_to_hours(169))
print(min_to_hours(269))
print(type(min_to_hours(469)))

#default and not-default args
#if you are passing a default arg, it should be last
#so as to avoid run time error

def mins_and_secs_to_hours(mins, sec=60):
    hours = mins/60 + sec/3600
    return hours
#without a second arg
print(mins_and_secs_to_hours(35))
#with second arg
print(mins_and_secs_to_hours(35, 1000))