"""Builds every page in both languages. Run: python3 _build/pages.py"""
import os

from content import APPROACH, CLIENTS, SERVICES, TIMELINE
from layout import (ADDRESS, CH_URL, EMAIL, FOUNDED, ICON, L, LANGS, MAPS_URL, PHONE_DISPLAY, PHONE_TEL, SEAL, lines,
                    page, r)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def arrow_btn(href, text, cls="btn btn-red"):
    return f'<a class="{cls}" href="{href}"><span>{text}</span>{ICON["arrow"]}</a>'


def page_hero(lang, eyebrow, title, lead):
    return f"""<section class="page-hero">
  <div class="wrap">
    <p class="label reveal-up">{eyebrow}</p>
    <h1 class="page-title split">{lines(title)}</h1>
    <p class="page-lead reveal-up">{lead}</p>
  </div>
</section>"""


def deadlines_section(lang):
    t = {
        "label": L("Key dates", "重要日期"),
        "title": L("Next HMRC|deadline", "下一個 HMRC|截止日期"),
        "after": L("Coming up after that", "之後的截止日期"),
        "note": L("Dates for Self Assessment and Making Tax Digital for Income Tax, worked out from today. Penalties start at £100 for a late return.",
                  "以今天日期計算的個人報稅及所得稅數碼報稅截止日期。逾期遞交報稅表，罰款由 £100 起。"),
    }
    return f"""<section class="section deadlines" id="key-dates" aria-labelledby="kd-h">
  <div class="wrap dl-grid" data-countdown>
    <div>
      <p class="label reveal-up">{r(t['label'], lang)}</p>
      <h2 class="h2 split" id="kd-h">{lines(r(t['title'], lang))}</h2>
      <p class="muted reveal-up">{r(t['note'], lang)}</p>
    </div>
    <div class="dl-card reveal-up">
      <p class="dl-big"><span data-cd-days>—</span> <span class="dl-unit" data-cd-unit></span></p>
      <p class="dl-until" data-cd-until></p>
      <p class="dl-what" data-cd-what></p>
      <h3 class="dl-after">{r(t['after'], lang)}</h3>
      <ol class="dl-list" data-deadlines></ol>
    </div>
  </div>
</section>"""


# ------------------------------------------------------------------ home
def home(lang):
    t = {
        "eyebrow": L("Hurst Street, Birmingham Chinatown · since 1975", "伯明翰唐人街 Hurst Street · 始於 1975"),
        "title": L("Accounts, tax|and sound advice|<em>since 1975.</em>", "專業會計|稅務諮詢|<em>始於 1975。</em>"),
        "lead": L("The first accountancy firm in the West Midlands for the Chinese community — now looking after businesses and families across the UK, in English and Chinese.",
                  "英國中西部首間為華人社區服務的會計師樓，至今已為全英各地的商業及家庭客戶服務，以中文及英文溝通。"),
        "cta": L("Book a consultation", "預約諮詢"),
        "cta2": L("Our services", "服務範圍"),
        "years": L("years in Birmingham", "年專業經驗"),
        "est": L("Founded by Philip Tan, 1975", "由陳智平先生於 1975 年創立"),
        "phone": L("Phone", "電話"), "email": L("Email", "電郵"), "visit": L("Visit", "地址"),
        "visit_v": L("31 Hurst Street, B5", "Hurst Street 31 號"),
        "next": L("Next HMRC deadline", "下一個 HMRC 截止日期"),
        "first_label": L("Who we are", "關於我們"),
        "first_title": L("The West Midlands’|first firm for the|Chinese community", "英國中西部|首間華人|會計師樓"),
        "first_p1": L("Philip Tan opened Tan &amp; Co in 1975 to give Chinese families and businesses in Birmingham an accountant who understood them. Half a century on, the firm has built its name on experience and a consistently high standard of client service.",
                      "陳智平先生於 1975 年創立本會計師樓，為伯明翰的華人家庭及生意提供真正了解他們的會計服務。半個世紀以來，我們憑豐富經驗及一貫優質的服務建立信譽及口碑。"),
        "first_p2": L("Most of our clients are businesses — limited companies, partnerships and sole traders — alongside individuals and charities. Many have been with us for decades.",
                      "我們的主要客戶為商業客戶，包括有限公司、合夥及個人生意，亦有個人客戶及非牟利慈善團體，不少客戶已與我們合作數十年。"),
        "first_link": L("Our story", "我們的故事"),
        "serve": L("We work with", "服務對象"),
        "svc_label": L("Services", "服務範圍"),
        "svc_title": L("Three things,|done properly", "三大服務|做到最好"),
        "svc_more": L("Details", "了解詳情"),
        "app_label": L("Our approach", "我們的宗旨"),
        "app_title": L("Client-focused,|goal-oriented", "以客為本|目標為先"),
    }
    svc_rows = "".join(f"""
      <li class="svc-row reveal-up">
        <a href="services.html#{s['id']}">
          <span class="svc-n">{s['n']}</span>
          <h3 class="svc-t">{r(s['title'], lang).replace('|', '<br>')}</h3>
          <p class="svc-d">{r(s['short'], lang)}</p>
          <span class="svc-go">{r(t['svc_more'], lang)} {ICON['arrow']}</span>
        </a>
      </li>""" for s in SERVICES)
    approach = "".join(f"""
      <li class="app-item reveal-up"><span class="app-n">{a['n']}</span><h3>{r(a['title'], lang)}</h3><p>{r(a['body'], lang)}</p></li>""" for a in APPROACH)
    clients = "".join(f"<li>{r(c, lang)}</li>" for c in CLIENTS)
    body = f"""
<section class="hero" data-hero>
  <div class="wrap hero-inner">
    <div class="hero-main">
      <p class="label hero-eyebrow reveal-up">{r(t['eyebrow'], lang)}</p>
      <h1 class="hero-title split">{lines(r(t['title'], lang))}</h1>
      <p class="hero-lead reveal-up">{r(t['lead'], lang)}</p>
      <div class="hero-actions reveal-up">
        {arrow_btn('contact.html', r(t['cta'], lang))}
        <a class="btn-text" href="services.html">{r(t['cta2'], lang)}</a>
      </div>
    </div>
    <aside class="ledger reveal-up" aria-label="{'At a glance' if lang == 'en' else '一覽'}">
      {SEAL}
      <div class="ledger-head">
        <p class="ledger-years"><span data-since="{FOUNDED}">51</span><span class="ledger-yl">{r(t['years'], lang)}</span></p>
        <p class="ledger-est">{r(t['est'], lang)}</p>
      </div>
      <ul class="ledger-rows">
        <li><a href="tel:{PHONE_TEL}"><span class="lr-l">{ICON['phone']}{r(t['phone'], lang)}</span><span class="lr-v">{PHONE_DISPLAY}</span></a></li>
        <li><a href="mailto:{EMAIL}"><span class="lr-l">{ICON['mail']}{r(t['email'], lang)}</span><span class="lr-v">{EMAIL}</span></a></li>
        <li><a href="{MAPS_URL}" target="_blank" rel="noopener"><span class="lr-l">{ICON['pin']}{r(t['visit'], lang)}</span><span class="lr-v">{r(t['visit_v'], lang)}</span></a></li>
      </ul>
      <a class="ledger-dl" href="#key-dates" data-next-deadline hidden>
        <span class="lr-k">{r(t['next'], lang)}</span>
        <span class="ledger-dl-row"><b data-dl-date></b><span class="ledger-in" data-dl-in></span></span>
      </a>
    </aside>
  </div>
</section>

<section class="section first" aria-labelledby="first-h">
  <div class="wrap split-grid">
    <div>
      <p class="label reveal-up">{r(t['first_label'], lang)}</p>
      <h2 class="h2 split" id="first-h">{lines(r(t['first_title'], lang))}</h2>
    </div>
    <div class="prose">
      <p class="reveal-up lead-p">{r(t['first_p1'], lang)}</p>
      <p class="reveal-up">{r(t['first_p2'], lang)}</p>
      <h3 class="mini-h reveal-up">{r(t['serve'], lang)}</h3>
      <ul class="tags reveal-up">{clients}</ul>
      <p class="reveal-up"><a class="btn-text" href="about.html">{r(t['first_link'], lang)}</a></p>
    </div>
  </div>
</section>

<section class="section services-home" aria-labelledby="svc-h">
  <div class="wrap">
    <div class="sec-head">
      <p class="label reveal-up">{r(t['svc_label'], lang)}</p>
      <h2 class="h2 split" id="svc-h">{lines(r(t['svc_title'], lang))}</h2>
    </div>
    <ul class="svc-list">{svc_rows}
    </ul>
  </div>
</section>

<section class="section dark approach" aria-labelledby="app-h">
  <div class="wrap">
    <div class="sec-head">
      <p class="label reveal-up">{r(t['app_label'], lang)}</p>
      <h2 class="h2 split" id="app-h">{lines(r(t['app_title'], lang))}</h2>
    </div>
    <ol class="app-list" data-progress>{approach}
    </ol>
  </div>
</section>
{deadlines_section(lang)}
"""
    title = L("Tan &amp; Co Accountants — Birmingham Chinatown since 1975 | 陳智平會計師樓",
              "陳智平會計師樓 — 伯明翰唐人街華人會計師樓，始於 1975 | Tan &amp; Co")
    desc = L("Accountants on Hurst Street, Birmingham since 1975 — the West Midlands’ first firm for the Chinese community. Tax, VAT, company formation, accounts and payroll, in English and Chinese.",
             "陳智平會計師樓自 1975 年起扎根伯明翰 Hurst Street，是英國中西部首間華人會計師樓。提供稅務、增值稅、公司成立、帳目及薪酬服務，中英文溝通。")
    return page(lang, "index.html", r(title, lang), r(desc, lang), body, "home")


# ------------------------------------------------------------------ services
def services(lang):
    t = {
        "eyebrow": L("Services", "服務範圍"),
        "title": L("Everything your|accounts need", "帳目及稅務|一站式服務"),
        "lead": L("Three areas of work, one team. Most clients use all three — we keep the books, file the returns and advise on what comes next.",
                  "三大服務範疇，同一個團隊。大部分客戶三項服務都會使用：我們處理簿記、遞交申報，並就未來發展提供意見。"),
        "good": L("Good to know", "最新資訊"),
        "on": L("On this page", "本頁內容"),
        "ask": L("Ask about this", "查詢此服務"),
        "calc_label": L("Limited company dates", "有限公司截止日期"),
        "calc_title": L("When are your|company’s deadlines?", "您的公司|何時截止？"),
        "calc_lead": L("Enter your company’s financial year end to see when its accounts, tax payment and tax return are due.",
                       "輸入公司的財政年度結束日，即可查看帳目、公司稅及報稅表的截止日期。"),
        "calc_input": L("Financial year end", "財政年度結束日"),
        "calc_note": L("Assumes a company that has already filed its first accounts and has taxable profits under £1.5 million. Your first accounts have different deadlines — ask us.",
                       "以已遞交首份帳目、應課稅利潤低於 £150 萬的公司計算。首份帳目的截止日期不同，請向我們查詢。"),
        "rates_h": L("Corporation Tax rates", "公司稅稅率"),
        "rates": L([("19%", "Small profits rate — profits up to £50,000"), ("25%", "Main rate — profits over £250,000"),
                    ("19–25%", "Marginal relief in between")],
                   [("19%", "小型利潤稅率：利潤不超過 £50,000"), ("25%", "主要稅率：利潤超過 £250,000"), ("19–25%", "介乎兩者之間可享邊際寬免")]),
        "vat_h": L("VAT threshold", "增值稅門檻"),
        "vat": L("Register when taxable turnover goes over <b>£90,000</b> in any 12 months. You can deregister below £88,000.",
                 "任何 12 個月內應課稅營業額超過 <b>£90,000</b> 須註冊增值稅；低於 £88,000 可申請註銷。"),
    }
    toc = "".join(f'<li><a href="#{s["id"]}"><span>{s["n"]}</span>{r(s["title"], lang).replace("|", " ")}</a></li>' for s in SERVICES)
    sections = ""
    for s in SERVICES:
        items = "".join(f"<li>{ICON['check']}<span>{r(i, lang)}</span></li>" for i in s["items"])
        sections += f"""
  <section class="svc-section" id="{s['id']}" aria-labelledby="{s['id']}-h">
    <div class="svc-side">
      <span class="svc-big-n" aria-hidden="true">{s['n']}</span>
      <h2 class="h2 split" id="{s['id']}-h">{lines(r(s['title'], lang))}</h2>
    </div>
    <div class="svc-body">
      <p class="lead-p reveal-up">{r(s['intro'], lang)}</p>
      <ul class="checks reveal-up">{items}</ul>
      <aside class="note reveal-up"><p class="note-k">{r(t['good'], lang)}</p><p>{r(s['note'], lang)}</p></aside>
      <p class="reveal-up"><a class="btn-text" href="contact.html?service={s['id']}">{r(t['ask'], lang)}</a></p>
    </div>
  </section>"""
    rates = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in r(t["rates"], lang))
    body = f"""
{page_hero(lang, r(t['eyebrow'], lang), r(t['title'], lang), r(t['lead'], lang))}
<div class="wrap svc-layout">
  <nav class="toc" aria-label="{r(t['on'], lang)}"><p class="label">{r(t['on'], lang)}</p><ul>{toc}</ul></nav>
  <div class="svc-sections">{sections}
  </div>
</div>

<section class="section paper-2 calc-sec" id="calculator" aria-labelledby="calc-h">
  <div class="wrap split-grid">
    <div>
      <p class="label reveal-up">{r(t['calc_label'], lang)}</p>
      <h2 class="h2 split" id="calc-h">{lines(r(t['calc_title'], lang))}</h2>
      <p class="muted reveal-up">{r(t['calc_lead'], lang)}</p>
      <div class="facts reveal-up">
        <h3 class="mini-h">{r(t['rates_h'], lang)}</h3>
        <dl class="rates">{rates}</dl>
        <h3 class="mini-h">{r(t['vat_h'], lang)}</h3>
        <p>{r(t['vat'], lang)}</p>
      </div>
    </div>
    <div class="calc reveal-up">
      <form data-ct-calc>
        <label for="ye">{r(t['calc_input'], lang)}</label>
        <input id="ye" type="date" required>
      </form>
      <dl class="calc-out" data-ct-out aria-live="polite"></dl>
      <p class="calc-note">{r(t['calc_note'], lang)}</p>
    </div>
  </div>
</section>
{deadlines_section(lang)}
"""
    title = L("Services — tax, VAT, company formation, accounts &amp; payroll | Tan &amp; Co Birmingham",
              "服務範圍 — 稅務、增值稅、成立公司、帳目及薪酬 | 陳智平會計師樓")
    desc = L("Self Assessment, Corporation Tax, VAT and Making Tax Digital; company formation and restructuring; bookkeeping, year-end accounts and payroll. Tan &amp; Co, Birmingham.",
             "個人報稅、公司稅、增值稅及數碼報稅；成立及重組公司；簿記、年結帳目及薪酬服務。陳智平會計師樓，伯明翰。")
    return page(lang, "services.html", r(title, lang), r(desc, lang), body, "services")


# ------------------------------------------------------------------ about
def about(lang):
    t = {
        "eyebrow": L("About", "關於我們"),
        "title": L("Half a century|in Birmingham", "扎根伯明翰|半個世紀"),
        "lead": L("Tan &amp; Co has been part of Birmingham’s Chinese community since 1975. The firm Philip Tan started now works from Hurst Street in Birmingham Chinatown, and is still built around the same idea: really understand the client, then do the work properly.",
                  "陳智平會計師樓自 1975 年起服務伯明翰華人社區。陳智平先生創立的會計師樓現位於伯明翰唐人街 Hurst Street，一直秉承同一理念：真正了解客戶，把工作做好。"),
        "tl_label": L("Our story", "我們的故事"),
        "tl_title": L("From one office|to clients UK-wide", "由伯明翰|服務至全英"),
        "app_label": L("How we work", "工作方式"),
        "app_title": L("Client-focused,|goal-oriented", "以客為本|目標為先"),
        "app_p": L("We listen to what each client needs and focus on their goals. Because no two clients are alike, we don’t offer a blanket service: we work closely with each one and tailor what we do so it actually delivers.",
                   "我們細心聆聽每位客戶的需要，專注於他們的目標。每位客戶都不一樣，所以我們不提供「一刀切」的服務，而是與客戶緊密合作，度身訂造，真正達到目標。"),
        "it_p": L("We also invest in up-to-date technology. Secure servers and digital records cut down on paper, help us file returns quickly — avoiding late-filing penalties — and keep your information safe.",
                  "我們亦投資於最新的資訊科技。安全的伺服器及電子紀錄減少文書工作，讓我們更快遞交報稅表及 VAT 申報表，減少逾期罰款及錯誤，並確保您的個人資料不會外洩。"),
        "who": L("Who we work with", "服務對象"),
        "who_p": L("Our clients are mainly businesses — companies and individual traders — together with individuals and a number of charities and not-for-profit organisations.",
                   "我們的主要客戶為商業客戶，例如企業公司及個人生意，亦有個人客戶以及一些非牟利慈善團體。"),
        "cta": L("Talk to us", "聯絡我們"),
    }
    tl = "".join(f"""
      <li class="tl-item reveal-up"><span class="tl-y">{r(y, lang)}</span><p>{r(txt, lang)}</p></li>""" for y, txt in TIMELINE)
    approach = "".join(f"""
      <li class="app-item reveal-up"><span class="app-n">{a['n']}</span><h3>{r(a['title'], lang)}</h3><p>{r(a['body'], lang)}</p></li>""" for a in APPROACH)
    clients = "".join(f"<li>{r(c, lang)}</li>" for c in CLIENTS)
    body = f"""
{page_hero(lang, r(t['eyebrow'], lang), r(t['title'], lang), r(t['lead'], lang))}

<section class="section" aria-labelledby="tl-h">
  <div class="wrap split-grid">
    <div class="sticky">
      <p class="label reveal-up">{r(t['tl_label'], lang)}</p>
      <h2 class="h2 split" id="tl-h">{lines(r(t['tl_title'], lang))}</h2>
      <div class="about-seal reveal-up">{SEAL}<p class="muted">{'The founder’s name seal — 陳智平, Philip Tan.' if lang == 'en' else '創辦人陳智平先生的姓名印。'}</p></div>
    </div>
    <ol class="timeline" data-progress>{tl}
    </ol>
  </div>
</section>

<section class="section dark approach" aria-labelledby="app-h">
  <div class="wrap">
    <div class="split-grid">
      <div>
        <p class="label reveal-up">{r(t['app_label'], lang)}</p>
        <h2 class="h2 split" id="app-h">{lines(r(t['app_title'], lang))}</h2>
      </div>
      <div class="prose">
        <p class="reveal-up lead-p">{r(t['app_p'], lang)}</p>
        <p class="reveal-up">{r(t['it_p'], lang)}</p>
      </div>
    </div>
    <ol class="app-list">{approach}
    </ol>
  </div>
</section>

<section class="section" aria-labelledby="who-h">
  <div class="wrap split-grid">
    <h2 class="h2 split" id="who-h">{lines(r(t['who'], lang))}</h2>
    <div class="prose">
      <p class="reveal-up lead-p">{r(t['who_p'], lang)}</p>
      <ul class="tags reveal-up">{clients}</ul>
      <p class="reveal-up">{arrow_btn('contact.html', r(t['cta'], lang))}</p>
    </div>
  </div>
</section>
"""
    title = L("About — Birmingham’s Chinese-community accountants since 1975 | Tan &amp; Co",
              "關於我們 — 1975 年創立的伯明翰華人會計師樓 | 陳智平會計師樓")
    desc = L("Founded by Philip Tan in 1975, Tan &amp; Co was the first accountancy firm in the West Midlands for the Chinese community. Still on Hurst Street, Birmingham.",
             "陳智平會計師樓由陳智平先生於 1975 年創立，是英國中西部首間服務華人社區的會計師樓，至今仍在伯明翰 Hurst Street。")
    return page(lang, "about.html", r(title, lang), r(desc, lang), body, "about")


# ------------------------------------------------------------------ contact
def contact(lang):
    t = {
        "eyebrow": L("Contact", "聯絡我們"),
        "title": L("Come and see us|on Hurst Street", "歡迎親臨|Hurst Street"),
        "lead": L("Call or email to book a consultation, in English or Chinese. Tell us a little about what you need and we’ll come back to you.",
                  "歡迎致電或電郵預約諮詢，中英文均可。請簡單告訴我們您的需要，我們會盡快回覆。"),
        "phone": L("Phone", "電話"), "email": L("Email", "電郵"), "office": L("Office", "辦事處"),
        "directions": L("Get directions", "查看地圖"),
        "getting": L("Getting here", "交通"),
        "getting_p": L("We’re on Hurst Street in Birmingham Chinatown, on the 5th floor of The Southside Building, a short walk from Birmingham New Street station.",
                       "辦事處位於伯明翰唐人街 Hurst Street，The Southside Building 5 樓，由 Birmingham New Street 火車站步行即達。"),
        "form_h": L("Send an enquiry", "網上查詢"),
        "name": L("Name", "姓名"), "f_email": L("Email", "電郵"), "f_phone": L("Phone (optional)", "電話（選填）"),
        "service": L("What can we help with?", "需要哪方面的協助？"),
        "lang_q": L("Preferred language", "希望使用的語言"),
        "message": L("Message", "內容"),
        "send": L("Write email", "撰寫電郵"),
        "err": L("Please add your name, a valid email address and a message.", "請填寫姓名、有效的電郵地址及查詢內容。"),
        "form_note": L("This opens your email app with the enquiry filled in — nothing is sent until you press send there.",
                       "按下後將開啟您的電郵程式並自動填上內容，您在電郵程式中按「傳送」後才會寄出。"),
        "opts": L(["Tax compliance &amp; planning", "Business start-up or reorganisation", "Accounts, bookkeeping or payroll", "Something else"],
                  ["稅務申報及規劃", "業務成立或重組", "帳目、簿記或薪酬", "其他"]),
        "langs": L(["English", "Chinese 中文"], ["中文", "English 英文"]),
    }
    ids = ["tax", "startups", "accounts", "other"]
    opts = "".join(f'<option value="{o}" data-id="{i}">{o}</option>' for o, i in zip(r(t["opts"], lang), ids))
    langs = "".join(f'<option>{o}</option>' for o in r(t["langs"], lang))
    addr = "<br>".join(r(ADDRESS, lang))
    body = f"""
{page_hero(lang, r(t['eyebrow'], lang), r(t['title'], lang), r(t['lead'], lang))}
<section class="section contact-sec">
  <div class="wrap contact-grid">
    <div class="contact-details">
      <dl class="cd">
        <div class="reveal-up"><dt>{r(t['phone'], lang)}</dt><dd><a class="big-link" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></dd></div>
        <div class="reveal-up"><dt>{r(t['email'], lang)}</dt><dd><a class="big-link" href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div class="reveal-up"><dt>{r(t['office'], lang)}</dt><dd><address>Tan &amp; Co Accountants<br>{addr}</address><a class="btn-text" href="{MAPS_URL}" target="_blank" rel="noopener">{r(t['directions'], lang)}</a></dd></div>
        <div class="reveal-up"><dt>{r(t['getting'], lang)}</dt><dd><p>{r(t['getting_p'], lang)}</p></dd></div>
      </dl>
    </div>
    <form class="form reveal-up" data-contact-form novalidate>
      <h2 class="form-h">{r(t['form_h'], lang)}</h2>
      <div class="field"><label for="f-name">{r(t['name'], lang)}</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field-row">
        <div class="field"><label for="f-email">{r(t['f_email'], lang)}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-phone">{r(t['f_phone'], lang)}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="f-service">{r(t['service'], lang)}</label><select id="f-service" name="service">{opts}</select></div>
        <div class="field"><label for="f-lang">{r(t['lang_q'], lang)}</label><select id="f-lang" name="lang">{langs}</select></div>
      </div>
      <div class="field"><label for="f-msg">{r(t['message'], lang)}</label><textarea id="f-msg" name="message" rows="5" required></textarea></div>
      <p class="form-err" data-form-error hidden role="alert">{r(t['err'], lang)}</p>
      <button class="btn btn-red" type="submit"><span>{r(t['send'], lang)}</span>{ICON['arrow']}</button>
      <p class="form-note">{r(t['form_note'], lang)}</p>
    </form>
  </div>
</section>
"""
    title = L("Contact — 31 Hurst Street, Birmingham B5 4BD | Tan &amp; Co Accountants",
              "聯絡我們 — 伯明翰 Hurst Street 31 號 | 陳智平會計師樓")
    desc = L("Call 0121 622 1818 or email info@tanandco.co.uk. 5th Floor, The Southside Building, 31 Hurst Street, Birmingham B5 4BD.",
             "致電 0121 622 1818 或電郵 info@tanandco.co.uk。地址：伯明翰 Hurst Street 31 號 The Southside Building 5 樓，B5 4BD。")
    return page(lang, "contact.html", r(title, lang), r(desc, lang), body, "contact")


# ------------------------------------------------------------------ legal
def legal(lang):
    zh_note = '<p class="note-inline">本頁以英文為準，中文為摘要。</p>' if lang == "zh" else ""
    zh_sum = """
      <h2>摘要</h2>
      <p>本網站內容僅供一般參考，並不構成專業意見；法律及稅務規定會不時改變，請就您的情況向我們查詢。我們只會為回覆您的查詢及提供服務而使用您提供的個人資料，並按英國《通用資料保護條例》（UK GDPR）處理。如欲查閱、更正或刪除您的資料，請電郵 info@tanandco.co.uk。</p>""" if lang == "zh" else ""
    body = f"""
{page_hero(lang, r(L('Legal', '法律聲明'), lang), r(L('Legal &amp; privacy', '法律聲明及|私隱政策'), lang), r(L('The small print, in plain English.', '條款細則。'), lang))}
<section class="section">
  <div class="wrap legal prose" lang="en-GB">
    {zh_note}{zh_sum}
    <h2 id="disclaimer">Disclaimer</h2>
    <p>The information on this website is general guidance on matters that may interest you. It is not professional advice and should not be relied on as such. We work to keep it current and accurate, but tax rules, thresholds and deadlines change, so please speak to us about your own circumstances before acting.</p>
    <p>To the fullest extent permitted by law, Tan &amp; Co (Birmingham) Ltd accepts no liability for any loss arising from use of this website or reliance on its content. Nothing here excludes liability that cannot be excluded by law.</p>
    <h2 id="privacy">Privacy</h2>
    <p>Tan &amp; Co (Birmingham) Ltd is the data controller for personal information you give us through this website, by email or by phone.</p>
    <h3>What we collect</h3>
    <p>Your name, contact details and whatever you tell us in your enquiry. This website does not use advertising or tracking cookies.</p>
    <h3>Why we use it</h3>
    <p>To reply to your enquiry and, if you become a client, to provide our services and meet our legal and professional obligations (including anti-money-laundering checks). We do not sell your information or use it for marketing without your consent.</p>
    <h3>How long we keep it</h3>
    <p>Enquiries that don’t lead to work are deleted within 12 months. Client records are kept for as long as the law and our professional rules require.</p>
    <h3>Your rights</h3>
    <p>You can ask to see, correct or delete your information, or object to how we use it, by emailing <a class="u" href="mailto:{EMAIL}">{EMAIL}</a>. If you are unhappy with our response you can complain to the <a class="u" href="https://ico.org.uk/make-a-complaint/" target="_blank" rel="noopener">Information Commissioner’s Office</a>.</p>
    <h2 id="company">Company information</h2>
    <p>Tan &amp; Co (Birmingham) Ltd, registered in England and Wales, company number <a class="u" href="{CH_URL}" target="_blank" rel="noopener">07261243</a>. Registered office: 5th Floor, The Southside Building, 31 Hurst Street, Birmingham B5 4BD.</p>
  </div>
</section>
"""
    title = L("Legal &amp; privacy | Tan &amp; Co Accountants", "法律聲明及私隱政策 | 陳智平會計師樓")
    desc = L("Website disclaimer, privacy notice and company information for Tan &amp; Co (Birmingham) Ltd.",
             "Tan &amp; Co (Birmingham) Ltd 網站免責聲明、私隱政策及公司資料。")
    return page(lang, "legal.html", r(title, lang), r(desc, lang), body, "legal")


PAGES = {"index.html": home, "services.html": services, "about.html": about, "contact.html": contact, "legal.html": legal}

if __name__ == "__main__":
    for lang, meta in LANGS.items():
        out_dir = os.path.join(ROOT, meta["dir"])
        os.makedirs(out_dir, exist_ok=True)
        for name, fn in PAGES.items():
            with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
                f.write(fn(lang))
            print("wrote", meta["dir"] + name)
