# VK Music — Landing Page

A single-page, dark-mode landing page for an independent music artist. Built with plain HTML5 and CSS3 — no frameworks, no build step, no dependencies.

## Files

- `index.html` — page markup and content
- `style.css` — all styling (Flexbox layout, colors, responsive rules)
- `VK-Music-Content.pdf` — quick-reference list of all editable text (tagline, track names, email, etc.)

## Run it

Just open `index.html` in a browser. No server or install required.

## Structure

- **Header** — sticky nav (Tracks / About / Contact)
- **Hero** — brand name, tagline, logo placeholder, "Listen Now" CTA
- **Tracks** — 4 track cards with title, meta, and a Play button (UI only, not wired to audio)
- **About** — short bio blurb
- **Footer** — booking email + social links (also serves as the Contact section)

## Customizing

- **Colors/theme**: edit the CSS variables at the top of `style.css` (`:root` block)
- **Logo**: replace `.logo-placeholder` div in `index.html` with an `<img>` tag
- **Tracks**: duplicate/edit `.track-card` blocks in `index.html`
- **Email/socials**: update the `mailto:` link and social `href="#"` links in the footer
- **Play buttons**: currently non-functional placeholders — hook up an audio player or streaming links as needed

## Notes

- Fully responsive via Flexbox; one media query at 600px handles minor mobile tweaks
- Uses system fonts only (no external font/library requests)
- Code is commented throughout to explain layout decisions
