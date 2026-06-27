import urllib.request

urls = []

with open("links.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            urls.append(line)

configs = set()

for url in urls:
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            text = r.read().decode("utf-8", errors="ignore")
            for line in text.splitlines():
                line = line.strip()
                if line:
                    configs.add(line)
    except Exception as e:
        print(f"Error: {url} -> {e}")

with open("sub.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(configs)))

print(f"Saved {len(configs)} configs.")
