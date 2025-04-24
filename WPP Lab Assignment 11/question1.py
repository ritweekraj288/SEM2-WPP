# import pandas as pd
# import datetime
# a = pd.Timestamp("2012-01-15")
# print("Date time object for Jan 15 2012:", a)
# b= pd.Timestamp("2012-01-15 21:20:00")
# print("Specific date and time of 9:20 pm:", b)
# c = pd.Timestamp.now()
# print("Local date and time:", c)
# d = pd.Timestamp("2012-01-15").date()
# print("A date without time:", d)
# e = pd.Timestamp.today().date()
# print("Current date:", e)
# f = pd.Timestamp("2012-01-15 21:20:00").time()
# print("Time from a date time:", f)
# g = datetime.datetime.now().time()
# print("Current local time:", g)


import pandas as pd
import datetime

# (a) DateTime object for Jan 15, 2012
date_a = pd.Timestamp("2012-01-15")

# (b) Specific date and time of 9:20 PM
date_b = pd.Timestamp("2012-01-15 21:20")

# (c) Local date and time
date_c = pd.Timestamp.now()

# (d) A date without time
date_d = date_c.date()

# (e) Current date
date_e = pd.Timestamp.today().date()

# (f) Time from a datetime
date_f = date_c.time()

# (g) Current local time
date_g = datetime.datetime.now().time()

# Display results
print("a) DateTime object for Jan 15, 2012:", date_a)
print("b) Specific date and time of 9:20 PM:", date_b)
print("c) Local date and time:", date_c)
print("d) A date without time:", date_d)
print("e) Current date:", date_e)
print("f) Time from a datetime:", date_f)
print("g) Current local time:", date_g)