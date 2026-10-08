---
name: BLE Portfolio
description: Graphite exhibition for stylized 3D worlds and characters
colors:
  accent: "#ff7964"
  accent-hover: "#ff9585"
  bg: "#191c1e"
  surface: "#232729"
  text: "#f3f0e7"
  muted: "#b7b8b4"
  line: "#44484a"
  media-bg: "#101315"
typography:
  display:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "clamp(3.4rem, 7.6vw, 6rem)"
    fontWeight: 600
    lineHeight: 1.03
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "clamp(2.7rem, 5vw, 4.7rem)"
    fontWeight: 600
    lineHeight: 1.03
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Manrope, sans-serif"
    fontSize: "19px"
    fontWeight: 600
    lineHeight: 1.35
  body:
    fontFamily: "Manrope, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Manrope, sans-serif"
    fontSize: "14px"
    fontWeight: 700
rounded:
  sharp: "0"
  control: "4px"
spacing:
  compact: "8px"
  label: "18px"
  inset: "24px"
  gutter: "32px"
  section-heading: "40px"
  gallery-row: "64px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.bg}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "13px 24px"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.bg}"
    rounded: "{rounded.control}"
  button-close:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.control}"
    padding: "8px 14px"
  navigation:
    textColor: "{colors.text}"
  filter:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    padding: "8px 0"
  filter-active:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    padding: "8px 0"
  work-selector:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    padding: "10px 0"
  work-selector-active:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    padding: "10px 0"
  project-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.sharp}"
---
# Design System: BLE Portfolio

## Overview

**Creative North Star: "Graphite Exhibition"**

Graphite Exhibition gives BLE's stylized characters and environments the scale of a screening room. Warm white condensed headlines sit against graphite; coral identifies actions and selected states. Artwork supplies the remaining color and visual complexity.

The interface uses flat exhibit surfaces, generous intervals and compact reading text. Rectangular media frames hold the work; quiet controls support exploring images, films and orbitable models.

**Key Characteristics:**

- Graphite surfaces and warm white reading text.
- Condensed display type paired with open sans-serif body text.
- Coral actions and selected-state underlines.
- Large rectangular artwork, flat depth and restrained motion.

## Colors

A charcoal neutral field allows the supplied work to remain the visual authority.

### Primary

Coral accent marks primary actions, links, emphasis and the selected control. Its lighter hover value signals interactivity.

### Neutral

Graphite background carries the page. The raised graphite surface groups contact and media; dark media background supports films and models. Warm white carries reading text, muted gray carries supporting metadata, and the line color separates sections.

**The Artwork Color Rule.** Let the work supply the broad color range; use coral for actions, emphasis and selected states.

## Typography

Barlow Condensed supplies the large display and headline roles; Manrope supplies body, titles and controls. Both use sans-serif fallback. The display is tightly tracked and balanced, while reading text remains open and calm.

The frontmatter records the default display, headline, project-card title, body and primary-control roles. Individual project headings use a wider display clamp, and profile/contact headings have their own observed large-size variants. Supporting labels and captions range from 12px to 14px; card titles reduce to 17px on phones. Body paragraphs are limited to 70ch, with project introductions limited to 58ch.

## Layout

The desktop work index uses a twelve-column grid with alternating seven/five and six/six spans. Filtering restores equal six-column spans. Horizontal gutters use the gutter token; rows use the gallery-row token. Main content uses responsive outer padding of max(32px, 7vw); section gaps are intentionally larger than the internal rhythm.

At 900px the header contracts, metadata stacks and process notes become two columns. At 600px the index and galleries become single-column, main content uses the inset token, profile stacks and the stage becomes a portrait composition with artwork above the copy. The first project-gallery artwork spans both columns on larger screens. Images in inspection views use containment so the work remains legible.

The exhibition uses viewport-aware height bounded by minimum and maximum heights. Model viewing occupies 580px on larger screens and 400px on phones.

## Elevation & Depth

The interface has no drop shadows. Tonal changes, artwork overlays, whitespace and thin section rules create depth. The exhibition uses dark gradients to preserve text contrast; the image dialog uses a dark translucent backdrop. These are contextual media treatments rather than general card decoration.

**The Flat Exhibit Rule.** Separate surfaces through tone, spacing and thin rules; do not add interface drop shadows.

## Shapes

Media frames, project cards and the image dialog have square corners. Primary and close controls use the control radius. Thin borders and selected-state underlines provide structure; frames avoid enclosing every item in an outlined box.

## Components

Primary links are solid coral with graphite text and compact softened corners. Hover lightens coral; press compresses to 0.97 scale. Keyboard focus uses a 2px coral outline offset by 6px. The close-image button is transparent with a thin line-colored border.

Navigation is compact text, coral on hover, with a short underline reveal on fine-pointer devices. Filters use muted text at rest and warm white with a thin coral underline when active. The work selector follows the same language with a thicker selected underline and semibold text. These controls expose their selected state through aria-pressed.

Project cards combine a rectangular image and a separate title/metadata row. Fine motion uses a 1.035 image zoom over 550ms and a coral title hover. Filters hide unmatched projects immediately and announce the visible count.

The featured-work selector decodes incoming artwork before swapping its image, accessible description and link. The outgoing layer dissolves over 180ms with ease-out; newer requests supersede older requests. Reduced motion swaps immediately. General control transitions use 180ms, with the source easing curve for transforms.

Images open in a native modal dialog with explicit close, Escape support and focus restoration. Films use native video controls. Model-viewer keeps a poster until the user requests the real model, exposes loading progress and shows an error with a direct-file fallback when needed.

**The Motion Access Rule.** Honor reduced motion with immediate state changes and no image zoom or button compression.

## Do's and Don'ts

### Do:

- **Do** keep supplied artwork and attribution visible in the project experience.
- **Do** use condensed headlines and Manrope for reading and controls.
- **Do** preserve square media frames, coral focus outlines and selected-state underlines.
- **Do** keep video playback native and load interactive models on demand.

### Don't:

- **Don't** add decorative drop shadows to exhibit surfaces.
- **Don't** force artwork into the interface palette.
- **Don't** animate state changes when reduced motion is requested.

