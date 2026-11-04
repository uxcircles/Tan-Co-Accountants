"""Site copy, English and Traditional Chinese side by side: L(english, 中文)."""
from layout import L

SERVICES = [
    {
        "id": "tax",
        "n": "01",
        "title": L("Tax compliance|&amp; planning", "稅務申報|及規劃"),
        "short": L("Personal, self-employed, company and VAT returns — filed on time, with planning to keep the bill no higher than it should be.",
                   "個人、自僱、公司及增值稅（VAT）申報準時遞交，並為您合理規劃，不多交一分稅。"),
        "intro": L("Advice and returns for every part of UK tax — personal, corporate and VAT — with planning that stays within the rules and the deadlines.",
                   "全面處理英國個人稅、公司稅及增值稅的申報及諮詢，在合法合規的前提下為您規劃，確保準時遞交。"),
        "items": [
            L("Self Assessment registration and tax returns for individuals, the self-employed and partners",
              "個人、自僱人士及合夥人的個人報稅（Self Assessment）登記及申報"),
            L("Corporation Tax returns (CT600) and company tax planning", "公司稅申報（CT600）及公司稅務規劃"),
            L("Tax planning — using the allowances and reliefs you are entitled to", "稅務規劃：充分運用您可享有的免稅額及寬免"),
            L("Tax appeals, and support through HMRC enquiries and investigations", "稅務上訴，以及協助應對 HMRC 查詢及稅務調查"),
            L("VAT registration, quarterly VAT returns under Making Tax Digital, and deregistration",
              "增值稅（VAT）註冊、按數碼報稅（MTD）遞交季度申報表，以及註銷"),
        ],
        "note": L("<b>Making Tax Digital for Income Tax</b> started on 6 April 2026 for sole traders and landlords with income over £50,000. "
                  "It reaches income over £30,000 from April 2027 and over £20,000 from April 2028 — quarterly updates through compatible software, "
                  "then a final return. We can set you up and file for you.",
                  "<b>所得稅數碼報稅（MTD for Income Tax）</b>已於 2026 年 4 月 6 日起適用於年收入超過 £50,000 的自僱人士及業主；"
                  "2027 年 4 月起擴展至收入超過 £30,000，2028 年 4 月起擴展至超過 £20,000。須以認可軟件每季遞交更新，年底再作最終申報。我們可為您安排及代為申報。"),
    },
    {
        "id": "startups",
        "n": "02",
        "title": L("Business start-ups|&amp; reorganisation", "業務成立|或重組"),
        "short": L("The right structure from day one — sole trader, partnership or limited company — and help when the business changes shape.",
                   "由第一天起選擇合適的業務架構：獨資、合夥或有限公司；業務轉型時亦全程協助。"),
        "intro": L("Whether you are opening your first shop or restructuring a family business, we explain the options and handle the paperwork.",
                   "無論是開設第一間店舖，還是重組家族生意，我們都會清楚解釋各項選擇，並處理一切文件手續。"),
        "items": [
            L("Advice on the best structure for you: sole trader, partnership or limited company",
              "就獨資、合夥或有限公司等架構提供專業意見，助您選擇最適合的方案"),
            L("Company formation and registration with Companies House and HMRC", "成立公司，並向 Companies House 及 HMRC 註冊"),
            L("Share transfers and changes of directors, company secretary and registered address",
              "股份轉讓，以及更改董事、公司秘書及註冊地址"),
            L("Reorganising, incorporating or winding down an existing business", "重組、將現有生意轉為有限公司，或結束業務"),
        ],
        "note": L("<b>Companies House identity checks.</b> Since 18 November 2025, every new company director and person with significant control "
                  "must verify their identity. Existing directors verify when they file their next confirmation statement. We can guide you through it.",
                  "<b>Companies House 身份核實。</b>自 2025 年 11 月 18 日起，所有新任公司董事及重大控制人士必須核實身份；"
                  "現任董事則須在遞交下一份確認聲明書時完成核實。我們可協助您辦理。"),
    },
    {
        "id": "accounts",
        "n": "03",
        "title": L("Accounts preparation|&amp; outsourcing", "帳目編製|及外判服務"),
        "short": L("Bookkeeping, year-end accounts, management accounts and payroll for businesses of every size and sector.",
                   "為各行各業、不同規模的機構提供簿記、年結帳目、管理帳目及薪酬服務。"),
        "intro": L("We prepare accounts for organisations of every size and complexity — from a single takeaway to a group of companies, and charities too.",
                   "我們為不同規模及複雜程度的機構編製帳目，由一間外賣店到集團公司，以至慈善團體。"),
        "items": [
            L("Bookkeeping, and business plans and forecasts for bank loans", "簿記，以及申請銀行貸款所需的生意計劃書及預算"),
            L("Year-end accounts for sole traders, partnerships and limited companies", "獨資、合夥及有限公司的年結帳目"),
            L("Management accounts, so you know where the business stands during the year", "管理帳目，讓您全年掌握業務狀況"),
            L("Payroll and PAYE: payslips, Real Time Information returns to HMRC, P60s, P45s and P11Ds",
              "薪酬及 PAYE：工資單、向 HMRC 實時申報（RTI）、P60、P45 及 P11D"),
            L("Accounts for charities and not-for-profit organisations", "慈善團體及非牟利機構帳目"),
        ],
        "note": L("<b>Limited company deadlines</b> run from your year end: accounts to Companies House within 9 months, Corporation Tax "
                  "9 months and a day, and the CT600 within 12 months. Try the calculator below.",
                  "<b>有限公司的截止日期</b>以財政年度結束日計算：9 個月內向 Companies House 遞交帳目，9 個月零 1 天內繳交公司稅，"
                  "12 個月內遞交 CT600。請試用下方的計算器。"),
    },
]

CLIENTS = [
    L("Limited companies", "有限公司"),
    L("Sole traders &amp; partnerships", "獨資及合夥生意"),
    L("Restaurants, takeaways &amp; retail", "餐館、外賣店及零售"),
    L("Individuals &amp; landlords", "個人及業主"),
    L("Charities &amp; not-for-profits", "慈善及非牟利團體"),
]

APPROACH = [
    {
        "n": "01",
        "title": L("We listen first", "先聆聽"),
        "body": L("No two clients are the same, so we start with your goals — not a standard package.",
                  "每位客戶的需要及目標都不同，所以我們先了解您的目標，而不是套用標準方案。"),
    },
    {
        "n": "02",
        "title": L("Then we tailor", "再度身訂造"),
        "body": L("We reject the blanket approach. The service is shaped around your business, and changes as it does.",
                  "我們拒絕「一刀切」。服務會按您的生意度身訂造，並隨業務發展而調整。"),
    },
    {
        "n": "03",
        "title": L("Digital and secure", "數碼化及安全"),
        "body": L("Modern software and secure servers mean less paper, faster filing and your data kept safe.",
                  "先進的軟件及安全的伺服器，減少文書工作、加快遞交申報，並確保您的資料安全。"),
    },
]

TIMELINE = [
    ("1975", L("Philip Tan founds Tan &amp; Co in Birmingham — the first accountancy firm in the West Midlands set up to serve the Chinese community and its businesses.",
               "陳智平先生於伯明翰創立陳智平會計師樓，是英國中西部首間專為華人社區及華人生意提供服務的會計師樓。")),
    ("2010", L("The practice is incorporated as Tan &amp; Co (Birmingham) Ltd.", "會計師樓註冊成為 Tan &amp; Co (Birmingham) Ltd。")),
    ("2024", L("The Chinese Quarter around Hurst Street, where the office is based, is officially renamed Birmingham Chinatown.",
               "辦事處所在的 Hurst Street 一帶「華人區」正式易名為「伯明翰唐人街」（Birmingham Chinatown）。")),
    (L("Today", "今天"), L("From Hurst Street, serving businesses and individuals across the West Midlands and the rest of the UK.",
                         "以 Hurst Street 辦事處為基地，服務範圍已擴展至英國中西部以至全英各地的商業及個人客戶。")),
]
