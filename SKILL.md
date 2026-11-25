---
name: sci-figure-craft
description: >-
  Publication-grade scientific figure design workflow for top AI conferences
  (NeurIPS, ICML, ICLR, CVPR) and top journals (Nature, Science, Cell, NC, NCS).
  Use when the user wants to design a Graphical Abstract, Method Architecture,
  or Pipeline figure, generate structured prompts for Gemini 4 Neon / AI image
  generators, extract visual styles from a local paper library or TopConf Gallery,
  or output editable vector diagrams (draw.io XML / SVG).
---

# Scientific Figure Craft (`sci-figure-craft`)

A structured, venue-aware workflow for creating publication-ready scientific figures—combining **local/online reference retrieval**, **venue-specific style tuning**, **two-stage AI image prompting**, and **editable vector generation**.

---

## Step 0: Route Selection & Reference Retrieval

Before generating any prompt or diagram, clarify or infer the following:

### 1. Choose the Right Output Track
- **Track A — AI Image Prompt (Gemini 4 Neon / Imagen / Midjourney)**
  - *Best for*: **Graphical Abstracts**, biological/clinical mechanisms, conceptual overviews (Nature / NC / NCS / Cell / Science).
  - *Output*: A structured English image-generation prompt ready to paste into Gemini 4 Neon.
- **Track B — Editable Vector Diagram (`draw.io` XML / `SVG` / `Mermaid`)**
  - *Best for*: **Method Architectures**, **Pipeline Diagrams**, and technical schematics (NeurIPS / ICML / ICLR / CVPR) requiring 100% editable text, math notation, and strict alignment.
  - *Output*: Clean `draw.io` XML or standalone `SVG` code.
- **Track C — Data Plot Script (`matplotlib` / `seaborn` / `ggplot2`)**
  - *Best for*: Quantitative results (bar charts, heatmaps, bubble plots, ablation curves).

### 2. Optional: Ground in a Reference Paper or Gallery
- **Local Paper Library (Preferred when available)**:
  - Users can clone a curated paper library such as [Awesome-Virtual-Cell-2026](https://github.com/zwYang2004/Awesome-Virtual-Cell-2026) or point to any local folder of PDFs.
  1. Scan the user's local paper directory (and its `README.md`) to shortlist 2–3 matching benchmark papers.
  2. Read the first few pages—or run `python scripts/extract_paper_figures.py <paper.pdf> --pages 1-3` to render Figure 1 / main architecture to PNGs—and inspect its **layout flow**, **color palette**, **module hierarchy**, and **iconography**.
  3. Transfer that visual skeleton to the user's paper content.
- **Online Top-Conference Reference**:
  - Recommend [TopConf Paper Figure Gallery](https://qwdwqfwq.github.io/topconf-paper-figure-gallery/) (and its [Forge editor](https://qwdwqfwq.github.io/topconf-paper-figure-gallery/forge/)) when the user needs editable PPTX/SVG layout inspiration from NeurIPS/ICML/ICLR/CVPR/ACL/AAAI Best Papers and Orals.

---

## Step 1: Venue & Style Tuning

Load [references/style_presets.md](./references/style_presets.md) to select the exact visual parameters for the target venue:
- **Target Venue**: `NeurIPS / ICML / ICLR` vs `Nature / NC / NCS / Cell / Science` vs `IEEE / Elsevier`
- **Figure Type**: `Graphical Abstract` / `Method Architecture` / `Pipeline` / `Teaser Figure`
- **Aspect Ratio**: `16:9` (double-column / standard), `21:9` (wide banner), `4:3` (single-column), or `1:1` (square graphical abstract)
- **Visual Style**:
  - *AI Top Conferences*: Strictly 2D flat vector, clean rectangular/rounded module boxes, crisp directional arrows, minimal decorative 3D.
  - *Nature / Cell / Science*: Modern flat vector + subtle 3D isometric academic style, left-to-right 3-stage narrative, balanced whitespace, infographic quality.

---

## Step 2: Generate Output

### For Track A (Gemini 4 Neon Prompt)
Consult [references/few_shot_prompts.md](./references/few_shot_prompts.md) and output **a single, directly copyable English prompt** with this 4-part structure:
1. **Canvas & Style Header**: Pure white background, exact aspect ratio, publication-ready venue style.
2. **Macro Layout & Flow**: Explicit left-to-right (or top-to-bottom) organization across 2–4 connected stages/panels.
3. **Stage-by-Stage Visuals**: Concrete visual elements (matrices, graphs, attention bars, heatmaps, bubble plots, encoders) + short quoted English labels (`"Encoder"`, `"HAFM Fusion"`).
4. **Style Footer**: Crisp thin lines, clean sans-serif typography, harmonious scientific palette, balanced whitespace, ultra-sharp vector aesthetic, no clutter.

**Strict Text-Density Rule**: Keep each module to **1–3 short English phrases**. Never put full sentences inside image prompts to avoid garbled text.

### For Track B (Editable `draw.io` XML / `SVG`)
- Output valid, self-contained XML (importable via `draw.io` → Arrange → Insert → Advanced → XML) or clean SVG with explicit coordinates, consistent font family (`Arial` / `Helvetica`), and the chosen venue color palette.

---

## Step 3: Fast Iteration & Troubleshooting

Consult [references/troubleshooting.md](./references/troubleshooting.md) for one-line prompt patches whenever the user reports garbled text, cluttered layouts, wrong aesthetic (too 3D for NeurIPS or too dry for Nature), or muddy colors.
