import time 
import sys 
from colorama import init , Fore 
import random 
  
init(autoreset=True)

lyrics = """ my tea,s gone cold and , i wonder why ? i got out of the bed at all 
the morning rain clouds up my window and i cant see at all 
and if i could it,d be all be gray . but your picture on my wall 
it reminds me that its not so bad , not soooo bad """

deep_colors=[  Fore.BLACK ,  Fore.YELLOW ]

for char in lyrics:
    sys.stdout.write(random.choice(deep_colors)+char)
    sys.stdout.flush()
    time.sleep(0.08)
    