# Troubleshooting & Prompt Patch Playbook

When an AI-generated figure (e.g., from Gemini 4 Neon) has visual flaws, append or swap the corresponding patch below instead of rewriting from scratch.

| Issue | Root Cause | Quick Fix (Append / Swap in Prompt) |
| :--- | :--- | :--- |
| **Garbled or misspelled text** | Too many labels or long sentences inside quotes | Keep max 1–3 words per label; append `minimal text, only short uppercase/title-case labels`. For final submission, overlay clean text boxes in Keynote / PowerPoint / Illustrator. |
| **Cluttered / overcrowded layout** | Too many sub-components in one stage | Append `minimalist, generous whitespace, simplified iconography, clean spacious layout, max 3 stages`. |
| **Too cartoonish / illustrative for NeurIPS or ICLR** | Trigger words like `3D`, `glowing`, or `infographic` | Replace with `strictly 2D flat vector technical schematic, clean rectangular module boxes, uniform thin black/navy strokes, no 3D effects, no glowing effects`. |
| **Too dry / lacks "Nature" polish** | Generic boxes without domain visuals | Add concrete scientific sub-visuals: `crisp heatmap`, `enrichment bubble plot`, `volcano plot`, `molecular network graph`, `cell membrane schematic`. |
| **Muddy or clashing colors** | Unconstrained color generation | Lock the palette explicitly: `harmonious scientific palette limited to deep navy, teal, soft purple, and coral on a pure white (#FFFFFF) background`. |
| **Broken arrows / unclear flow** | Ambiguous spatial ordering | Explicitly specify `flowing strictly from left to right across three clearly separated panels (Left panel, Middle panel, Right panel) connected by bold directional arrows`. |
