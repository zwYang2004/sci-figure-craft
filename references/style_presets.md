# Venue Style Presets & Color Palettes

Use this table to calibrate visual style, aspect ratio, typography, and exact HEX palettes before generating a prompt or vector diagram.

---

## 1. AI Top Conferences (NeurIPS / ICML / ICLR / CVPR / ACL)
- **Typical Figures**: Method Architecture, Model Pipeline, Teaser Figure
- **Aspect Ratio**: `16:9` (double-column), `21:9` (compact wide banner), `4:3` (single-column)
- **Visual Style**: `strictly 2D flat vector technical schematic style, clean rounded rectangular module boxes, sharp directional arrows, crisp uniform stroke width, no 3D effects`
- **Narrative Focus**: Input tensors/tokens → Core modules (Encoder, Attention, Fusion, Loss) → Output predictions; emphasize data flow and dimensional transformations.
- **Recommended Palette**:
  - Deep Navy (text/borders): `#1B365D`
  - Slate Blue (primary modules): `#4A7C9B`
  - Teal (secondary modules): `#2A9D8F`
  - Soft Orange (highlights/loss/attention): `#E76F51`
  - Light Gray (container fills): `#F4F6F9`

---

## 2. Nature / Science / Cell & Sub-journals (NC / NCS / Nature Methods / Nature Biotech)
- **Typical Figures**: Graphical Abstract, Conceptual Framework, Overview Workflow
- **Aspect Ratio**: `16:9` (standard horizontal), `1:1` (square graphical abstract)
- **Visual Style**: `modern flat vector and subtle 3D isometric academic style, Nature journal infographic quality, balanced whitespace, ultra-sharp vector aesthetic`
- **Narrative Focus**: 3-stage left-to-right story:
  1. **Left**: Scientific problem / multi-modal biological or clinical inputs
  2. **Middle**: Core computational or biological mechanism
  3. **Right**: Quantitative performance + biological/clinical discoveries (bar charts, heatmaps, bubble plots, pathway networks)
- **Recommended Palette**:
  - Deep Navy: `#1D3557`
  - Teal: `#2A9D8F`
  - Soft Purple: `#7B68EE`
  - Coral: `#E66C6C`
  - Amber: `#F4A261`
  - Slate Gray: `#6C757D`

---

## 3. Engineering / Reliability / Applied Journals (IEEE / Elsevier)
- **Typical Figures**: System Architecture, Optimization Loop (MDP/Control), State-Space Policy Heatmap
- **Aspect Ratio**: `16:9`
- **Visual Style**: `flat vector and subtle 3D isometric academic style, IEEE/Elsevier journal publication quality, crisp thin lines, minimalist`
- **Recommended Palette**:
  - Deep Navy: `#1A2B4C`
  - Metallic Blue: `#3B6E9C`
  - Teal: `#2A9D8F`
  - Amber: `#E9C46A`
  - Soft Purple: `#8E7DBE`
  - Slate Gray: `#64748B`
