import sys
import time
import json
from src.livechart import LiveChart

try:
    url = sys.argv[1]
    result = LiveChart().result(url)
    filename = url.split('/')[-2] + "_" + url.split('/')[-1] + "_" + str(time.time()) + ".json"

    f = open(filename, "w")
    f.write(json.dumps(result))
    f.close

    print(result)
except:
    print("Something went wrong.")
    print("Make sure you enter the command like this:")
    print("py main.py https://www.livechart.me/winter-2020/tv")