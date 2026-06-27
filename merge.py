import base64
import requests

with open("links.txt", "r", encoding="utf-8") as f:
    urls = [i.strip() for i in f if i.strip()]

configs = []

for url in urls:
    try:
        text = requests.get(url, timeout=20).text.strip()

        try:
            text = base64.b64decode(text + "==").decode()
        except:
            pass

        for line in text.splitlines():
            line = line.strip()
            if line:
                configs.append(line)

    except Exception as e:
        print(e)

configs = list(dict.fromkeys(configs))

result = "\n".join(configs)

encoded = base64.b64encode(result.encode()).decode()

with open("sub.txt", "w") as f:
    f.write(encoded)
