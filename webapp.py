from datetime import date
import uuid

today = date.today()
name = 'Bea'
date = today.strftime("%m/%d/%y")
randomID = uuid.uuid4()

print('hello world')
print('my name is ' + name)
print("today's date is " + date)
print("your id is " + str(randomID))
