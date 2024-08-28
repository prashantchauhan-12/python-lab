from datetime import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist)

formatted_time = current_time.strftime("%a %B %d %H:%M:%S IST %Y")
print(formatted_time)
