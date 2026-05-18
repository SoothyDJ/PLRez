"""
PLRez daily stats emailer.
Queries GoatCounter API for yesterday's data, emails a digest to soothiedj@gmail.com.

Required env vars (set as GitHub repo secrets):
  GC_CODE    — GoatCounter site code  (e.g. "plrez")
  GC_TOKEN   — GoatCounter API token
  GMAIL_PASS — Gmail App Password (16-char, not your regular password)
"""

import json
import os
import smtplib
import urllib.error
import urllib.request
from datetime import date, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

RECIPIENT = "soothiedj@gmail.com"

yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
gc_code   = os.environ["GC_CODE"]
gc_token  = os.environ["GC_TOKEN"]
gmail_pass = os.environ["GMAIL_PASS"]


def api(path: str) -> dict:
    url = (
        f"https://{gc_code}.goatcounter.com/api/v0/{path}"
        f"?start={yesterday}&end={yesterday}&limit=10"
    )
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {gc_token}"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"GoatCounter API {e.code}: {e.read().decode()}")
        return {}
    except Exception as e:
        print(f"Request failed: {e}")
        return {}


def table(items: list, key: str, n: int = 8) -> str:
    rows = []
    for item in (items or [])[:n]:
        label = item.get(key) or "(direct)"
        count = item.get("count", 0)
        rows.append(f"  {label:<48} {count:>4}")
    return "\n".join(rows) if rows else "  (none)"


total     = api("stats/total")
hits      = api("stats/hits")
refs      = api("stats/refs")
countries = api("stats/countries")

tv = total.get("total", 0)
tu = total.get("total_unique", 0)

pages_text   = table(hits.get("hits", []),            "path")
refs_text    = table(refs.get("refs", []),             "ref")
country_text = table(countries.get("countries", []),  "country")

body = f"""\
PLRez Daily Stats — {yesterday}
{"=" * 46}

Visits:          {tv}
Unique visitors: {tu}

TOP PAGES
{pages_text}

TOP REFERRERS
{refs_text}

COUNTRIES
{country_text}

Dashboard:   https://pl-rez.vercel.app
GoatCounter: https://{gc_code}.goatcounter.com
"""

msg = MIMEMultipart()
msg["Subject"] = f"PLRez Stats {yesterday} — {tv} visits ({tu} unique)"
msg["From"]    = RECIPIENT
msg["To"]      = RECIPIENT
msg.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(RECIPIENT, gmail_pass)
    smtp.sendmail(RECIPIENT, RECIPIENT, msg.as_string())

print(f"Done. Sent stats for {yesterday}: {tv} visits, {tu} unique.")
