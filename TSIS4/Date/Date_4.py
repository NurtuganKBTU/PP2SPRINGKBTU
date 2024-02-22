import datetime

monday = datetime.datetime.now()
friday = datetime.datetime(2023,2,16,12,12,42)
print((monday - friday).total_seconds())