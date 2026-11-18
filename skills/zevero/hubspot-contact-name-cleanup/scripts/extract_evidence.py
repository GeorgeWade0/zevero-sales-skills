"""Usage: python3 -I extract_evidence.py <emails_result_file> <contacts.json>
contacts.json: [{"id":..., "email":...}, ...]
Prints compact name evidence per contact from logged HubSpot emails."""
import json, re, sys

def load(path):
    raw = open(path).read()
    d = json.loads(raw)
    if isinstance(d, list):
        d = json.loads(d[0]["text"])
    return d

emails = load(sys.argv[1])["results"]
contacts = json.load(open(sys.argv[2]))

QUOTE = re.compile(r"(\n\s*>|\n.{0,40}\d{4}年\d{1,2}月\d{1,2}日.{0,60}<|\nOn .{0,80}wrote:|\nFrom:|\n差出人|\n-----Original)")

for c in contacts:
    addr = c["email"].lower()
    ev = set()
    for e in emails:
        p = e["properties"]
        text = p.get("hs_email_text") or ""
        frm = (p.get("hs_email_from_email") or "").lower()
        to = (p.get("hs_email_to_email") or "").lower()
        # "Name <addr>" anywhere (quoted headers)
        for m in re.finditer(r"([^\n<>:]{1,30})\s*<" + re.escape(addr) + r">", text, re.I):
            ev.add("HDR: " + m.group(1).strip())
        if frm == addr:
            fn, ln = p.get("hs_email_from_firstname"), p.get("hs_email_from_lastname")
            if fn or ln:
                ev.add(f"FROMFIELD: {ln} {fn}")
            body = QUOTE.split(text)[0]
            ev.add("SIG: " + body[-350:].replace("\n", " / "))
        elif addr in to:
            ev.add("GREET: " + text[:160].replace("\n", " / "))
    print(f"## {c['id']} {addr}")
    for x in list(ev)[:6]:
        print("   ", x[:400])
