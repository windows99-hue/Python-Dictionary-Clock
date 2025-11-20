from datetime import datetime
import pytz
from colorama import init, Fore, Back, Style
import time
import os
import sys

init()

def yellow_hex(text):
    return f"\033[38;2;255;216;102m{text}\033[0m"

def purple_hex(text):
    return f"\033[38;2;171;157;242m{text}\033[0m"

def cyan_italic(text):
    return f"\033[3;38;2;120;220;232m{text}\033[0m"

def get_clock_output():
    n = datetime.now()

    clock: dict = {
        "hour": purple_hex(str(n.hour)),
        "minute": purple_hex(str(n.minute)),
        "second": purple_hex(str(n.second)),
        "day": "[" + purple_hex(str(n.day)) + ", " + yellow_hex("\"" + ["Monday", "Tuesday", "Wednesday", 
                "Thursday", "Friday", "Saturday", "Sunday"][n.weekday()] + "\"") + "]",
        "month": yellow_hex("\"" + ["January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December"][n.month - 1] +"\""),
        "year": purple_hex(str(n.year)),
        "timezone": yellow_hex("\"" + f"GMT{'+' if (offset := int(datetime.now().astimezone().strftime('%z')) // 100) >= 0 else ''}{offset}" + "\"")
    }

    output_lines = []
    output_lines.append(Fore.WHITE + "clock" + Fore.RESET + Fore.RED + ":" + Fore.RESET + cyan_italic(" dict ") + Fore.RED + "=" + Fore.RESET + " {")
    items = list(clock.items())
    for i, (key, value) in enumerate(items):
        if i < len(items) - 1:
            output_lines.append(f'    ' + yellow_hex(f'"{key}"') + Fore.RED + ": " + Fore.RESET + value + ",")
        else:
            output_lines.append(f'    ' + yellow_hex(f'"{key}"') + Fore.RED + ": " + Fore.RESET + value)
    output_lines.append("}")
    
    return output_lines

def live_clock():
    try:
        output_lines = get_clock_output()
        for line in output_lines:
            print(line)
        
        total_lines = len(output_lines)
        
        while True:
            time.sleep(0.5)
            
            for i in range(total_lines):
                sys.stdout.write("\033[F")
            
            new_output = get_clock_output()
            
            for line in new_output:
                print(line)
                
    except KeyboardInterrupt:
        print("\n" + yellow_hex("时钟已停止"))

if __name__ == "__main__":
    live_clock()