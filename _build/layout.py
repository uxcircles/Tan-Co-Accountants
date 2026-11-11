"""Shared header, footer, page shell, contact details and UI strings for both languages."""
import hashlib
import json
import os

LANGS = {
    "en": {"dir": "", "html": "en-GB", "label": "EN", "name": "English"},
    "zh": {"dir": "zh/", "html": "zh-Hant", "label": "中文", "name": "繁體中文"},
}

SITE = "https://www.tanandco.co.uk/"
PHONE_DISPLAY = "0121 622 1818"
PHONE_INTL = "+44 121 622 1818"
PHONE_TEL = "+441216221818"
EMAIL = "info@tanandco.co.uk"
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=The+Southside+Building+31+Hurst+Street+Birmingham+B5+4BD"
COMPANY_NO = "07261243"
CH_URL = "https://find-and-update.company-information.service.gov.uk/company/07261243"
FOUNDED = 1975


def L(en, zh):
    return {"en": en, "zh": zh}


def r(x, lang):
    return x[lang] if isinstance(x, dict) else x


def lines(text):
    """Split a headline on '|' into masked lines for the reveal animation."""
    return "".join(f'<span class="line"><span>{part}</span></span>' for part in text.split("|"))


NAV = [
    ("services.html", L("Services", "服務範圍")),
    ("about.html", L("About", "關於我們")),
    ("contact.html", L("Contact", "聯絡我們")),
]

BRAND = L("Tan &amp; Co", "陳智平會計師樓")
ADDRESS = L(["5th Floor, The Southside Building", "31 Hurst Street", "Birmingham B5 4BD"],
            ["伯明翰 Hurst Street 31 號", "The Southside Building 5 樓", "Birmingham B5 4BD"])

UI = {
    "skip": L("Skip to content", "跳至正文"),
    "menu": L("Menu", "選單"),
    "call": L("Call", "致電"),
    "email": L("Email", "電郵"),
    "visit": L("Visit", "地圖"),
    "talk": L("Get in touch", "預約諮詢"),
    "hours": L("Opening hours", "辦公時間"),
    "hours_text": L("Please call to arrange<br>an appointment", "請致電預約<br>會面時間"),
    "office": L("Office", "辦事處"),
    "pages": L("Pages", "頁面"),
    "language": L("Language", "語言"),
    "legal": L("Legal &amp; privacy", "法律聲明及私隱政策"),
    "directions": L("Get directions", "查看地圖"),
    "footer_q": L("Questions about tax|or your accounts?", "稅務或帳目|有任何疑問？"),
    "footer_lead": L("Call, email or drop in at Hurst Street — we reply in English or Chinese.",
                     "歡迎致電、電郵或親臨 Hurst Street 辦事處，我們以中文或英文為您服務。"),
    "reg": L(f"Tan &amp; Co (Birmingham) Ltd · Registered in England and Wales, company no. {COMPANY_NO}",
             f"Tan &amp; Co (Birmingham) Ltd · 於英格蘭及威爾斯註冊，公司編號 {COMPANY_NO}"),
    "top": L("Back to top", "返回頂部"),
    "concept": L("Concept", "概念"),
    "concept_long": L('Concept redesign. Not the <a href="https://tanandco.co.uk/" target="_blank" rel="noopener">official Tan &amp; Co website</a>.',
                      '概念設計展示，並非 <a href="https://tanandco.co.uk/" target="_blank" rel="noopener">陳智平會計師樓官方網站</a>。'),
    "concept_by": L("Designed by ", "設計："),
    "concept_note": L("Unofficial redesign concept by", "非官方概念設計："),
    "since": L("Since 1975", "始於 1975"),
}

# Strings main.js needs (deadlines, calculator, form)
JS_STRINGS = {
    "en": {
        "today": "today", "tomorrow": "tomorrow", "inDays": "in {n} days", "days": "days", "day": "day",
        "until": "until {date}",
        "dl": {
            "jan": "Self Assessment online return and tax due for {ty}",
            "jul": "Second payment on account for {ty}",
            "oct5": "Register for Self Assessment if you started self-employment or letting in {ty}",
            "oct31": "Paper Self Assessment return deadline for {ty}",
            "mtd": "Making Tax Digital quarterly update to {end} (if you’re in MTD)",
        },
        "calc": {"accounts": "Accounts to Companies House", "ctpay": "Corporation Tax payment",
                 "ct600": "Company Tax Return (CT600)", "cs01": "Confirmation statement (within 14 days of)"},
        "mailSubject": "Website enquiry", "mailName": "Name", "mailPhone": "Phone", "mailLang": "Preferred language",
        "mailService": "Service",
    },
    "zh": {
        "today": "今天", "tomorrow": "明天", "inDays": "還有 {n} 天", "days": "天", "day": "天",
        "until": "距離 {date}",
        "dl": {
            "jan": "{ty} 稅務年度網上個人報稅及繳稅截止",
            "jul": "{ty} 稅務年度第二期預繳稅款",
            "oct5": "如於 {ty} 稅務年度開始自僱或出租物業，須登記個人報稅",
            "oct31": "{ty} 稅務年度紙本個人報稅表截止",
            "mtd": "數碼報稅（MTD）季度申報：截至 {end} 的季度（如適用）",
        },
        "calc": {"accounts": "向 Companies House 遞交年度帳目", "ctpay": "繳交公司稅",
                 "ct600": "遞交公司稅申報表（CT600）", "cs01": "確認聲明書（此日期後 14 天內）"},
        "mailSubject": "網站查詢", "mailName": "姓名", "mailPhone": "電話", "mailLang": "希望使用的語言",
        "mailService": "查詢服務",
    },
}

ICON = {
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "arrow-ne": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
}

# The Tan & Co mark, redrawn as SVG from the original 30px logo: a red frame around a brush-stroke "T".
MARK_SVG = """<svg class="mark" viewBox="0 0 30 30" aria-hidden="true">
  <path class="mark-frame" d="M1 1h28v28H1z"/>
  <path class="mark-stroke" d="M7.2 8.9c4.6-.5 10.4-.6 16.4-.7M10.6 10.4C7.4 13.4 5.6 17 6.6 19.9c1.2 3.4 6.1 3.6 11.6 1.4"/>
</svg>"""

# A founder's name seal (姓名印): 陳智平印, read top-right down, then the left column.
SEAL = """<span class="seal" aria-hidden="true"><span>陳</span><span>智</span><span>平</span><span>印</span></span>"""


def lang_switch(lang, page):
    prefix = "../" if LANGS[lang]["dir"] else ""
    items = []
    for code, meta in LANGS.items():
        href = prefix + meta["dir"] + (page if page != "index.html" else "")
        if not href:
            href = "./"
        cur = ' aria-current="true"' if code == lang else ""
        items.append(f'<a href="{href}" lang="{meta["html"]}" hreflang="{meta["html"]}"{cur}>{meta["label"]}</a>')
    return '<div class="lang" role="group" aria-label="Language / 語言">' + "".join(items) + "</div>"


_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ver(rel):
    """Short content hash for cache-busting ?v= query strings."""
    with open(os.path.join(_ROOT, "assets", rel), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


def asset(lang):
    return ("../" if LANGS[lang]["dir"] else "") + "assets/"


def brand_block(lang):
    sub = "陳智平會計師樓" if lang == "en" else "Tan &amp; Co Accountants"
    main = "Tan &amp; Co" if lang == "en" else "陳智平會計師樓"
    return f"""<a class="brand" href="./" aria-label="{'Tan &amp; Co Accountants — home' if lang == 'en' else '陳智平會計師樓 — 主頁'}">
      {MARK_SVG}
      <span class="brand-text"><span class="brand-name">{main}</span><span class="brand-sub" lang="{'zh-Hant' if lang == 'en' else 'en-GB'}">{sub}</span></span>
    </a>"""


def header(lang, page):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{href}"{cur if href == page else ""}>{r(label, lang)}</a>' for href, label in NAV)
    big = "".join(
        f'<li><a href="{href}"{cur if href == page else ""}><span class="mn">0{i}</span>{r(label, lang)}</a></li>'
        for i, (href, label) in enumerate(NAV, 1))
    return f"""<a class="skip" href="#main">{r(UI['skip'], lang)}</a>
<div class="concept-bar" role="note">
  <div class="wrap concept-inner">
    <p><span class="concept-tag">{r(UI['concept'], lang)}</span><span class="concept-long">{r(UI['concept_long'], lang)}</span></p>
    <a href="https://ux-circles.com/professionals" target="_blank" rel="noopener"><span class="concept-by">{r(UI['concept_by'], lang)}</span><strong>UX CIRCLES</strong> {ICON['arrow-ne']}</a>
  </div>
</div>
<header class="site-header" data-header>
  <div class="wrap header-inner">
    {brand_block(lang)}
    <nav class="main-nav" aria-label="Main">{nav}</nav>
    {lang_switch(lang, page)}
    <a class="btn btn-ink header-cta" href="tel:{PHONE_TEL}">{ICON['phone']}<span>{PHONE_DISPLAY}</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="menu-lines"><span></span><span></span></span><span class="sr">{r(UI['menu'], lang)}</span></button>
  </div>
</header>
<div class="menu" id="menu" hidden>
  <div class="wrap menu-inner">
    <ul class="menu-links">{big}</ul>
    <div class="menu-foot">
      <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      {lang_switch(lang, page)}
    </div>
  </div>
</div>"""


def footer(lang, page):
    nav = "".join(f'<li><a href="{h}">{r(lbl, lang)}</a></li>' for h, lbl in NAV)
    nav += f'<li><a href="legal.html">{r(UI["legal"], lang)}</a></li>'
    addr = "<br>".join(r(ADDRESS, lang))
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <h2 class="footer-q split">{lines(r(UI['footer_q'], lang))}</h2>
        <p class="footer-lead">{r(UI['footer_lead'], lang)}</p>
      </div>
      <div class="footer-contact">
        <a class="big-link" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <a class="big-link" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </div>
    <div class="footer-grid">
      <div><h3 class="f-h">{r(UI['office'], lang)}</h3><p>{addr}</p><p><a class="u" href="{MAPS_URL}" rel="noopener" target="_blank">{r(UI['directions'], lang)} ↗</a></p></div>
      <div><h3 class="f-h">{r(UI['hours'], lang)}</h3><p>{r(UI['hours_text'], lang)}</p></div>
      <div><h3 class="f-h">{r(UI['pages'], lang)}</h3><ul class="f-links">{nav}</ul></div>
      <div><h3 class="f-h">{r(UI['language'], lang)}</h3>{lang_switch(lang, page)}</div>
    </div>
  </div>
  <div class="wrap footer-base">
    <span>© <span data-year>2026</span> {r(UI['reg'], lang)}<br><span class="concept-note">{r(UI['concept_note'], lang)} <a class="u" href="https://ux-circles.com/professionals" target="_blank" rel="noopener">UX CIRCLES</a></span></span>
    <a href="#main" class="u">{r(UI['top'], lang)} ↑</a>
  </div>
</footer>
<nav class="action-bar" aria-label="Quick contact">
  <a href="tel:{PHONE_TEL}">{ICON['phone']}<span>{r(UI['call'], lang)}</span></a>
  <a href="mailto:{EMAIL}">{ICON['mail']}<span>{r(UI['email'], lang)}</span></a>
  <a href="{MAPS_URL}" target="_blank" rel="noopener">{ICON['pin']}<span>{r(UI['visit'], lang)}</span></a>
</nav>"""


# Fonts are self-hosted subsets built by _build/fonts.py; preload what the hero needs first.
PRELOAD = {"en": ["fraunces", "instrument-sans"], "zh": ["fraunces", "noto-serif-tc-600"]}


def page(lang, name, title, description, body, body_class=""):
    a = asset(lang)
    meta = LANGS[lang]
    path = "" if name == "index.html" else name
    alts = "\n".join(f'<link rel="alternate" hreflang="{m["html"]}" href="{SITE}{m["dir"]}{path}">' for m in LANGS.values())
    js = json.dumps(JS_STRINGS[lang], ensure_ascii=False)
    preloads = "\n".join(f'<link rel="preload" href="{a}fonts/{f}.woff2" as="font" type="font/woff2" crossorigin>'
                         for f in PRELOAD[lang])
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "AccountingService",
        "name": "Tan & Co Accountants", "alternateName": ["陳智平會計師樓", "Tan & Co (Birmingham) Ltd"],
        "url": SITE, "telephone": PHONE_INTL, "email": EMAIL, "foundingDate": str(FOUNDED),
        "founder": {"@type": "Person", "name": "Philip Tan"},
        "address": {"@type": "PostalAddress", "streetAddress": "5th Floor, The Southside Building, 31 Hurst Street",
                    "addressLocality": "Birmingham", "postalCode": "B5 4BD", "addressCountry": "GB"},
        "areaServed": ["West Midlands", "United Kingdom"], "knowsLanguage": ["en", "zh"],
    }, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="{meta['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE}{meta['dir']}{path}">
{alts}
<link rel="alternate" hreflang="x-default" href="{SITE}{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'en_GB' if lang == 'en' else 'zh_HK'}">
<meta name="theme-color" content="#f4efe5">
<link rel="icon" href="{a}img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{a}img/favicon.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="{a}img/apple-touch-icon.png">
{preloads}
<link rel="stylesheet" href="{a}css/style.css?v={ver("css/style.css")}">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{schema}</script>
</head>
<body class="{body_class}">
{header(lang, name)}
<main id="main">
{body}
</main>
{footer(lang, name)}
<script>window.TANCO = {js};</script>
<script src="{a}js/main.js?v={ver("js/main.js")}" defer></script>
</body>
</html>
"""
