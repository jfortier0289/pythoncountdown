from datetime import date

def diff_dates(date1, date2):
    return abs(date2-date1).days

def main():
    d1 = date.today()
###########################################################
#   Below is where is change the date where the countdown #
#   is to                                                 #
###########################################################
    d2 = date(2019,12,25)
    result1 = diff_dates(d2, d1)
    print '{} days b4 christmas'.format(result1, d1, d2)

main()
