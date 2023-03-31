# import pandas as pd
# print(pd.to_datetime(pd.to_datetime('now',utc=True).tz_localize('Asia/Kolkata').value).strftime('%Y/%m/%d %H:%M:%S'))

# import time

# #sleep
# time.sleep(10)
# print("Sup boi")


# threading

import threading

class Bazinga:
    def add(self,a,b):
        print(a+b)
    
    def bakchodi(self):
        thread = threading.Thread(target=self.add,args=(1,2))
        thread.start()
        print("Bakchodi")


sheldon = Bazinga()
sheldon.bakchodi()