# JCB-Reflex

Personal portfolio built with Reflex (Python web framework).

## Stack

- **Reflex 0.9.5.post2** (not 0.8.x — README is stale)
- **React Router 7** + **Tailwind CSS v4** + **Radix UI** in `.web/`
- Single-file app: `JCB_Reflex/JCB_Reflex.py` (all components, no sub-packages)
- Static assets: `assets/` (images, CSS, CV PDF) — not `.web/`

## Commands

```bash
reflex run              # dev: frontend :3000, backend :8000
reflex export --frontend-only   # static build for shared hosting
reflex export           # full export with backend
```

## Dev workflow

- Edit `JCB_Reflex/JCB_Reflex.py` for app changes
- Edit `assets/custom.css` for styles
- Edit `assets/img/` for images
- `.web/` is auto-generated — do not edit directly
- `rxconfig.py` sets app name and plugins (Tailwind v4, Sitemap)

## Architecture notes

- All UI components defined in one file as top-level functions
- Two state classes: `State` (mobile menu toggle), `ThemeState` (dark/light)
- Theme toggle uses CSS variable `var(--navbar-bg)` — not Tailwind config
- Contact form uses FormSubmit.co (no backend required for form submission)
- Portfolio projects link to external demos (Render apps have cold-start lag)

## Static deployment (Namecheap/cPanel)

```bash
reflex export --frontend-only
# upload .web/build/client/ contents to public_html
```

State/Backend features do not work in static export. FormSubmit handles form submission client-side.
