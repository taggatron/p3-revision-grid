import json
import os

with open('images_b64.json', 'r') as f:
    images_b64 = json.load(f)

# Import cards_data from generate_site.py
from generate_site import cards_data

html_template = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GCSE Physics P3 Revision Grid | Electricity & Magnetism Flashcards (OCR Gateway J250)</title>
  <meta name="description" content="Interactive 4x4 GCSE Combined Science (Gateway J250) P3 revision flashcard grid covering Electricity and Magnetism with mark schemes, calculation steps, and diagrams.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  
  <style>
    /* CSS RESET & VARIABLES */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    :root {
      /* Theme - Dark (Default) */
      --bg-primary: #0a0e17;
      --bg-secondary: #111827;
      --bg-card: rgba(17, 24, 39, 0.85);
      --bg-card-hover: rgba(24, 33, 53, 0.95);
      --bg-glass: rgba(17, 24, 39, 0.7);
      --border-color: rgba(255, 255, 255, 0.1);
      --border-color-hover: rgba(255, 255, 255, 0.2);
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
      --shadow-lg: 0 20px 40px -10px rgba(0, 0, 0, 0.7);
      --shadow-glow: 0 0 25px rgba(0, 194, 255, 0.2);

      /* Column Accents */
      --col1-color: #00d2ff;
      --col1-bg: rgba(0, 210, 255, 0.12);
      --col1-border: rgba(0, 210, 255, 0.35);

      --col2-color: #fbbf24;
      --col2-bg: rgba(251, 191, 36, 0.12);
      --col2-border: rgba(251, 191, 36, 0.35);

      --col3-color: #10b981;
      --col3-bg: rgba(16, 185, 129, 0.12);
      --col3-border: rgba(16, 185, 129, 0.35);

      --col4-color: #c084fc;
      --col4-bg: rgba(192, 132, 252, 0.12);
      --col4-border: rgba(192, 132, 252, 0.35);

      /* Status Colors */
      --status-unseen: #64748b;
      --status-learning: #f59e0b;
      --status-mastered: #10b981;

      /* Radii */
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;

      --font-main: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

        [data-theme="light"] {
      --bg-primary: #f8fafc;
      --bg-secondary: #ffffff;
      --bg-card: rgba(255, 255, 255, 0.98);
      --bg-card-hover: #ffffff;
      --bg-glass: rgba(255, 255, 255, 0.92);
      --border-color: rgba(226, 232, 240, 0.9);
      --border-color-hover: rgba(203, 213, 225, 1);
      --text-primary: #0f172a;
      --text-secondary: #334155;
      --text-muted: #64748b;
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
      --shadow-md: 0 4px 14px -1px rgba(0, 0, 0, 0.08), 0 2px 6px -1px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 12px 28px -4px rgba(0, 0, 0, 0.1), 0 4px 10px -2px rgba(0, 0, 0, 0.05);
      --shadow-glow: 0 0 25px rgba(2, 132, 199, 0.15);

      --col1-color: #0284c7;
      --col1-bg: rgba(2, 132, 199, 0.09);
      --col1-border: rgba(2, 132, 199, 0.3);

      --col2-color: #d97706;
      --col2-bg: rgba(217, 119, 6, 0.09);
      --col2-border: rgba(217, 119, 6, 0.3);

      --col3-color: #059669;
      --col3-bg: rgba(5, 150, 105, 0.09);
      --col3-border: rgba(5, 150, 105, 0.3);

      --col4-color: #7e22ce;
      --col4-bg: rgba(126, 34, 206, 0.09);
      --col4-border: rgba(126, 34, 206, 0.3);
    }

    [data-theme="light"] body {
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(2, 132, 199, 0.07) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(126, 34, 206, 0.06) 0%, transparent 40%);
    }

    [data-theme="light"] header {
      background: rgba(255, 255, 255, 0.88);
      border-color: rgba(226, 232, 240, 0.95);
      box-shadow: var(--shadow-md);
    }

    [data-theme="light"] .brand-text h1 {
      background: linear-gradient(90deg, #0f172a, #0284c7);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    [data-theme="light"] .matrix-tile {
      background: #ffffff;
      border-color: #e2e8f0;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.04);
    }

    [data-theme="light"] .matrix-tile:hover {
      border-color: #cbd5e1;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
    }

    [data-theme="light"] .card-face.card-front {
      background: #ffffff;
      border-color: #e2e8f0;
    }

    [data-theme="light"] .card-face.card-back {
      background: #ffffff;
      border-color: rgba(2, 132, 199, 0.35);
      box-shadow: 0 15px 35px rgba(2, 132, 199, 0.12), 0 5px 15px rgba(0, 0, 0, 0.05);
    }

    [data-theme="light"] .mark-scheme-box {
      background: #f0fdf4;
      border-left-color: #059669;
      border-top: 1px solid #dcfce7;
      border-right: 1px solid #dcfce7;
      border-bottom: 1px solid #dcfce7;
    }

    [data-theme="light"] .calc-breakdown-box {
      background: #fffbeb;
      border: 1px solid #fde68a;
    }

    [data-theme="light"] .calc-working-code {
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fcd34d;
    }

    [data-theme="light"] .examiner-tip-box {
      background: #faf5ff;
      border-left-color: #7e22ce;
      border-top: 1px solid #f3e8ff;
      border-right: 1px solid #f3e8ff;
      border-bottom: 1px solid #f3e8ff;
      color: #3b0764;
    }

    [data-theme="light"] .diagram-card-container {
      background: #f8fafc;
      border-color: #e2e8f0;
    }

    [data-theme="light"] .diagram-img-wrapper {
      border-color: #cbd5e1;
      background: #ffffff;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    [data-theme="light"] .diagram-zoom-overlay {
      background: rgba(15, 23, 42, 0.8);
      color: #ffffff;
    }

    [data-theme="light"] .rate-btn-review {
      background: #fffbeb;
      color: #b45309;
      border: 1px solid #fcd34d;
    }

    [data-theme="light"] .rate-btn-review:hover {
      background: #fef3c7;
      border-color: #f59e0b;
    }

    [data-theme="light"] .jump-dot {
      background: #cbd5e1;
    }

    [data-theme="light"] .jump-dot.active {
      background: #0284c7;
      box-shadow: 0 0 8px rgba(2, 132, 199, 0.5);
    }

    [data-theme="light"] .jump-dot.is-mastered {
      background: #059669;
    }

    [data-theme="light"] .jump-dot.is-learning {
      background: #d97706;
    }

    [data-theme="light"] .formula-table th {
      background: #f1f5f9;
      color: #0284c7;
    }

    [data-theme="light"] .formula-table code {
      background: #fef3c7;
      color: #92400e;
    }

    body {
      font-family: var(--font-main);
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.5;
      min-height: 100vh;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(0, 210, 255, 0.05) 0%, transparent 35%),
        radial-gradient(circle at 85% 85%, rgba(192, 132, 252, 0.05) 0%, transparent 35%);
    }

    /* CONTAINER */
    .app-container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 1.5rem 1.25rem 4rem;
    }

    /* HEADER */
    header {
      background: var(--bg-glass);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.5rem 2rem;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-md);
      position: sticky;
      top: 1rem;
      z-index: 50;
    }

    .header-top {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1.25rem;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .brand-icon {
      width: 48px;
      height: 48px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, #00d2ff, #7e22ce);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3);
      flex-shrink: 0;
    }

    .brand-text h1 {
      font-size: 1.45rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.2;
      background: linear-gradient(90deg, var(--text-primary), var(--col1-color));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-text p {
      font-size: 0.875rem;
      color: var(--text-secondary);
      font-weight: 500;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      padding: 0.55rem 0.95rem;
      border-radius: var(--radius-md);
      font-family: var(--font-main);
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid var(--border-color);
      background: var(--bg-secondary);
      color: var(--text-primary);
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      user-select: none;
      text-decoration: none;
    }

    .btn:hover {
      background: var(--bg-card-hover);
      border-color: var(--border-color-hover);
      transform: translateY(-1px);
      box-shadow: var(--shadow-sm);
    }

    .btn:active {
      transform: translateY(0);
    }

    .btn-primary {
      background: linear-gradient(135deg, #0284c7, #00d2ff);
      color: #ffffff;
      border: none;
      box-shadow: 0 4px 12px rgba(0, 210, 255, 0.25);
    }

    .btn-primary:hover {
      background: linear-gradient(135deg, #0369a1, #00b4d8);
      box-shadow: 0 6px 16px rgba(0, 210, 255, 0.4);
    }

    .btn-accent {
      background: linear-gradient(135deg, #7c3aed, #a855f7);
      color: #ffffff;
      border: none;
    }

    .btn-accent:hover {
      background: linear-gradient(135deg, #6d28d9, #9333ea);
    }

    .btn-icon-only {
      width: 38px;
      height: 38px;
      padding: 0;
      border-radius: var(--radius-md);
      font-size: 1.1rem;
    }

    /* PROGRESS & STATS BAR */
    .progress-section {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      background: rgba(0, 0, 0, 0.15);
      border-radius: var(--radius-md);
      padding: 0.85rem 1.15rem;
      border: 1px solid var(--border-color);
    }

    [data-theme="light"] .progress-section {
      background: rgba(0, 0, 0, 0.03);
    }

    .progress-info {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.5rem;
      font-size: 0.85rem;
    }

    .stats-pills {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .stat-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.2rem 0.65rem;
      border-radius: var(--radius-full);
      font-size: 0.775rem;
      font-weight: 600;
    }

    .stat-badge.mastered {
      background: rgba(16, 185, 129, 0.15);
      color: #10b981;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .stat-badge.learning {
      background: rgba(245, 158, 11, 0.15);
      color: #f59e0b;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .stat-badge.unseen {
      background: rgba(100, 116, 139, 0.15);
      color: #94a3b8;
      border: 1px solid rgba(100, 116, 139, 0.3);
    }

    .progress-bar-container {
      width: 100%;
      height: 8px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-full);
      overflow: hidden;
      position: relative;
    }

    [data-theme="light"] .progress-bar-container {
      background: rgba(0, 0, 0, 0.08);
    }

    .progress-bar-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #00d2ff, #10b981);
      border-radius: var(--radius-full);
      transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 0 8px rgba(16, 185, 129, 0.5);
    }

    /* CONTROLS TOOLBAR */
    .controls-toolbar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 2rem;
      padding: 0.5rem 0.25rem;
    }

    .view-switch {
      display: flex;
      background: var(--bg-secondary);
      padding: 4px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
    }

    .view-switch-btn {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      background: transparent;
      border: none;
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .view-switch-btn.active {
      background: var(--bg-primary);
      color: var(--text-primary);
      box-shadow: var(--shadow-sm);
    }

    .filter-group {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .filter-chip {
      padding: 0.35rem 0.8rem;
      border-radius: var(--radius-full);
      font-size: 0.8rem;
      font-weight: 600;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .filter-chip:hover {
      border-color: var(--border-color-hover);
      color: var(--text-primary);
    }

    .filter-chip.active {
      background: var(--text-primary);
      color: var(--bg-primary);
      border-color: var(--text-primary);
    }

    /* GRID VIEW (4x4 REVISION GRID) */
    .grid-view {
      display: block;
    }

    .grid-view.hidden {
      display: none;
    }

    .grid-columns-header {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
      margin-bottom: 1.25rem;
    }

    .col-header-card {
      padding: 1rem 1.15rem;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.95rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      box-shadow: var(--shadow-sm);
      border-width: 1px;
      border-style: solid;
    }

    .col-header-card.col-charge {
      background: var(--col1-bg);
      border-color: var(--col1-border);
      color: var(--col1-color);
    }

    .col-header-card.col-energy {
      background: var(--col2-bg);
      border-color: var(--col2-border);
      color: var(--col2-color);
    }

    .col-header-card.col-circuits {
      background: var(--col3-bg);
      border-color: var(--col3-border);
      color: var(--col3-color);
    }

    .col-header-card.col-magnetism {
      background: var(--col4-bg);
      border-color: var(--col4-border);
      color: var(--col4-color);
    }

    .revision-matrix {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
    }

    /* GRID CARD TILE */
    .matrix-tile {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 230px;
      cursor: pointer;
      position: relative;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      overflow: hidden;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }

    .matrix-tile:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: var(--border-color-hover);
    }

    .matrix-tile::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
    }

    .matrix-tile.col-charge::before { background: var(--col1-color); }
    .matrix-tile.col-energy::before { background: var(--col2-color); }
    .matrix-tile.col-circuits::before { background: var(--col3-color); }
    .matrix-tile.col-magnetism::before { background: var(--col4-color); }

    .tile-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      margin-bottom: 0.85rem;
    }

    .tile-qtag {
      font-weight: 800;
      font-size: 0.85rem;
      padding: 0.2rem 0.55rem;
      border-radius: var(--radius-sm);
      letter-spacing: 0.05em;
    }

    .col-charge .tile-qtag { background: var(--col1-bg); color: var(--col1-color); }
    .col-energy .tile-qtag { background: var(--col2-bg); color: var(--col2-color); }
    .col-circuits .tile-qtag { background: var(--col3-bg); color: var(--col3-color); }
    .col-magnetism .tile-qtag { background: var(--col4-bg); color: var(--col4-color); }

    .tile-badges {
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .badge-diagram {
      background: rgba(0, 210, 255, 0.15);
      color: var(--col1-color);
      border-radius: var(--radius-full);
      padding: 0.15rem 0.45rem;
      font-size: 0.7rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.25rem;
    }

    .badge-calc {
      background: rgba(251, 191, 36, 0.15);
      color: var(--col2-color);
      border-radius: var(--radius-full);
      padding: 0.15rem 0.45rem;
      font-size: 0.7rem;
      font-weight: 700;
    }

    .tile-body {
      flex: 1;
      margin-bottom: 1rem;
    }

    .tile-question {
      font-size: 0.925rem;
      font-weight: 500;
      color: var(--text-primary);
      line-height: 1.45;
      display: -webkit-box;
      -webkit-line-clamp: 4;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .tile-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 0.75rem;
      border-top: 1px solid var(--border-color);
      font-size: 0.775rem;
    }

    .status-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      font-weight: 600;
      padding: 0.15rem 0.5rem;
      border-radius: var(--radius-full);
      font-size: 0.75rem;
    }

    .status-pill.unseen {
      color: var(--text-muted);
      background: rgba(100, 116, 139, 0.1);
    }

    .status-pill.learning {
      color: #f59e0b;
      background: rgba(245, 158, 11, 0.1);
    }

    .status-pill.mastered {
      color: #10b981;
      background: rgba(16, 185, 129, 0.12);
    }

    .tile-action-hint {
      color: var(--text-secondary);
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 0.2rem;
    }

    .matrix-tile:hover .tile-action-hint {
      color: var(--col1-color);
    }

    /* FOCUS / CAROUSEL FLASHCARD VIEW */
    .focus-view {
      display: none;
      max-width: 900px;
      margin: 0 auto;
    }

    .focus-view.active {
      display: block;
    }

    .focus-card-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.25rem;
      font-size: 0.9rem;
      color: var(--text-secondary);
    }

    .deck-counter {
      font-weight: 700;
      font-family: var(--font-mono);
      background: var(--bg-secondary);
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-full);
      border: 1px solid var(--border-color);
    }

    /* 3D FLASHCARD CONTAINER */
    .flashcard-3d-wrapper {
      perspective: 1400px;
      width: 100%;
      min-height: 540px;
      margin-bottom: 1.5rem;
    }

    .flashcard-inner {
      position: relative;
      width: 100%;
      min-height: 540px;
      transform-style: preserve-3d;
      transition: transform 0.65s cubic-bezier(0.4, 0, 0.2, 1);
      border-radius: var(--radius-lg);
    }

    .flashcard-inner.flipped {
      transform: rotateY(180deg);
    }

    .card-face {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      border-radius: var(--radius-lg);
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-lg);
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      overflow-y: auto;
    }

    .card-face.card-front {
      z-index: 2;
      transform: rotateY(0deg);
    }

    .card-face.card-back {
      transform: rotateY(180deg);
      background: var(--bg-card);
      border-color: rgba(0, 210, 255, 0.25);
    }

    /* Custom Scrollbar for Card Back */
    .card-face::-webkit-scrollbar {
      width: 6px;
    }
    .card-face::-webkit-scrollbar-track {
      background: rgba(0, 0, 0, 0.1);
      border-radius: 4px;
    }
    .card-face::-webkit-scrollbar-thumb {
      background: var(--border-color);
      border-radius: 4px;
    }
    .card-face::-webkit-scrollbar-thumb:hover {
      background: var(--text-muted);
    }

    /* FRONT FACE CONTENT */
    .card-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }

    .topic-indicator {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-full);
      font-size: 0.85rem;
      font-weight: 700;
    }

    .card-marks-badge {
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.3rem 0.75rem;
      border-radius: var(--radius-full);
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
    }

    .front-question-box {
      margin: auto 0;
      padding: 1.5rem 0;
      text-align: center;
    }

    .front-question-number {
      font-size: 1.15rem;
      font-weight: 800;
      font-family: var(--font-mono);
      letter-spacing: 0.05em;
      margin-bottom: 0.75rem;
      opacity: 0.8;
    }

    .front-question-text {
      font-size: 1.45rem;
      font-weight: 600;
      line-height: 1.5;
      color: var(--text-primary);
      max-width: 760px;
      margin: 0 auto 1.5rem;
    }

    .hint-container {
      margin-top: 1rem;
    }

    .hint-text {
      display: none;
      background: rgba(251, 191, 36, 0.1);
      border: 1px dashed rgba(251, 191, 36, 0.4);
      color: #fbbf24;
      padding: 0.75rem 1.25rem;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      max-width: 650px;
      margin: 0.75rem auto 0;
      text-align: left;
    }

    .hint-text.active {
      display: block;
      animation: fadeIn 0.3s ease;
    }

    .front-footer-prompt {
      text-align: center;
      margin-top: 1.5rem;
    }

    .flip-btn-prompt {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.85rem 1.75rem;
      border-radius: var(--radius-full);
      font-size: 1rem;
      font-weight: 700;
      background: linear-gradient(135deg, var(--col1-color), #3b82f6);
      color: #ffffff;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 20px rgba(0, 210, 255, 0.35);
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .flip-btn-prompt:hover {
      transform: scale(1.03);
      box-shadow: 0 6px 25px rgba(0, 210, 255, 0.5);
    }

    .key-tip {
      font-size: 0.775rem;
      color: var(--text-muted);
      margin-top: 0.5rem;
    }

    /* BACK FACE CONTENT */
    .back-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 1rem;
      margin-bottom: 1.25rem;
    }

    .back-title {
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .back-title h3 {
      font-size: 1.15rem;
      font-weight: 800;
      color: #10b981;
    }

    .flip-back-btn {
      padding: 0.35rem 0.75rem;
      font-size: 0.8rem;
    }

    .mark-scheme-box {
      background: rgba(16, 185, 129, 0.06);
      border-left: 4px solid #10b981;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      padding: 1.15rem 1.35rem;
      margin-bottom: 1.25rem;
    }

    .mark-scheme-box h4 {
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #10b981;
      margin-bottom: 0.6rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .mark-scheme-points {
      list-style-type: none;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .mark-scheme-points li {
      position: relative;
      padding-left: 1.4rem;
      font-size: 0.95rem;
      line-height: 1.5;
    }

    .mark-scheme-points li::before {
      content: '✓';
      position: absolute;
      left: 0;
      color: #10b981;
      font-weight: 800;
    }

    /* CALCULATION WORKING BOX */
    .calc-breakdown-box {
      background: rgba(251, 191, 36, 0.07);
      border: 1px solid rgba(251, 191, 36, 0.3);
      border-radius: var(--radius-md);
      padding: 1.15rem 1.35rem;
      margin-bottom: 1.25rem;
    }

    .calc-header {
      font-size: 0.85rem;
      font-weight: 700;
      color: #fbbf24;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .calc-row {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      margin-bottom: 0.5rem;
      font-size: 0.9rem;
    }

    .calc-row strong {
      color: var(--text-secondary);
      font-size: 0.8rem;
    }

    .calc-working-code {
      font-family: var(--font-mono);
      background: rgba(0, 0, 0, 0.25);
      padding: 0.5rem 0.75rem;
      border-radius: var(--radius-sm);
      white-space: pre-line;
      line-height: 1.45;
      color: #fef08a;
    }

    /* DIAGRAM CONTAINER ON CARD BACK */
    .diagram-card-container {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1rem;
      margin-bottom: 1.25rem;
      text-align: center;
      box-shadow: var(--shadow-sm);
    }

    .diagram-header-tag {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.75rem;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--col1-color);
    }

    .diagram-img-wrapper {
      position: relative;
      cursor: zoom-in;
      overflow: hidden;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      background: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
      max-height: 320px;
    }

    .diagram-img-wrapper img {
      max-width: 100%;
      max-height: 320px;
      object-fit: contain;
      display: block;
      transition: transform 0.3s ease;
    }

    .diagram-img-wrapper:hover img {
      transform: scale(1.02);
    }

    .diagram-zoom-overlay {
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(0, 0, 0, 0.75);
      color: #ffffff;
      padding: 0.25rem 0.6rem;
      border-radius: var(--radius-full);
      font-size: 0.75rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 0.3rem;
      backdrop-filter: blur(4px);
    }

    .diagram-caption {
      font-size: 0.825rem;
      color: var(--text-secondary);
      margin-top: 0.65rem;
      line-height: 1.4;
      text-align: left;
    }

    /* EXAMINER TIP BOX */
    .examiner-tip-box {
      background: rgba(192, 132, 252, 0.08);
      border-left: 4px solid var(--col4-color);
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      padding: 0.85rem 1.15rem;
      margin-bottom: 1.25rem;
      font-size: 0.875rem;
      line-height: 1.45;
    }

    .examiner-tip-box strong {
      color: var(--col4-color);
      display: block;
      margin-bottom: 0.25rem;
    }

    /* SELF EVALUATION BUTTONS */
    .rating-actions-bar {
      display: flex;
      gap: 0.85rem;
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 1px solid var(--border-color);
    }

    .rate-btn {
      flex: 1;
      padding: 0.85rem;
      border-radius: var(--radius-md);
      font-family: var(--font-main);
      font-size: 0.95rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      cursor: pointer;
      border: none;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .rate-btn-review {
      background: rgba(245, 158, 11, 0.15);
      color: #f59e0b;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .rate-btn-review:hover {
      background: rgba(245, 158, 11, 0.25);
      border-color: rgba(245, 158, 11, 0.6);
      transform: translateY(-2px);
    }

    .rate-btn-master {
      background: linear-gradient(135deg, #059669, #10b981);
      color: #ffffff;
      box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }

    .rate-btn-master:hover {
      background: linear-gradient(135deg, #047857, #059669);
      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
      transform: translateY(-2px);
    }

    /* CAROUSEL BOTTOM NAVIGATION */
    .deck-nav-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-top: 1rem;
    }

    .deck-jump-list {
      display: flex;
      gap: 0.35rem;
      flex-wrap: wrap;
      justify-content: center;
      max-width: 500px;
    }

    .jump-dot {
      width: 12px;
      height: 12px;
      border-radius: var(--radius-full);
      background: var(--border-color);
      cursor: pointer;
      transition: all 0.2s ease;
      border: none;
    }

    .jump-dot:hover {
      background: var(--text-secondary);
      transform: scale(1.2);
    }

    .jump-dot.active {
      background: var(--col1-color);
      transform: scale(1.25);
      box-shadow: 0 0 8px var(--col1-color);
    }

    .jump-dot.is-mastered {
      background: #10b981;
    }

    .jump-dot.is-learning {
      background: #f59e0b;
    }

    /* MODALS */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      animation: fadeIn 0.2s ease;
    }

    .modal-backdrop.open {
      display: flex;
    }

    .modal-dialog {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 850px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: var(--shadow-lg);
      padding: 2rem;
      position: relative;
      animation: zoomIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .modal-close-btn {
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: transparent;
      border: none;
      color: var(--text-secondary);
      font-size: 1.5rem;
      cursor: pointer;
      width: 36px;
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: var(--radius-sm);
      transition: all 0.2s ease;
    }

    .modal-close-btn:hover {
      background: var(--border-color);
      color: var(--text-primary);
    }

    /* FORMULA SHEET TABLE */
    .formula-table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.25rem 0;
      font-size: 0.9rem;
    }

    .formula-table th, .formula-table td {
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border-color);
      text-align: left;
    }

    .formula-table th {
      background: rgba(0, 0, 0, 0.2);
      color: var(--col1-color);
      font-weight: 700;
    }

    .formula-table code {
      font-family: var(--font-mono);
      font-weight: 700;
      color: #fbbf24;
      background: rgba(0, 0, 0, 0.2);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }

    /* LIGHTBOX MODAL SPECIFIC */
    .lightbox-dialog {
      max-width: 1050px;
      padding: 1.5rem;
      text-align: center;
    }

    .lightbox-img-box {
      background: #ffffff;
      border-radius: var(--radius-md);
      padding: 1rem;
      margin: 1rem 0;
      max-height: 70vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }

    .lightbox-img-box img {
      max-width: 100%;
      max-height: 65vh;
      object-fit: contain;
      border-radius: var(--radius-sm);
    }

    .lightbox-caption {
      font-size: 0.95rem;
      color: var(--text-secondary);
      line-height: 1.5;
    }

    /* CELEBRATION TOAST / OVERLAY */
    .celebration-toast {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: linear-gradient(135deg, #059669, #10b981);
      color: #ffffff;
      padding: 1rem 1.5rem;
      border-radius: var(--radius-md);
      box-shadow: 0 10px 30px rgba(16, 185, 129, 0.4);
      display: none;
      align-items: center;
      gap: 0.75rem;
      font-weight: 700;
      z-index: 999;
      animation: slideUp 0.3s ease;
    }

    .celebration-toast.show {
      display: flex;
    }

    /* ANIMATIONS */
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    @keyframes zoomIn {
      from { opacity: 0; transform: scale(0.95); }
      to { opacity: 1; transform: scale(1); }
    }

    @keyframes slideUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 1024px) {
      .grid-columns-header {
        grid-template-columns: repeat(2, 1fr);
      }
      .revision-matrix {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 640px) {
      .app-container {
        padding: 1rem 0.75rem 3rem;
      }
      header {
        padding: 1.15rem;
        margin-bottom: 1.25rem;
        position: relative;
        top: 0;
      }
      .brand-text h1 {
        font-size: 1.2rem;
      }
      .grid-columns-header {
        display: none; /* Hide header row on phone, each card has its own topic indicator */
      }
      .revision-matrix {
        grid-template-columns: 1fr;
        gap: 1rem;
      }
      .flashcard-3d-wrapper, .flashcard-inner {
        min-height: 580px;
      }
      .card-face {
        padding: 1.25rem;
      }
      .front-question-text {
        font-size: 1.15rem;
      }
    }

    /* PRINT STYLES FOR REVISION HANDOUT */
    @media print {
      body {
        background: #ffffff !important;
        color: #000000 !important;
      }
      header, .controls-toolbar, .rating-actions-bar, .deck-nav-bar, .modal-backdrop, .btn, .flip-btn-prompt {
        display: none !important;
      }
      .app-container {
        max-width: 100% !important;
        padding: 0 !important;
      }
      .grid-view {
        display: block !important;
      }
      .grid-columns-header {
        grid-template-columns: repeat(4, 1fr) !important;
      }
      .revision-matrix {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 15px !important;
      }
      .matrix-tile {
        page-break-inside: avoid;
        border: 1px solid #333 !important;
        background: #fff !important;
        min-height: auto !important;
      }
    }
  </style>
</head>
<body>

  <div class="app-container">
    <!-- APP HEADER -->
    <header>
      <div class="header-top">
        <div class="brand-group">
          <div class="brand-icon">⚡</div>
          <div class="brand-text">
            <h1>GCSE Physics (Gateway J250) – P3 Revision Grid</h1>
            <p>Electricity &amp; Magnetism Interactive $4 \times 4$ Revision Flashcards &amp; Diagrams</p>
          </div>
        </div>

        <div class="header-actions">
          <button class="btn btn-primary" id="btnFormulaSheet" title="View P3 Physics Equations">
            📐 Formulas
          </button>
          <button class="btn" id="btnShuffle" title="Shuffle flashcard sequence">
            🔀 Shuffle
          </button>
          <button class="btn" id="btnResetProgress" title="Reset your mastery progress">
            ↺ Reset
          </button>
          <button class="btn btn-icon-only" id="btnToggleSound" title="Toggle audio feedback">
            🔊
          </button>
          <button class="btn btn-icon-only" id="btnToggleTheme" title="Toggle Dark/Light Mode">
            🌓
          </button>
          <button class="btn btn-icon-only" id="btnHelp" title="Keyboard shortcuts and guide">
            ❓
          </button>
        </div>
      </div>

      <!-- PROGRESS & STATS -->
      <div class="progress-section">
        <div class="progress-info">
          <span style="font-weight: 700;">Revision Mastery: <strong id="progressPercentText" style="color: var(--col1-color);">0%</strong> (<span id="progressRatioText">0/16</span> Mastered)</span>
          <div class="stats-pills">
            <span class="stat-badge mastered" id="statMasteredCount">✓ 0 Mastered</span>
            <span class="stat-badge learning" id="statLearningCount">🔁 0 In Progress</span>
            <span class="stat-badge unseen" id="statUnseenCount">○ 16 Unattempted</span>
          </div>
        </div>
        <div class="progress-bar-container">
          <div class="progress-bar-fill" id="progressBarFill"></div>
        </div>
      </div>
    </header>

    <!-- CONTROLS & FILTERS -->
    <div class="controls-toolbar">
      <!-- VIEW SWITCHER -->
      <div class="view-switch">
        <button class="view-switch-btn active" id="btnViewGrid">
          <span>⊞</span> 4×4 Grid View
        </button>
        <button class="view-switch-btn" id="btnViewFocus">
          <span>🂡</span> Focus Flashcards
        </button>
      </div>

      <!-- TOPIC FILTER -->
      <div class="filter-group">
        <button class="filter-chip active" data-filter="all">All Topics (16)</button>
        <button class="filter-chip" data-filter="charge" style="border-left: 3px solid var(--col1-color);">⚡ Charge &amp; Time</button>
        <button class="filter-chip" data-filter="energy" style="border-left: 3px solid var(--col2-color);">💡 Energy &amp; Power</button>
        <button class="filter-chip" data-filter="circuits" style="border-left: 3px solid var(--col3-color);">🔌 Circuits &amp; Res.</button>
        <button class="filter-chip" data-filter="magnetism" style="border-left: 3px solid var(--col4-color);">🧲 Magnetism</button>
      </div>
    </div>

    <!-- MAIN VIEW 1: 4x4 REVISION GRID -->
    <main class="grid-view" id="gridView">
      <!-- 4 COLUMN HEADERS -->
      <div class="grid-columns-header">
        <div class="col-header-card col-charge">
          <span>⚡</span> 1. Charge, Current &amp; Time
        </div>
        <div class="col-header-card col-energy">
          <span>💡</span> 2. Energy &amp; Power
        </div>
        <div class="col-header-card col-circuits">
          <span>🔌</span> 3. Circuits &amp; Resistance
        </div>
        <div class="col-header-card col-magnetism">
          <span>🧲</span> 4. Magnetism &amp; Electromagnetism
        </div>
      </div>

      <!-- 4x4 MATRIX OF TILES -->
      <div class="revision-matrix" id="revisionMatrix">
        <!-- Rendered dynamically by JS -->
      </div>
    </main>

    <!-- MAIN VIEW 2: FOCUS CAROUSEL FLASHCARD DECK -->
    <section class="focus-view" id="focusView">
      <div class="focus-card-meta">
        <div>
          <button class="btn btn-sm" id="btnBackToGrid">← Return to 4×4 Grid</button>
        </div>
        <div class="deck-counter" id="deckCounter">Card 1 of 16</div>
        <div>
          <span id="focusCardStatusBadge" class="status-pill unseen">○ Unattempted</span>
        </div>
      </div>

      <!-- 3D FLIP CARD CONTAINER -->
      <div class="flashcard-3d-wrapper">
        <div class="flashcard-inner" id="flashcardInner">
          
          <!-- FRONT FACE (QUESTION) -->
          <div class="card-face card-front" id="cardFrontFace">
            <div class="card-top-bar">
              <span class="topic-indicator" id="frontTopicIndicator">⚡ Charge, Current &amp; Time</span>
              <span class="card-marks-badge" id="frontMarksBadge">[2 Marks]</span>
            </div>

            <div class="front-question-box">
              <div class="front-question-number" id="frontQuestionNum">QUESTION 1</div>
              <h2 class="front-question-text" id="frontQuestionText">Loading question...</h2>
              
              <div class="hint-container">
                <button class="btn" id="btnToggleHint" style="font-size: 0.8rem; padding: 0.35rem 0.8rem;">
                  💡 Show Formula / Hint
                </button>
                <div class="hint-text" id="hintTextBox">Hint text goes here</div>
              </div>
            </div>

            <div class="front-footer-prompt">
              <button class="flip-btn-prompt" id="btnFlipCardFront">
                <span>Reveal Answer &amp; Mark Scheme</span>
                <span>↻</span>
              </button>
              <div class="key-tip">Press <kbd style="background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px;">Space</kbd> or click to flip</div>
            </div>
          </div>

          <!-- BACK FACE (ANSWER & MARK SCHEME) -->
          <div class="card-face card-back" id="cardBackFace">
            <div class="back-header">
              <div class="back-title">
                <span>✅</span>
                <h3 id="backCardTitle">A1: Official Mark Scheme</h3>
              </div>
              <button class="btn flip-back-btn" id="btnFlipCardBack">
                ↻ Flip Back
              </button>
            </div>

            <!-- MARK SCHEME BOX -->
            <div class="mark-scheme-box">
              <h4><span>🎯</span> Mark Allocation &amp; Key Points</h4>
              <ul class="mark-scheme-points" id="markSchemeList">
                <!-- Dynamically populated -->
              </ul>
            </div>

            <!-- CALCULATION BOX (if applicable) -->
            <div class="calc-breakdown-box" id="calcBreakdownBox" style="display: none;">
              <div class="calc-header">
                <span>🔢</span> Step-by-Step Calculation Breakdown
              </div>
              <div class="calc-row">
                <strong>Formula:</strong>
                <code id="calcFormula">E = Q × V</code>
              </div>
              <div class="calc-row">
                <strong>Given Values:</strong>
                <span id="calcGiven">V = 4 V, Q = 150 C</span>
              </div>
              <div class="calc-row">
                <strong>Working:</strong>
                <div class="calc-working-code" id="calcWorking">150 C × 4 V = 600 J</div>
              </div>
              <div class="calc-row">
                <strong>Final Answer:</strong>
                <span id="calcResult" style="font-weight: 800; color: #10b981; font-size: 1.05rem;">600 J</span>
              </div>
            </div>

            <!-- HIGH RES GEMINI DIAGRAM (if applicable) -->
            <div class="diagram-card-container" id="diagramContainer" style="display: none;">
              <div class="diagram-header-tag">
                <span>🖼️ EXPLANATION DIAGRAM (GCSE SPECIFICATION)</span>
                <span style="font-size: 0.75rem; color: var(--text-muted);">Click image to expand 🔍</span>
              </div>
              <div class="diagram-img-wrapper" id="diagramWrapper">
                <img id="diagramImage" src="" alt="Explanation Diagram">
                <div class="diagram-zoom-overlay">🔍 Click to Enlarge</div>
              </div>
              <p class="diagram-caption" id="diagramCaptionText">Diagram caption</p>
            </div>

            <!-- EXAMINER TIP BOX -->
            <div class="examiner-tip-box" id="examinerTipBox">
              <strong>⚠️ Examiner Advice &amp; Common Pitfalls:</strong>
              <span id="examinerTipText">Tip goes here</span>
            </div>

            <!-- SELF RATING BUTTONS -->
            <div class="rating-actions-bar">
              <button class="rate-btn rate-btn-review" id="btnRateLearning">
                <span>🔁</span> Still Need Practice (Press 1)
              </button>
              <button class="rate-btn rate-btn-master" id="btnRateMastered">
                <span>🎉</span> Mastered! (Press 2)
              </button>
            </div>
          </div>

        </div>
      </div>

      <!-- CAROUSEL NAVIGATION -->
      <div class="deck-nav-bar">
        <button class="btn" id="btnPrevCard">
          <span>←</span> Previous
        </button>

        <div class="deck-jump-list" id="jumpDotsList">
          <!-- 16 jump dots -->
        </div>

        <button class="btn btn-primary" id="btnNextCard">
          Next <span>→</span>
        </button>
      </div>
    </section>

  </div>

  <!-- MODAL 1: FORMULA SHEET -->
  <div class="modal-backdrop" id="formulaModal">
    <div class="modal-dialog">
      <button class="modal-close-btn" id="btnCloseFormulaModal">&times;</button>
      <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.5rem;">
        <span style="font-size: 1.6rem;">📐</span>
        <h2>GCSE Gateway Physics P3 Formula Sheet</h2>
      </div>
      <p style="color: var(--text-secondary); margin-bottom: 1.25rem;">
        Key equations, SI units, and relationships assessed in Electricity &amp; Magnetism.
      </p>

      <table class="formula-table">
        <thead>
          <tr>
            <th>Equation</th>
            <th>Word Formula</th>
            <th>Standard SI Units</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>Q = I × t</code></td>
            <td>Charge = Current × Time</td>
            <td>Charge in Coulombs (C), Current in Amperes (A), Time in seconds (s)</td>
          </tr>
          <tr>
            <td><code>E = Q × V</code></td>
            <td>Energy = Charge × Potential Difference</td>
            <td>Energy in Joules (J), Charge in Coulombs (C), Voltage in Volts (V)</td>
          </tr>
          <tr>
            <td><code>V = I × R</code></td>
            <td>Potential Difference = Current × Resistance</td>
            <td>Voltage in Volts (V), Current in Amperes (A), Resistance in Ohms (Ω)</td>
          </tr>
          <tr>
            <td><code>P = V × I</code></td>
            <td>Power = Potential Difference × Current</td>
            <td>Power in Watts (W), Voltage in Volts (V), Current in Amperes (A)</td>
          </tr>
          <tr>
            <td><code>P = I² × R</code></td>
            <td>Power = Current² × Resistance</td>
            <td>Power in Watts (W), Current in Amperes (A), Resistance in Ohms (Ω)</td>
          </tr>
          <tr>
            <td><code>E = P × t</code></td>
            <td>Energy = Power × Time</td>
            <td>Joules (J) = Watts (W) × seconds (s)<br>OR <strong>kWh = kW × hours</strong></td>
          </tr>
          <tr>
            <td><code>F = B × I × l</code></td>
            <td>Force = Flux Density × Current × Length</td>
            <td>Force in Newtons (N), B in Tesla (T), Current in Amps (A), Length in metres (m)</td>
          </tr>
        </tbody>
      </table>

      <div style="background: rgba(0, 210, 255, 0.08); border: 1px solid var(--col1-border); border-radius: var(--radius-md); padding: 1rem; margin-top: 1rem;">
        <h4 style="color: var(--col1-color); margin-bottom: 0.35rem;">⚡ Essential Unit Conversions &amp; Multipliers</h4>
        <ul style="padding-left: 1.25rem; font-size: 0.875rem; color: var(--text-secondary); display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.4rem;">
          <li><code>1 mA = 0.001 A</code> (÷ 1000)</li>
          <li><code>1 kW = 1000 W</code> (× 1000)</li>
          <li><code>1 hour = 3600 seconds</code></li>
          <li><code>1 kWh = 3,600,000 J</code> (3.6 MJ)</li>
          <li><code>1 kΩ = 1000 Ω</code></li>
          <li><code>1 µA = 0.000001 A</code> (10⁻⁶ A)</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODAL 2: LIGHTBOX DIAGRAM ZOOM -->
  <div class="modal-backdrop" id="lightboxModal">
    <div class="modal-dialog lightbox-dialog">
      <button class="modal-close-btn" id="btnCloseLightbox">&times;</button>
      <h3 id="lightboxTitle" style="color: var(--col1-color); margin-bottom: 0.5rem;">Diagram View</h3>
      <div class="lightbox-img-box">
        <img id="lightboxImage" src="" alt="Enlarged Diagram">
      </div>
      <p class="lightbox-caption" id="lightboxCaption">Diagram description</p>
    </div>
  </div>

  <!-- MODAL 3: KEYBOARD SHORTCUTS & HELP -->
  <div class="modal-backdrop" id="helpModal">
    <div class="modal-dialog" style="max-width: 600px;">
      <button class="modal-close-btn" id="btnCloseHelpModal">&times;</button>
      <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.75rem;">
        <span style="font-size: 1.5rem;">⌨️</span>
        <h2>Keyboard Shortcuts &amp; Revision Guide</h2>
      </div>
      <p style="color: var(--text-secondary); margin-bottom: 1.25rem; font-size: 0.9rem;">
        Power-user controls to study efficiently without touching your mouse:
      </p>

      <table class="formula-table" style="margin-bottom: 1.25rem;">
        <tbody>
          <tr>
            <td><kbd style="background: rgba(255,255,255,0.1); padding: 3px 8px; border-radius: 4px; font-family: monospace;">Space</kbd> or <kbd style="background: rgba(255,255,255,0.1); padding: 3px 8px; border-radius: 4px; font-family: monospace;">Enter</kbd></td>
            <td>Flip flashcard between Question and Mark Scheme</td>
          </tr>
          <tr>
            <td><kbd style="background: rgba(255,255,255,0.1); padding: 3px 8px; border-radius: 4px; font-family: monospace;">←</kbd> / <kbd style="background: rgba(255,255,255,0.1); padding: 3px 8px; border-radius: 4px; font-family: monospace;">→</kbd></td>
            <td>Navigate to Previous / Next flashcard</td>
          </tr>
          <tr>
            <td><kbd style="background: rgba(255,255,255,0.1); padding: 3px 8px; border-radius: 4px; font-family: monospace;">1</kbd></td>
            <td>Mark current card as "Still Need Practice" 🔁</td>
          </tr>
          <tr>
            <td><kbd style="background: rgba(255,255,255,0.1); padding: 3px 8px; border-radius: 4px; font-family: monospace;">2</kbd></td>
            <td>Mark current card as "Mastered!" 🎉</td>
          </tr>
          <tr>
            <td><kbd style="background: rgba(255,255,255,0.1); padding: 3px 8px; border-radius: 4px; font-family: monospace;">G</kbd></td>
            <td>Switch to 4×4 Grid View</td>
          </tr>
          <tr>
            <td><kbd style="background: rgba(255,255,255,0.1); padding: 3px 8px; border-radius: 4px; font-family: monospace;">F</kbd></td>
            <td>Open Formula Sheet</td>
          </tr>
          <tr>
            <td><kbd style="background: rgba(255,255,255,0.1); padding: 3px 8px; border-radius: 4px; font-family: monospace;">Esc</kbd></td>
            <td>Close open modals</td>
          </tr>
        </tbody>
      </table>

      <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: var(--radius-md); padding: 0.85rem 1.15rem; font-size: 0.85rem;">
        <strong style="color: #10b981;">💡 Spaced Repetition Advice:</strong>
        <p style="color: var(--text-secondary); margin-top: 0.25rem;">
          Your progress is automatically saved in your browser. Review the cards marked "Still Need Practice" until the mastery progress reaches 100%!
        </p>
      </div>
    </div>
  </div>

  <!-- CELEBRATION TOAST -->
  <div class="celebration-toast" id="celebrationToast">
    <span>🏆</span>
    <span id="toastMessage">Outstanding! Question Mastered!</span>
  </div>

  <!-- INLINE APPLICATION LOGIC & DATA -->
  <script>
    // EMBEDDED DATA
    const CARDS = __CARDS_JSON__;
    const IMAGES = __IMAGES_JSON__;

    // LOCAL STORAGE STATE
    const STORAGE_KEY = 'gcse_p3_revision_state_v1';
    let userState = {
      cardStatus: {}, // id: 'unseen' | 'learning' | 'mastered'
      soundEnabled: true,
      currentFilter: 'all',
      currentIndex: 0
    };

    function loadState() {
      try {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {
          const parsed = JSON.parse(saved);
          userState = { ...userState, ...parsed };
        }
      } catch (e) {
        console.warn('Could not load progress from localStorage', e);
      }
    }

    function saveState() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
          cardStatus: userState.cardStatus,
          soundEnabled: userState.soundEnabled
        }));
      } catch (e) {
        console.warn('Could not save progress to localStorage', e);
      }
    }

    // WEB AUDIO SYNTHESIZER (No external audio files needed!)
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    function playBeep(type) {
      if (!userState.soundEnabled) return;
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);

      const now = audioCtx.currentTime;

      if (type === 'flip') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.08);
        gain.gain.setValueAtTime(0.04, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        osc.start(now);
        osc.stop(now + 0.08);
      } else if (type === 'master') {
        // High dual-tone chime
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(587.33, now); // D5
        osc.frequency.setValueAtTime(880, now + 0.1); // A5
        gain.gain.setValueAtTime(0.08, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
        osc.start(now);
        osc.stop(now + 0.35);
      } else if (type === 'review') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(329.63, now); // E4
        gain.gain.setValueAtTime(0.05, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
        osc.start(now);
        osc.stop(now + 0.15);
      } else if (type === 'reset') {
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.linearRampToValueAtTime(110, now + 0.2);
        gain.gain.setValueAtTime(0.03, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
        osc.start(now);
        osc.stop(now + 0.2);
      }
    }

    // STATE VARIABLES
    let currentDeck = [...CARDS];
    let isFlipped = false;

    // DOM ELEMENTS
    const gridView = document.getElementById('gridView');
    const focusView = document.getElementById('focusView');
    const revisionMatrix = document.getElementById('revisionMatrix');
    const btnViewGrid = document.getElementById('btnViewGrid');
    const btnViewFocus = document.getElementById('btnViewFocus');
    const btnBackToGrid = document.getElementById('btnBackToGrid');
    
    // Progress Elements
    const progressBarFill = document.getElementById('progressBarFill');
    const progressPercentText = document.getElementById('progressPercentText');
    const progressRatioText = document.getElementById('progressRatioText');
    const statMasteredCount = document.getElementById('statMasteredCount');
    const statLearningCount = document.getElementById('statLearningCount');
    const statUnseenCount = document.getElementById('statUnseenCount');

    // Focus Card Elements
    const flashcardInner = document.getElementById('flashcardInner');
    const frontTopicIndicator = document.getElementById('frontTopicIndicator');
    const frontMarksBadge = document.getElementById('frontMarksBadge');
    const frontQuestionNum = document.getElementById('frontQuestionNum');
    const frontQuestionText = document.getElementById('frontQuestionText');
    const btnToggleHint = document.getElementById('btnToggleHint');
    const hintTextBox = document.getElementById('hintTextBox');
    const btnFlipCardFront = document.getElementById('btnFlipCardFront');
    const btnFlipCardBack = document.getElementById('btnFlipCardBack');
    const deckCounter = document.getElementById('deckCounter');
    const focusCardStatusBadge = document.getElementById('focusCardStatusBadge');

    // Back Card Elements
    const backCardTitle = document.getElementById('backCardTitle');
    const markSchemeList = document.getElementById('markSchemeList');
    const calcBreakdownBox = document.getElementById('calcBreakdownBox');
    const calcFormula = document.getElementById('calcFormula');
    const calcGiven = document.getElementById('calcGiven');
    const calcWorking = document.getElementById('calcWorking');
    const calcResult = document.getElementById('calcResult');
    const diagramContainer = document.getElementById('diagramContainer');
    const diagramWrapper = document.getElementById('diagramWrapper');
    const diagramImage = document.getElementById('diagramImage');
    const diagramCaptionText = document.getElementById('diagramCaptionText');
    const examinerTipBox = document.getElementById('examinerTipBox');
    const examinerTipText = document.getElementById('examinerTipText');
    const btnRateLearning = document.getElementById('btnRateLearning');
    const btnRateMastered = document.getElementById('btnRateMastered');
    const btnPrevCard = document.getElementById('btnPrevCard');
    const btnNextCard = document.getElementById('btnNextCard');
    const jumpDotsList = document.getElementById('jumpDotsList');

    // Modals
    const formulaModal = document.getElementById('formulaModal');
    const btnFormulaSheet = document.getElementById('btnFormulaSheet');
    const btnCloseFormulaModal = document.getElementById('btnCloseFormulaModal');

    const lightboxModal = document.getElementById('lightboxModal');
    const lightboxImage = document.getElementById('lightboxImage');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxCaption = document.getElementById('lightboxCaption');
    const btnCloseLightbox = document.getElementById('btnCloseLightbox');

    const helpModal = document.getElementById('helpModal');
    const btnHelp = document.getElementById('btnHelp');
    const btnCloseHelpModal = document.getElementById('btnCloseHelpModal');

    // Other Buttons
    const btnShuffle = document.getElementById('btnShuffle');
    const btnResetProgress = document.getElementById('btnResetProgress');
    const btnToggleSound = document.getElementById('btnToggleSound');
    const btnToggleTheme = document.getElementById('btnToggleTheme');
    const celebrationToast = document.getElementById('celebrationToast');
    const toastMessage = document.getElementById('toastMessage');

    // INITIALIZATION
    function init() {
      loadState();
      applyTheme();
      updateSoundButtonUI();
      renderMatrix();
      renderJumpDots();
      updateProgressStats();
      showCard(userState.currentIndex);

      setupEventListeners();
    }

    // THEME HANDLING
    function applyTheme() {
      const savedTheme = localStorage.getItem('gcse_p3_theme') || 'light';
      document.documentElement.setAttribute('data-theme', savedTheme);
      btnToggleTheme.textContent = savedTheme === 'light' ? '🌙' : '☀️';
    }

    function toggleTheme() {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('gcse_p3_theme', next);
      btnToggleTheme.textContent = next === 'light' ? '🌙' : '☀️';
      playBeep('flip');
    }

    function updateSoundButtonUI() {
      btnToggleSound.textContent = userState.soundEnabled ? '🔊' : '🔇';
      btnToggleSound.title = userState.soundEnabled ? 'Sound FX Enabled (Click to mute)' : 'Sound FX Muted (Click to enable)';
    }

    // MATRIX RENDERING (4x4 GRID)
    function renderMatrix() {
      revisionMatrix.innerHTML = '';

      CARDS.forEach(card => {
        const status = userState.cardStatus[card.id] || 'unseen';
        const hasDiag = !!card.diagramKey;
        const hasCalc = card.hasCalculation;

        const tile = document.createElement('div');
        tile.className = `matrix-tile col-${card.colSlug}`;
        tile.dataset.id = card.id;
        tile.dataset.category = card.colSlug;

        let statusText = '○ Unattempted';
        if (status === 'mastered') statusText = '✓ Mastered';
        else if (status === 'learning') statusText = '🔁 In Progress';

        tile.innerHTML = `
          <div class="tile-header">
            <span class="tile-qtag">${card.qNum}</span>
            <div class="tile-badges">
              ${hasDiag ? '<span class="badge-diagram">🖼️ Diagram</span>' : ''}
              ${hasCalc ? '<span class="badge-calc">🔢 Calc</span>' : ''}
            </div>
          </div>
          <div class="tile-body">
            <p class="tile-question">${escapeHTML(card.question)}</p>
          </div>
          <div class="tile-footer">
            <span class="status-pill ${status}">${statusText}</span>
            <span class="tile-action-hint">Study Card ➔</span>
          </div>
        `;

        tile.addEventListener('click', () => {
          const index = currentDeck.findIndex(c => c.id === card.id);
          if (index !== -1) {
            switchToFocusView(index);
          }
        });

        revisionMatrix.appendChild(tile);
      });

      applyCurrentFilter();
    }

    function escapeHTML(str) {
      return str.replace(/[&<>'"]/g, 
        tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
      );
    }

    // JUMP DOTS RENDERING
    function renderJumpDots() {
      jumpDotsList.innerHTML = '';
      currentDeck.forEach((card, idx) => {
        const dot = document.createElement('button');
        dot.className = 'jump-dot';
        dot.title = `${card.qNum}: ${card.question.substring(0, 40)}...`;

        const status = userState.cardStatus[card.id];
        if (status === 'mastered') dot.classList.add('is-mastered');
        else if (status === 'learning') dot.classList.add('is-learning');

        if (idx === userState.currentIndex) dot.classList.add('active');

        dot.addEventListener('click', () => {
          showCard(idx);
        });

        jumpDotsList.appendChild(dot);
      });
    }

    // SHOW CARD IN FOCUS VIEW
    function showCard(index) {
      if (currentDeck.length === 0) return;
      if (index < 0) index = currentDeck.length - 1;
      if (index >= currentDeck.length) index = 0;

      userState.currentIndex = index;
      const card = currentDeck[index];

      // Unflip card
      isFlipped = false;
      flashcardInner.classList.remove('flipped');
      hintTextBox.classList.remove('active');
      btnToggleHint.textContent = '💡 Show Formula / Hint';

      // Meta
      deckCounter.textContent = `Card ${index + 1} of ${currentDeck.length}`;
      const status = userState.cardStatus[card.id] || 'unseen';
      focusCardStatusBadge.className = `status-pill ${status}`;
      focusCardStatusBadge.textContent = status === 'mastered' ? '✓ Mastered' : (status === 'learning' ? '🔁 In Progress' : '○ Unattempted');

      // Front
      frontTopicIndicator.textContent = `${card.colIcon} ${card.colName}`;
      frontTopicIndicator.style.background = `var(--col${card.col}-bg)`;
      frontTopicIndicator.style.color = `var(--col${card.col}-color)`;
      frontMarksBadge.textContent = `[${card.marks} Marks]`;
      frontQuestionNum.textContent = `${card.qNum} • (Row ${card.row}, Col ${card.col})`;
      frontQuestionText.textContent = card.question;
      hintTextBox.textContent = card.note || `Formula / Concept: ${card.formula}`;

      // Back
      backCardTitle.textContent = `${card.qNum} Mark Scheme (${card.marks} Marks)`;
      markSchemeList.innerHTML = card.markScheme.map(pt => `<li>${pt}</li>`).join('');

      // Calculation
      if (card.calculation) {
        calcBreakdownBox.style.display = 'block';
        calcFormula.textContent = card.calculation.formula;
        calcGiven.textContent = card.calculation.given;
        calcWorking.textContent = card.calculation.working;
        calcResult.textContent = card.calculation.result;
      } else {
        calcBreakdownBox.style.display = 'none';
      }

      // Diagram
      if (card.diagramKey && IMAGES[card.diagramKey]) {
        diagramContainer.style.display = 'block';
        const imgUrl = IMAGES[card.diagramKey];
        diagramImage.src = imgUrl;
        diagramImage.alt = card.diagramCaption;
        diagramCaptionText.textContent = card.diagramCaption;

        diagramWrapper.onclick = () => {
          openLightbox(imgUrl, `${card.qNum}: ${card.colName} Diagram`, card.diagramCaption);
        };
      } else {
        diagramContainer.style.display = 'none';
      }

      // Examiner Tip
      examinerTipText.textContent = card.examinerTip;

      // Update Dots
      const dots = jumpDotsList.querySelectorAll('.jump-dot');
      dots.forEach((dot, dIdx) => {
        dot.classList.toggle('active', dIdx === index);
      });
    }

    function flipCard() {
      isFlipped = !isFlipped;
      flashcardInner.classList.toggle('flipped', isFlipped);
      playBeep('flip');
    }

    function rateCurrentCard(status) {
      const card = currentDeck[userState.currentIndex];
      userState.cardStatus[card.id] = status;
      saveState();

      if (status === 'mastered') {
        playBeep('master');
        showToast(`🎉 ${card.qNum} Mastered! Great job!`);
      } else {
        playBeep('review');
        showToast(`🔁 ${card.qNum} marked for review.`);
      }

      updateProgressStats();
      renderJumpDots();
      renderMatrix();

      // Automatically advance to next card after brief delay
      setTimeout(() => {
        showCard(userState.currentIndex + 1);
      }, 350);
    }

    function updateProgressStats() {
      let mastered = 0;
      let learning = 0;
      let unseen = 0;

      CARDS.forEach(c => {
        const s = userState.cardStatus[c.id];
        if (s === 'mastered') mastered++;
        else if (s === 'learning') learning++;
        else unseen++;
      });

      const total = CARDS.length;
      const pct = Math.round((mastered / total) * 100);

      progressBarFill.style.width = `${pct}%`;
      progressPercentText.textContent = `${pct}%`;
      progressRatioText.textContent = `${mastered}/${total}`;

      statMasteredCount.textContent = `✓ ${mastered} Mastered`;
      statLearningCount.textContent = `🔁 ${learning} In Progress`;
      statUnseenCount.textContent = `○ ${unseen} Unattempted`;

      if (mastered === total && total > 0) {
        showToast('🏆 100% MASTERY! You are completely ready for GCSE P3!');
      }
    }

    function showToast(msg) {
      toastMessage.textContent = msg;
      celebrationToast.classList.add('show');
      setTimeout(() => {
        celebrationToast.classList.remove('show');
      }, 2500);
    }

    // VIEW SWITCHING
    function switchToGridView() {
      gridView.classList.remove('hidden');
      focusView.classList.remove('active');
      btnViewGrid.classList.add('active');
      btnViewFocus.classList.remove('active');
      playBeep('flip');
    }

    function switchToFocusView(cardIndex = 0) {
      gridView.classList.add('hidden');
      focusView.classList.add('active');
      btnViewGrid.classList.remove('active');
      btnViewFocus.classList.add('active');
      showCard(cardIndex);
      window.scrollTo({ top: 120, behavior: 'smooth' });
      playBeep('flip');
    }

    // FILTERING
    function applyCurrentFilter() {
      const filter = userState.currentFilter;
      const tiles = revisionMatrix.querySelectorAll('.matrix-tile');

      tiles.forEach(tile => {
        const cat = tile.dataset.category;
        if (filter === 'all' || filter === cat) {
          tile.style.display = 'flex';
        } else {
          tile.style.display = 'none';
        }
      });

      // Filter active deck if in focus view
      if (filter === 'all') {
        currentDeck = [...CARDS];
      } else {
        currentDeck = CARDS.filter(c => c.colSlug === filter);
      }
      renderJumpDots();
    }

    // LIGHTBOX
    function openLightbox(src, title, caption) {
      lightboxImage.src = src;
      lightboxTitle.textContent = title;
      lightboxCaption.textContent = caption;
      lightboxModal.classList.add('open');
      playBeep('flip');
    }

    function closeLightbox() {
      lightboxModal.classList.remove('open');
    }

    // EVENT LISTENERS
    function setupEventListeners() {
      // Views
      btnViewGrid.addEventListener('click', switchToGridView);
      btnViewFocus.addEventListener('click', () => switchToFocusView(userState.currentIndex));
      btnBackToGrid.addEventListener('click', switchToGridView);

      // Card flipping
      btnFlipCardFront.addEventListener('click', flipCard);
      btnFlipCardBack.addEventListener('click', flipCard);

      // Hint toggle
      btnToggleHint.addEventListener('click', (e) => {
        e.stopPropagation();
        const active = hintTextBox.classList.toggle('active');
        btnToggleHint.textContent = active ? '🙈 Hide Hint' : '💡 Show Formula / Hint';
        playBeep('flip');
      });

      // Rating
      btnRateLearning.addEventListener('click', (e) => {
        e.stopPropagation();
        rateCurrentCard('learning');
      });
      btnRateMastered.addEventListener('click', (e) => {
        e.stopPropagation();
        rateCurrentCard('mastered');
      });

      // Navigation
      btnPrevCard.addEventListener('click', () => {
        showCard(userState.currentIndex - 1);
        playBeep('flip');
      });
      btnNextCard.addEventListener('click', () => {
        showCard(userState.currentIndex + 1);
        playBeep('flip');
      });

      // Shuffle
      btnShuffle.addEventListener('click', () => {
        currentDeck = [...currentDeck].sort(() => Math.random() - 0.5);
        userState.currentIndex = 0;
        renderJumpDots();
        showCard(0);
        showToast('🔀 Flashcard deck shuffled!');
        playBeep('flip');
      });

      // Reset
      btnResetProgress.addEventListener('click', () => {
        if (confirm('Are you sure you want to reset all your revision progress?')) {
          userState.cardStatus = {};
          saveState();
          updateProgressStats();
          renderMatrix();
          renderJumpDots();
          showCard(userState.currentIndex);
          playBeep('reset');
          showToast('↺ Progress reset. Start fresh!');
        }
      });

      // Sound Toggle
      btnToggleSound.addEventListener('click', () => {
        userState.soundEnabled = !userState.soundEnabled;
        saveState();
        updateSoundButtonUI();
        if (userState.soundEnabled) playBeep('master');
      });

      // Theme Toggle
      btnToggleTheme.addEventListener('click', toggleTheme);

      // Filter Chips
      document.querySelectorAll('.filter-chip').forEach(chip => {
        chip.addEventListener('click', () => {
          document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          userState.currentFilter = chip.dataset.filter;
          applyCurrentFilter();
          userState.currentIndex = 0;
          showCard(0);
          playBeep('flip');
        });
      });

      // Formula Modal
      btnFormulaSheet.addEventListener('click', () => {
        formulaModal.classList.add('open');
        playBeep('flip');
      });
      btnCloseFormulaModal.addEventListener('click', () => {
        formulaModal.classList.remove('open');
      });
      formulaModal.addEventListener('click', (e) => {
        if (e.target === formulaModal) formulaModal.classList.remove('open');
      });

      // Help Modal
      btnHelp.addEventListener('click', () => {
        helpModal.classList.add('open');
        playBeep('flip');
      });
      btnCloseHelpModal.addEventListener('click', () => {
        helpModal.classList.remove('open');
      });
      helpModal.addEventListener('click', (e) => {
        if (e.target === helpModal) helpModal.classList.remove('open');
      });

      // Lightbox
      btnCloseLightbox.addEventListener('click', closeLightbox);
      lightboxModal.addEventListener('click', (e) => {
        if (e.target === lightboxModal) closeLightbox();
      });

      // Keyboard Shortcuts
      window.addEventListener('keydown', (e) => {
        // Close modals on Escape
        if (e.key === 'Escape') {
          formulaModal.classList.remove('open');
          helpModal.classList.remove('open');
          lightboxModal.classList.remove('open');
          return;
        }

        // If a modal is open, ignore other keys
        if (formulaModal.classList.contains('open') || helpModal.classList.contains('open') || lightboxModal.classList.contains('open')) {
          return;
        }

        // Space or Enter: Flip card
        if (e.code === 'Space' || e.key === 'Enter') {
          if (focusView.classList.contains('active')) {
            e.preventDefault();
            flipCard();
          }
        } else if (e.key === 'ArrowRight') {
          if (focusView.classList.contains('active')) {
            e.preventDefault();
            showCard(userState.currentIndex + 1);
            playBeep('flip');
          }
        } else if (e.key === 'ArrowLeft') {
          if (focusView.classList.contains('active')) {
            e.preventDefault();
            showCard(userState.currentIndex - 1);
            playBeep('flip');
          }
        } else if (e.key === '1') {
          if (focusView.classList.contains('active')) {
            rateCurrentCard('learning');
          }
        } else if (e.key === '2') {
          if (focusView.classList.contains('active')) {
            rateCurrentCard('mastered');
          }
        } else if (e.key.toLowerCase() === 'g') {
          switchToGridView();
        } else if (e.key.toLowerCase() === 'f') {
          formulaModal.classList.add('open');
          playBeep('flip');
        } else if (e.key === '?') {
          helpModal.classList.add('open');
          playBeep('flip');
        }
      });
    }

    // BOOTSTRAP
    document.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>"""

# Replace placeholders
final_html = html_template.replace('__CARDS_JSON__', json.dumps(cards_data))
final_html = final_html.replace('__IMAGES_JSON__', json.dumps(images_b64))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated index.html successfully!")
print(f"File size: {os.path.getsize('index.html')} bytes")
