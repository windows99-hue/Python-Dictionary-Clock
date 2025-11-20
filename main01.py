from datetime import datetime
import pytz
from colorama import init, Fore, Back, Style

n = datetime.now()

# 定义#FFD866黄色（RGB: 255, 216, 102）
def yellow_hex(text):
    return f"\033[38;2;255;216;102m{text}\033[0m"

# 定义#AB9DF2紫色（RGB: 171, 157, 242）
def purple_hex(text):
    return f"\033[38;2;171;157;242m{text}\033[0m"

# 定义#78DCE8青色并斜体（RGB: 120, 220, 232）
def cyan_italic(text):
    return f"\033[3;38;2;120;220;232m{text}\033[0m"

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

# 输出 - 修改这一行，给dict加上斜体和颜色
print(Fore.WHITE+"clock"+Fore.RESET+Fore.RED+":"+Fore.RESET+cyan_italic(" dict ")+Fore.RED+"="+Fore.RESET+" {")
items = list(clock.items())
for i, (key, value) in enumerate(items):
    if i < len(items) - 1:
        print(f'    '+ yellow_hex(f'"{key}"') +Fore.RED+": "+Fore.RESET+value+",")
    else:
        print(f'    '+ yellow_hex(f'"{key}"') +Fore.RED+": "+Fore.RESET+value)
print("}")