from datetime import datetime
start = datetime.now()

divisible_by_3_or_5 = [p for p in range(1000) if p%3==0 or p%5==0]
print( sum(divisible_by_3_or_5) )

end = datetime.now()
print( "runtime = %s" % (end - start) )