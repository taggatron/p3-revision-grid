# GCSE Combined Science (Gateway J250) – P3 Revision Grid

An interactive, self-contained revision flashcard website designed for **OCR Gateway Combined Science Physics: Topic P3 (Electricity & Magnetism)**.

## 🚀 Quick Start
- Simply double-click **`index.html`** in any web browser (Chrome, Safari, Firefox, Edge).
- Completely self-contained: all code, styles, and high-resolution diagrams are embedded directly within `index.html` (no build step or server required).

## 🌐 Deploy to GitHub Pages (Free & Instant)
1. Initialize a git repository and push this folder to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of P3 Revision Grid"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```
2. In your GitHub repository:
   - Go to **Settings** > **Pages**.
   - Under **Source**, select **Deploy from a branch** -> branch: **`main`**, folder: **`/ (root)`**.
   - Click **Save**. Your revision app will be live at `https://<your-username>.github.io/<your-repo-name>/`!

## ⚡ Features
- **4×4 Revision Grid**: Complete interactive grid matching the 4 topics and 16 end-of-topic test questions:
  1. *Charge, Current & Time* (Q1, Q5, Q9, Q13)
  2. *Energy & Power* (Q2, Q6, Q10, Q14)
  3. *Circuits & Resistance* (Q3, Q7, Q11, Q15)
  4. *Magnetism & Electromagnetism* (Q4, Q8, Q12, Q16)
- **3D Flip Flashcard Mode**: Smooth flip animations between questions and official OCR mark schemes.
- **Scientific Diagrams (Google Gemini Generated)**: High-resolution textbook illustrations with zoom lightbox on key concepts (Electrostatics, Circuit resistance measurement, Wire magnetic field, Earth magnetism, Parallel circuit current splitting, Electromagnet & induced nails, LDR experiment, and the Motor Effect).
- **Step-by-step Calculations**: Full working for all calculation questions ($E = Q \times V$, $Q = I \times t$, $E = P \times t$, $P = V \times I$, $F = B \times I \times l$, and unit conversions).
- **Formula Sheet Reference**: Built-in modal listing all P3 equations, SI units, and metric multipliers.
- **Spaced Repetition & Progress Tracker**: Marks cards as *Mastered* or *In Progress* with automatic `localStorage` persistence.
- **Dark & Light Mode**: Clean, accessible themes with toggle.
- **Audio Feedback**: Native Web Audio API sound effects (no external audio assets).
- **Keyboard Shortcuts**: Power-user navigation (`Space`, `←`/`→`, `1`/`2`, `G`, `F`, `Esc`, `?`).
- **Print Friendly**: Dedicated `@media print` styling for revision handouts.
