ToolKit Pro

A small web app I built for myself (and anyone else who needs it) — a calculator that doesn't round things off, a chess game you can actually play, and a currency converter that works without installing anything.

Live at **[toolkitpro.co.in](https://toolkitpro.co.in)**

---

Why I made this

I got tired of phone calculators switching to scientific notation the moment numbers got big. I wanted something that just... shows the full number. So I built one. Then added chess because why not. Then currency converter because a friend asked.

---

What's inside

**Calculator** — Uses Big.js under the hood so it never loses precision. No scientific notation, no rounding surprises. Has a basic and scientific mode, plus a history log.

**Chess** — Play against the computer (Easy / Medium / Hard) or pass the phone to a friend for 2-player mode. Has undo, flip board, and pawn promotion.

**Currency Converter** — Pulls real-time exchange rates for 160+ currencies. Just pick two currencies, enter an amount, done.

---

Stack

Pure HTML, CSS, and JavaScript. No React, no Vue, no build tools. Just files.

- [Big.js](https://github.com/MikeMcl/big.js/) for the precision math
- [Supabase](https://supabase.com) for auth (optional — guest mode works without an account)
- GitHub Pages for hosting
- Custom domain via Cloudflare

---

Pages

```
index.html      → main app
privacy.html    → privacy policy
terms.html      → terms of service
contact.html    → contact page
404.html        → custom error page
sitemap.xml     → for search engines
robots.txt      → crawl rules
ads.txt         → adsense verification
```

---

Accounts

You don't need one. Guest mode gives full access to all tools. If you do make an account, you can save your display name and change your password from the profile page.

---

Contact

Instagram: [@fix_before_flex](https://www.instagram.com/fix_before_flex)  
Email: support@toolkitpro.co.in

---

*Built by Siddhartha — first web project, still improving it.*
