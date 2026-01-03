# good morning sir
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

if timestamp == '00:00:00' :
    print("hey! it's midnight")
if timestamp > '00:00:00' and timestamp < '12:00:00':
    print("good morning sir")
if timestamp == '12:00:00':
    print("good noon sir")
if timestamp > '12:00:00' and timestamp < '16:00:00':
    print("good afternoon")
if timestamp > '16:00:00' and timestamp < '17:00:00':
    print("good evening sir")
if timestamp > '17:00:00' and timestamp < '24:00:00':
    print("good night sir")


