from datetime import date
from datetime import timedelta

def checkio(from_date, to_date):
    delta = to_date-from_date;

    from_day = from_date.weekday();
    to_day = from_date.weekday() + (delta.days % 7);
    extra = 0;
    if to_day==5 or (to_day>=6 and from_day == 6):
        extra = 1;
    elif to_day>=6:
        extra = 2;
        
     

    print ("diff: ", delta.days // 7, " d1: ", from_date.weekday(), ", d2:", to_date.weekday(), "from_day: ", from_day, "to_day: ", to_day);
    
    return (delta.days//7)*2 + extra; 

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

