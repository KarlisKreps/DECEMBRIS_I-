from datetime import datetime

# Laiks
current_hour = datetime.now().hour

print(f'Pasreizejais laiks: {current_hour}')

if current_hour > 5 and current_hour <= 12: #6:00 - 12:00 rits
    print("Labrīt!")
elif current_hour > 12 and current_hour < 16: #13:00 - 16:00 diena
    print("Labdien!")
else:
    print("Labvakar!") #16:00 - 6:00 vakars