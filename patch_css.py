"""
Patch index.html CSS:
  1. Increase font sizes (skip calendar grid elements)
  2. Center-align date column
  3. Narrow date column
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# ── helper ──────────────────────────────────────────────────────────────────
def replace_exact(text, old, new):
    assert old in text, f'NOT FOUND: {old!r}'
    return text.replace(old, new, 1)

html = src

# ── 1. Base font size ────────────────────────────────────────────────────────
html = replace_exact(html,
    'body { font-family: var(--font); background: var(--bg); color: var(--text); font-size: 14px;',
    'body { font-family: var(--font); background: var(--bg); color: var(--text); font-size: 16px;')

# ── 2. Header / Tabs / Cards ─────────────────────────────────────────────────
html = replace_exact(html,
    '.header-title { font-size: 16px;',
    '.header-title { font-size: 18px;')

html = replace_exact(html,
    '.tab-btn { flex: 1; border: none; background: none; font-family: var(--font); font-size: 13px;',
    '.tab-btn { flex: 1; border: none; background: none; font-family: var(--font); font-size: 15px;')

html = replace_exact(html,
    '.card-title { font-size: 12px; font-weight: 600; color: var(--text-sub); letter-spacing: 1px; text-transform: uppercase; }',
    '.card-title { font-size: 14px; font-weight: 600; color: var(--text-sub); letter-spacing: 1px; text-transform: uppercase; }')

# ── 3. Achievement rings ──────────────────────────────────────────────────────
html = replace_exact(html,
    '.ring-name { font-size: 11px;',
    '.ring-name { font-size: 13px;')

# ── 4. Calendar: center + narrow (KEEP font-sizes as-is) ─────────────────────
# 4a. Header first-child: left→center, remove padding-left + min-width, add width:1%
html = replace_exact(html,
    '.cal-table thead th:first-child { text-align: left; padding-left: 8px; border-right: 2px solid var(--border); min-width: 44px; }',
    '.cal-table thead th:first-child { text-align: center; border-right: 2px solid var(--border); width: 1%; white-space: nowrap; }')

# 4b. Day row first-child: remove padding-left override (use default td padding)
html = replace_exact(html,
    '.cal-day-row td:first-child { border-right: 2px solid var(--border); padding-left: 8px; }',
    '.cal-day-row td:first-child { border-right: 2px solid var(--border); }')

# 4c. date-cell: add text-align:center
html = replace_exact(html,
    '.date-cell { white-space: nowrap; }',
    '.date-cell { white-space: nowrap; text-align: center; }')

# ── 5. Memo editing row ───────────────────────────────────────────────────────
html = replace_exact(html,
    '.memo-tag-btn { font-size: 12px;',
    '.memo-tag-btn { font-size: 13px;')

html = replace_exact(html,
    '.memo-textarea { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 8px 10px; font-size: 13px;',
    '.memo-textarea { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 8px 10px; font-size: 15px;')

html = replace_exact(html,
    '.memo-save-btn { background: linear-gradient(135deg, var(--g-from) 0%, var(--g-to) 100%); color: #fff; border: none; border-radius: 50px; padding: 6px 18px; font-size: 12px;',
    '.memo-save-btn { background: linear-gradient(135deg, var(--g-from) 0%, var(--g-to) 100%); color: #fff; border: none; border-radius: 50px; padding: 6px 18px; font-size: 13px;')

html = replace_exact(html,
    '.memo-cancel-btn { background: none; border: 1px solid var(--border); border-radius: 8px; padding: 6px 12px; font-size: 12px;',
    '.memo-cancel-btn { background: none; border: 1px solid var(--border); border-radius: 8px; padding: 6px 12px; font-size: 13px;')

# ── 6. Month memo / text blocks ───────────────────────────────────────────────
html = replace_exact(html,
    '.section-label { font-size: 12px;',
    '.section-label { font-size: 13px;')

html = replace_exact(html,
    '.big-textarea { width: 100%; border: 1px solid var(--border); border-radius: 10px; padding: 12px; font-size: 14px;',
    '.big-textarea { width: 100%; border: 1px solid var(--border); border-radius: 10px; padding: 12px; font-size: 16px;')

html = replace_exact(html,
    '.edit-link { background: none; border: none; color: var(--accent); font-size: 12px;',
    '.edit-link { background: none; border: none; color: var(--accent); font-size: 13px;')

html = replace_exact(html,
    '.text-content { font-size: 14px;',
    '.text-content { font-size: 16px;')

html = replace_exact(html,
    '.text-empty { font-size: 13px;',
    '.text-empty { font-size: 15px;')

html = replace_exact(html,
    '.btn-cancel-sm { background: none; border: 1px solid var(--border); border-radius: 50px; padding: 7px 18px; font-size: 13px;',
    '.btn-cancel-sm { background: none; border: 1px solid var(--border); border-radius: 50px; padding: 7px 18px; font-size: 15px;')

html = replace_exact(html,
    '.btn-save { background: linear-gradient(135deg, var(--g-from) 0%, var(--g-to) 100%); color: #fff; border: none; border-radius: 50px; padding: 7px 22px; font-size: 13px;',
    '.btn-save { background: linear-gradient(135deg, var(--g-from) 0%, var(--g-to) 100%); color: #fff; border: none; border-radius: 50px; padding: 7px 22px; font-size: 15px;')

# ── 7. Month review ───────────────────────────────────────────────────────────
html = replace_exact(html,
    '.month-review-label { font-size: 13px;',
    '.month-review-label { font-size: 15px;')

html = replace_exact(html,
    '.month-review-body { font-size: 14px;',
    '.month-review-body { font-size: 16px;')

# ── 8. Annual tab ─────────────────────────────────────────────────────────────
html = replace_exact(html,
    '.year-heading { font-size: 18px; font-weight: 700; }',
    '.year-heading { font-size: 20px; font-weight: 700; }')

html = replace_exact(html,
    '.annual-table th { padding: 8px 10px; font-size: 12px;',
    '.annual-table th { padding: 8px 10px; font-size: 13px;')

html = replace_exact(html,
    '.annual-table td { padding: 8px 10px; border-bottom: 1px solid var(--border); text-align: center; font-size: 13px; }',
    '.annual-table td { padding: 8px 10px; border-bottom: 1px solid var(--border); text-align: center; font-size: 15px; }')

html = replace_exact(html,
    '.chip { display: inline-block; border-radius: 6px; padding: 2px 6px; font-weight: 700; font-size: 12px; }',
    '.chip { display: inline-block; border-radius: 6px; padding: 2px 6px; font-weight: 700; font-size: 13px; }')

html = replace_exact(html,
    '.chip-em { color: var(--text-sub); font-size: 11px; }',
    '.chip-em { color: var(--text-sub); font-size: 12px; }')

# ── 9. Body composition tab ───────────────────────────────────────────────────
html = replace_exact(html,
    '.form-label { font-size: 11px; font-weight: 600; color: var(--text-sub); }',
    '.form-label { font-size: 12px; font-weight: 600; color: var(--text-sub); }')

html = replace_exact(html,
    '.form-input { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 9px 10px; font-size: 14px;',
    '.form-input { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 9px 10px; font-size: 16px;')

html = replace_exact(html,
    '.form-sel { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 9px 10px; font-size: 14px;',
    '.form-sel { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 9px 10px; font-size: 16px;')

html = replace_exact(html,
    '.submit-btn { width: 100%; background: linear-gradient(135deg, var(--g-from) 0%, var(--g-to) 100%); color: #fff; border: none; border-radius: 50px; padding: 13px; font-size: 14px;',
    '.submit-btn { width: 100%; background: linear-gradient(135deg, var(--g-from) 0%, var(--g-to) 100%); color: #fff; border: none; border-radius: 50px; padding: 13px; font-size: 16px;')

html = replace_exact(html,
    '.chart-label { font-size: 11px;',
    '.chart-label { font-size: 12px;')

html = replace_exact(html,
    '.data-table th { padding: 9px 8px; font-size: 11px;',
    '.data-table th { padding: 9px 8px; font-size: 13px;')

html = replace_exact(html,
    '.data-table td { padding: 9px 8px; border-bottom: 1px solid var(--border); text-align: center; font-size: 12px; }',
    '.data-table td { padding: 9px 8px; border-bottom: 1px solid var(--border); text-align: center; font-size: 14px; }')

html = replace_exact(html,
    '.del-btn { background: none; border: 1px solid #E0B0B0; color: #C04040; border-radius: 6px; padding: 3px 8px; font-size: 11px;',
    '.del-btn { background: none; border: 1px solid #E0B0B0; color: #C04040; border-radius: 6px; padding: 3px 8px; font-size: 12px;')

html = replace_exact(html,
    '.empty-msg { text-align: center; padding: 36px 16px; color: var(--text-sub); font-size: 13px; }',
    '.empty-msg { text-align: center; padding: 36px 16px; color: var(--text-sub); font-size: 15px; }')

# ── 10. Settings modal ────────────────────────────────────────────────────────
html = replace_exact(html,
    '.modal-h { font-size: 16px; font-weight: 700; margin-bottom: 16px; }',
    '.modal-h { font-size: 18px; font-weight: 700; margin-bottom: 16px; }')

html = replace_exact(html,
    '.goal-name { font-size: 14px; font-weight: 600; }',
    '.goal-name { font-size: 16px; font-weight: 600; }')

html = replace_exact(html,
    '.goal-freq { font-size: 11px; color: var(--text-sub); margin-top: 1px; }',
    '.goal-freq { font-size: 13px; color: var(--text-sub); margin-top: 1px; }')

html = replace_exact(html,
    '.goal-edit-form .field-lbl { display: block; font-size: 11px;',
    '.goal-edit-form .field-lbl { display: block; font-size: 12px;')

html = replace_exact(html,
    '.goal-save-btn { flex: 1; background: var(--accent); color: #fff; border: none; border-radius: 10px; padding: 10px; font-size: 14px;',
    '.goal-save-btn { flex: 1; background: var(--accent); color: #fff; border: none; border-radius: 10px; padding: 10px; font-size: 16px;')

html = replace_exact(html,
    '.goal-cancel-btn { background: var(--bg); color: var(--text-sub); border: 1px solid var(--border); border-radius: 10px; padding: 10px 16px; font-size: 14px;',
    '.goal-cancel-btn { background: var(--bg); color: var(--text-sub); border: 1px solid var(--border); border-radius: 10px; padding: 10px 16px; font-size: 16px;')

html = replace_exact(html,
    '.add-h { font-size: 14px; font-weight: 600; color: var(--accent); margin-bottom: 14px; }',
    '.add-h { font-size: 16px; font-weight: 600; color: var(--accent); margin-bottom: 14px; }')

html = replace_exact(html,
    '.field-lbl { font-size: 11px; font-weight: 600; color: var(--text-sub); margin-bottom: 6px; display: block; letter-spacing: 0.5px; }',
    '.field-lbl { font-size: 12px; font-weight: 600; color: var(--text-sub); margin-bottom: 6px; display: block; letter-spacing: 0.5px; }')

html = replace_exact(html,
    '.text-input { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 10px 12px; font-size: 14px;',
    '.text-input { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 10px 12px; font-size: 16px;')

html = replace_exact(html,
    '.freq-sel { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 10px 12px; font-size: 14px;',
    '.freq-sel { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 10px 12px; font-size: 16px;')

html = replace_exact(html,
    '.add-goal-btn { width: 100%; background: linear-gradient(135deg, var(--g-from) 0%, var(--g-to) 100%); color: #fff; border: none; border-radius: 50px; padding: 13px; font-size: 14px;',
    '.add-goal-btn { width: 100%; background: linear-gradient(135deg, var(--g-from) 0%, var(--g-to) 100%); color: #fff; border: none; border-radius: 50px; padding: 13px; font-size: 16px;')

# ── 11. Login screen ──────────────────────────────────────────────────────────
html = replace_exact(html,
    '.login-title { font-size: 26px; font-weight: 700; color: var(--text); }',
    '.login-title { font-size: 28px; font-weight: 700; color: var(--text); }')

html = replace_exact(html,
    '.login-sub { font-size: 13px;',
    '.login-sub { font-size: 15px;')

html = replace_exact(html,
    '.login-btn { display: flex; align-items: center; gap: 10px; background: var(--surface); border: 1px solid var(--border); border-radius: 50px; padding: 13px 28px; font-size: 15px;',
    '.login-btn { display: flex; align-items: center; gap: 10px; background: var(--surface); border: 1px solid var(--border); border-radius: 50px; padding: 13px 28px; font-size: 16px;')

html = replace_exact(html,
    '.logout-btn { width: 100%; background: none; border: 1px solid #E0B0B0; color: #C04040; border-radius: 8px; padding: 10px; font-size: 13px;',
    '.logout-btn { width: 100%; background: none; border: 1px solid #E0B0B0; color: #C04040; border-radius: 8px; padding: 10px; font-size: 15px;')

# ── write ─────────────────────────────────────────────────────────────────────
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done - all patches applied.")
