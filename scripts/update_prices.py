"""Reads the CBAM certificate prices published by the European Commission
and writes them to prices.json, which the calculator loads when it opens."""
import json, re, sys, urllib.request, datetime, html

URL = "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en"

def parse(page):
    text = html.unescape(re.sub(r"<[^>]+>", " ", page))
    text = re.sub(r"\s+", " ", text)
    rows = re.findall(r"(Q[1-4] 20\d\d) (\d{1,2} [A-Z][a-z]+ 20\d\d) (\d{2,3}[.,]\d{1,2})", text)
    out, seen = [], set()
    for q, pub, price in rows:
        if q in seen:
            continue
        seen.add(q)
        out.append({"q": q, "published": pub, "price": round(float(price.replace(",", ".")), 2)})
    return out

def main():
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (CBAM calculator price check)"})
    page = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    prices = parse(page)
    if not prices:
        print("No prices found; keeping the existing prices.json")
        sys.exit(0)
    data = {"updated": datetime.date.today().isoformat(), "source": URL, "cbam": prices}
    with open("prices.json", "w") as f:
        json.dump(data, f, indent=2)
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
