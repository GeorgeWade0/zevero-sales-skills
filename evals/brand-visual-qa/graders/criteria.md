---
type: llm
weight: 1
---

Regression case from feedback: visuals were shown with broken-looking graphs and wonky formatting, and had to be sent back.

Pass only if ALL hold:
1. Before presenting, the response renders or otherwise inspects the output (screenshot, headless render, or an explicit check of the rendered result), not only the source code.
2. The reply states briefly what was checked (charts, labels, spacing or layout) and any fixes made.
3. The HTML uses Manrope and Zevero brand colours (e.g. #004646, #002321, #f7ff8a), not generic default palettes.
4. Charts have labelled axes and a legend or direct labels; no empty chart containers.
5. Placeholder numbers are clearly labelled as placeholders; no real prices or customer names are invented.
