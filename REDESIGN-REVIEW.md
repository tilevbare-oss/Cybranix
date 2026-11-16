# CYBRANIX redesign — review draft

Branch: `redesign/founder-led-consulting` (local only).
Original base: `487ef327fe90671085b638b6417d7e7d518779a2`.

## Positioning and content

- Founder-led practical IT consulting is the primary offer.
- Four focus areas: assessments and roadmaps; project and vendor management; documentation and process improvement; technology training and adoption.
- Small Business IT Review: owner interview, agreed inventory including recurring costs, operational gaps, prioritized recommendations, a 90-day roadmap, and findings walkthrough. Scope, timing and fee are agreed before starting.
- Ongoing advisory is a defined follow-on engagement.
- Existing government hardware/software sourcing content is on `government.html`.
- No clients, testimonials, certifications, partnerships, team members, metrics, or specialist engineering services are invented.
- Founder background uses the supplied briefing. Exact credentials and founder name were not provided and are omitted.

## Design and implementation

Navy, teal, and amber branding retained. Editorial typography, structured service descriptions, and a text-based roadmap replace the image-heavy hero. Original image retained in assets, but not downloaded by either page. Buildless HTML/CSS remains compatible with GitHub Pages; no dependencies, external fonts, tracking, or JavaScript are required for the website.

Accessible landmarks, skip links, focus outlines, reduced-motion support, touch-target styling, mobile layouts, canonical URLs, social metadata, favicon, robots.txt, and sitemap added. Phone link corrected to match the existing displayed number.

## Verification

Passed: local links and fragment targets; one main and h1 per page; unique IDs; phone link targets; primary text/button color contrast; unchanged CNAME and workflow files.

Desktop/mobile browser rendering is unverified: this managed environment exposes no browser QA tool. Responsive rules cover narrow phones through desktop. The inline preview displays the same HTML/CSS with local page switching; preview header positioning is static to suit the conversation.

## Review before release

The introductory-call action requests a time by email. Supply a booking URL if a scheduling service is preferred. No pricing or completion-time claims are made. Confirm founder background and service scope before release.

No push, merge, publishing, DNS edits, Pages settings changes, or custom-domain changes were performed. Main and CNAME are preserved. After approval, inspect authenticated Pages settings and ensure the deployment source remains main before pushing or merging any release.
