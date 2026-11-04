/* Tan & Co — menu, reveals, years count, HMRC deadlines, company date calculator, contact form */
(function () {
  var T = window.TANCO || {};
  var LANG = document.documentElement.lang || "en-GB";
  var LOCALE = LANG.indexOf("zh") === 0 ? "zh-HK" : "en-GB";
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };

  // ---------------------------------------------------------------- header & menu
  var header = $("[data-header]");
  var lastY = window.scrollY;
  function onHeader() {
    var y = window.scrollY;
    header.classList.toggle("is-scrolled", y > 20);
    header.classList.toggle("is-hidden", y > 520 && y > lastY && !document.body.classList.contains("menu-open"));
    lastY = y;
  }
  var btn = $(".menu-btn"), menu = $("#menu");
  function setMenu(open) {
    btn.setAttribute("aria-expanded", String(open));
    document.body.classList.toggle("menu-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (open) { menu.hidden = false; requestAnimationFrame(function () { menu.classList.add("is-open"); }); }
    else { menu.classList.remove("is-open"); setTimeout(function () { if (!menu.classList.contains("is-open")) menu.hidden = true; }, 400); }
  }
  if (btn && menu) {
    btn.addEventListener("click", function () { setMenu(btn.getAttribute("aria-expanded") !== "true"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu.classList.contains("is-open")) { setMenu(false); btn.focus(); } });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  }

  // ---------------------------------------------------------------- London date
  function londonNow() {
    var o = {};
    new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/London", year: "numeric", month: "2-digit", day: "2-digit" })
      .formatToParts(new Date()).forEach(function (p) { o[p.type] = p.value; });
    return { y: +o.year, m: +o.month, d: +o.day };
  }
  var now = londonNow();
  $$("[data-year]").forEach(function (el) { el.textContent = now.y; });
  $$("[data-since]").forEach(function (el) {
    el.setAttribute("data-count", now.y - +el.getAttribute("data-since"));
    el.textContent = el.getAttribute("data-count");
  });

  // ---------------------------------------------------------------- reveals & count-up
  var revealables = $$(".split, .reveal-up");
  var hasIO = "IntersectionObserver" in window;
  if (hasIO && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    revealables.forEach(function (el) {
      if (el.closest(".hero, .page-hero")) requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add("is-in"); }); });
      else io.observe(el);
    });
  } else {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  }
  var cio = hasIO && !reduced ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      cio.unobserve(en.target);
      var el = en.target, end = +el.getAttribute("data-count"), t0 = performance.now();
      (function tick(t) {
        var k = Math.min(1, (t - t0) / 1400), e = 1 - Math.pow(1 - k, 4);
        el.textContent = Math.round(end * e);
        if (k < 1) requestAnimationFrame(tick);
      })(t0);
    });
  }, { threshold: .5 }) : null;
  if (cio) $$("[data-count]").forEach(function (el) { el.textContent = "0"; cio.observe(el); });

  // ---------------------------------------------------------------- scroll-linked progress lines
  var progressEls = $$("[data-progress]");
  var ticking = false;
  function progress(el) {
    var r = el.getBoundingClientRect(), vh = window.innerHeight;
    return Math.max(0, Math.min(1, (vh * .75 - r.top) / (r.height + vh * .25)));
  }
  function onScroll() {
    ticking = false;
    onHeader();
    if (!reduced) progressEls.forEach(function (el) { el.style.setProperty("--p", progress(el).toFixed(3)); });
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();

  // ---------------------------------------------------------------- HMRC deadlines
  function utc(y, m, d) { return new Date(Date.UTC(y, m - 1, d)); }
  var today = utc(now.y, now.m, now.d);
  function fmt(date, opts) { return new Intl.DateTimeFormat(LOCALE, Object.assign({ timeZone: "UTC" }, opts)).format(date); }
  function longDate(date) { return fmt(date, { day: "numeric", month: "long", year: "numeric" }); }
  function shortDate(date) { return fmt(date, { day: "numeric", month: "short", year: "numeric" }); }
  function ty(start) { return start + "/" + String(start + 1).slice(2); }
  function daysUntil(date) { return Math.round((date - today) / 864e5); }
  function inText(n) { return n === 0 ? T.today : n === 1 ? T.tomorrow : (T.inDays || "").replace("{n}", n); }
  var MTD_START = utc(2026, 8, 7); // first quarterly update under MTD for Income Tax
  function upcomingDeadlines(count) {
    var list = [];
    for (var y = now.y - 1; y <= now.y + 2; y++) {
      list.push({ date: utc(y, 1, 31), key: "jan", ty: ty(y - 2) });
      list.push({ date: utc(y, 7, 31), key: "jul", ty: ty(y - 1) });
      list.push({ date: utc(y, 10, 5), key: "oct5", ty: ty(y - 1) });
      list.push({ date: utc(y, 10, 31), key: "oct31", ty: ty(y - 1) });
      // MTD quarterly updates: 7 Aug, 7 Nov, 7 Feb, 7 May for quarters ending 5 Jul, 5 Oct, 5 Jan, 5 Apr
      [[8, 7, 5], [11, 10, 5], [2, 1, 5], [5, 4, 5]].forEach(function (q) {
        list.push({ date: utc(y, q[0], 7), key: "mtd", end: utc(y, q[1], q[2]) });
      });
    }
    return list.filter(function (d) { return d.date >= today && (d.key !== "mtd" || d.date >= MTD_START); })
      .sort(function (a, b) { return a.date - b.date; }).slice(0, count);
  }
  function label(d) {
    var s = T.dl[d.key].replace("{ty}", d.ty || "");
    return d.end ? s.replace("{end}", fmt(d.end, { day: "numeric", month: "long" })) : s;
  }
  if (T.dl) {
    var up = upcomingDeadlines(6);
    $$("[data-next-deadline]").forEach(function (el) {
      $("[data-dl-date]", el).textContent = longDate(up[0].date);
      $("[data-dl-in]", el).textContent = inText(daysUntil(up[0].date));
      el.hidden = false;
    });
    var cd = $("[data-countdown]");
    if (cd) {
      var n = daysUntil(up[0].date);
      var nEl = $("[data-cd-days]", cd);
      nEl.setAttribute("data-count", n);
      nEl.textContent = n;
      if (cio) { nEl.textContent = "0"; cio.observe(nEl); }
      $("[data-cd-unit]", cd).textContent = n === 1 ? T.day : T.days;
      $("[data-cd-until]", cd).textContent = (T.until || "{date}").replace("{date}", longDate(up[0].date));
      $("[data-cd-what]", cd).textContent = label(up[0]);
      var ol = $("[data-deadlines]", cd);
      ol.innerHTML = "";
      up.slice(1).forEach(function (d) {
        var li = document.createElement("li");
        li.innerHTML = '<span class="dl-d"></span><span class="dl-l"></span><span class="dl-in"></span>';
        $(".dl-d", li).textContent = shortDate(d.date);
        $(".dl-l", li).textContent = label(d);
        $(".dl-in", li).textContent = inText(daysUntil(d.date));
        ol.appendChild(li);
      });
    }
  }

  // ---------------------------------------------------------------- limited company deadline calculator
  function addMonths(date, k) {
    var y = date.getUTCFullYear(), m = date.getUTCMonth(), d = date.getUTCDate();
    var lastOfMonth = d === new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
    var targetLast = new Date(Date.UTC(y, m + k + 1, 0)).getUTCDate();
    return new Date(Date.UTC(y, m + k, lastOfMonth ? targetLast : Math.min(d, targetLast)));
  }
  var calc = $("[data-ct-calc]"), out = $("[data-ct-out]");
  if (calc && out && T.calc) {
    var input = $("input", calc);
    input.value = (now.m > 3 ? now.y : now.y - 1) + "-03-31";
    var render = function () {
      var v = input.value.split("-");
      out.innerHTML = "";
      if (v.length !== 3) return;
      var ye = utc(+v[0], +v[1], +v[2]);
      var pay = new Date(addMonths(ye, 9).getTime() + 864e5);
      [["accounts", addMonths(ye, 9)], ["ctpay", pay], ["ct600", addMonths(ye, 12)]].forEach(function (row) {
        var div = document.createElement("div");
        div.innerHTML = "<dt></dt><dd></dd>";
        $("dt", div).textContent = T.calc[row[0]];
        $("dd", div).textContent = longDate(row[1]);
        out.appendChild(div);
      });
    };
    input.addEventListener("change", render);
    input.addEventListener("input", render);
    calc.addEventListener("submit", function (e) { e.preventDefault(); });
    render();
  }

  // ---------------------------------------------------------------- services table of contents
  var tocLinks = $$(".toc a[href^='#']");
  if (tocLinks.length && hasIO) {
    var byId = {};
    tocLinks.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        tocLinks.forEach(function (a) { a.classList.remove("is-active"); });
        var a = byId[en.target.id];
        if (!a) return;
        a.classList.add("is-active");
        if (window.innerWidth <= 960) a.closest("ul").scrollTo({ left: a.offsetLeft - 16, behavior: reduced ? "auto" : "smooth" });
      });
    }, { rootMargin: "-35% 0px -55% 0px" });
    $$(".svc-section").forEach(function (s) { tio.observe(s); });
  }

  // ---------------------------------------------------------------- contact form → email app
  var form = $("[data-contact-form]");
  if (form) {
    var want = (location.search.match(/[?&]service=(\w+)/) || [])[1];
    if (want) $$("option", form.elements.service).forEach(function (o) { if (o.getAttribute("data-id") === want) o.selected = true; });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements, ok = true;
      ["name", "email", "message"].forEach(function (k) {
        var bad = !f[k].value.trim() || (k === "email" && !/^\S+@\S+\.\S+$/.test(f[k].value));
        f[k].setAttribute("aria-invalid", bad ? "true" : "false");
        if (bad) ok = false;
      });
      $("[data-form-error]", form).hidden = ok;
      if (!ok) { $("[aria-invalid='true']", form).focus(); return; }
      var body = [
        f.message.value.trim(), "", "—",
        T.mailName + ": " + f.name.value.trim(),
        "Email: " + f.email.value.trim(),
        f.phone.value.trim() ? T.mailPhone + ": " + f.phone.value.trim() : null,
        T.mailService + ": " + f.service.value,
        T.mailLang + ": " + f.lang.value
      ].filter(function (l) { return l !== null; }).join("\n");
      var subject = T.mailSubject + " — " + f.service.value + " — " + f.name.value.trim();
      window.location.href = "mailto:info@tanandco.co.uk?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }
})();
