# Tan & Co Accountants (陳智平會計師樓): website redesign

This is a concept redesign of [tanandco.co.uk](https://tanandco.co.uk/) for Tan & Co (Birmingham) Ltd. Philip Tan founded the firm in Birmingham in 1975. It was the first accountancy firm in the West Midlands to serve the Chinese community. The site is plain HTML, CSS and JavaScript, so the repository root can be hosted on any static host (GitHub Pages, Netlify, Cloudflare Pages, Vercel).

## Languages

| Path   | Language            |
|--------|---------------------|
| `/`    | English             |
| `/zh/` | 繁體中文 (Traditional Chinese) |

Every page exists in both languages, with `hreflang` links between them and a language switch in the header, menu and footer.

**Pages:** Home · Services · About · Contact · Legal & privacy

## Run locally

```bash
python3 -m http.server 5190
```

Then open http://localhost:5190.

## Editing

The HTML is generated, which keeps the header, footer and contact details the same across all 10 pages:

- Contact details, header, footer, UI strings: `_build/layout.py`
- Services, approach, client types and timeline (both languages side by side, via `L(english, 中文)`): `_build/content.py`
- Page layouts and headlines: `_build/pages.py`. A `|` in a headline marks a line break for the reveal animation.

Rebuild after editing (Python 3, no dependencies):

```bash
python3 _build/pages.py
```

**Fonts** are self-hosted in `assets/fonts/`:

- Fraunces for headings
- Instrument Sans for body text
- Noto Serif TC for Chinese headings and the seal

The Chinese font contains only the characters used on the site. **After adding or changing Chinese text, run the font build and then rebuild the pages:**

```bash
python3 _build/fonts.py && python3 _build/pages.py
```

## What this fixes on the current site

Reviewed on tanandco.co.uk in November 2026:

- **Everything is on one page**, in full-screen slides. There are no separate URLs for services or contact, and there is no page title or description per topic for Google. On phones the first screen is mostly empty space above the headline.
- **Out-of-date payroll forms.** The Chinese page offers to file *P35* and *P14* returns. HMRC abolished both in 2013, when Real Time Information (RTI) replaced them.
- **The two languages disagree.** The English page says "over 50 years". The Chinese page still says 三十多年 (30-odd years).
- **Year count is off by one.** The "years of experience" counter starts from 1 January 1976, although the firm was founded in 1975.
- **The Chinese page is tagged as English** (`<html lang="en">`), so screen readers and search engines read it as English. The legal text on the Chinese page is also only in English.
- **Typos:** "lastest", "intergrity".
- **Privacy policy dated 19 March 2010.** It predates UK GDPR, mentions contacting people by fax, and gives no data controller, rights or ICO complaint route.
- **No company details.** The company name, registration number and registered office are not shown, although the company trading disclosure rules require them on a company website.
- **No mobile call button**, no structured data, and a `© 1999 – [this year]` copyright line written by JavaScript.

## What the redesign adds

**Design.** The look is built from the firm's own mark, a red square framing a brush-stroke "T", redrawn as SVG. The palette is ink, warm rice paper and seal red, with no stock photos. A founder's name seal (陳智平印) stamps itself onto the home page card. In the ledger card, the number of years sits over a double underline, the way a total is ruled in a ledger.

**Motion** is restrained and switches off entirely for visitors whose device asks for reduced motion:

- Headlines slide up line by line, and paragraphs fade in once
- The seal stamps once
- The years since 1975 and the HMRC countdown count up
- A red progress line runs along the approach steps and down the About timeline

**Useful features:**

- **Ledger card** on the home page with years since 1975 (worked out from today's date), phone, email, directions and the next HMRC deadline
- **Next HMRC deadline** countdown, including Self Assessment and the new **Making Tax Digital for Income Tax** quarterly updates (7 Aug / 7 Nov / 7 Feb / 7 May from August 2026)
- **Limited company deadline calculator**: enter a year end to get the Companies House accounts, Corporation Tax payment and CT600 dates
- Current **Corporation Tax rates** and the **VAT threshold** (£90,000 / £88,000), plus "Good to know" notes on:
  - Making Tax Digital for Income Tax: £50k from 2026, £30k from 2027, £20k from 2028
  - Companies House identity verification, required since 18 November 2025
- Fixed **Call / Email / Visit** bar on phones
- **Contact form** that opens the visitor's email app with the enquiry filled in. "Ask about this" links on the Services page pre-select the service.
- Correct `tel:` and `mailto:` links, `AccountingService` structured data, and a title and description for each page in both languages
- Rewritten **privacy notice** (UK GDPR) and company information

## Structure

```
_build/layout.py     header, footer, page shell, contact details, UI strings, logo and seal
_build/content.py    services, approach, client types, timeline (EN + 繁中)
_build/pages.py      page templates
_build/fonts.py      downloads the self-hosted fonts (Chinese subset via Google Fonts text=)
assets/css/style.css
assets/js/main.js    reveals, menu, years count, deadlines, calculator, contents list, form
assets/img/          favicon (SVG + PNG), apple-touch-icon
```

## For the firm to check before launch

- **Opening hours.** The current site doesn't list them, so the footer says "please call to arrange an appointment". Send the hours and they can be added, along with an open/closed status.
- **Languages spoken.** The site says "English and Chinese". If you'd like Cantonese and/or Mandarin named explicitly, say which ones.
- **Client types.** "Restaurants, takeaways & retail" and "landlords" are inferred from your services and community. Please confirm they are accurate.
- **Professional body.** Add your ACCA, ICAEW or ATT membership (with a verify link) if you'd like it shown. None is claimed at the moment.
- **Timeline.** The 2010 entry uses the Companies House incorporation date, and the 2024 entry refers to the Chinatown renaming. Please add any other milestones you'd like.
- **Privacy notice** is a plain-English draft. Have it reviewed, especially the retention periods.
- **Contact form** has no server and opens the visitor's email app. Swap in Formspree, Netlify Forms or similar if you want submissions without email.
- **Redirect** `/cn/index.html` to `/zh/`.
