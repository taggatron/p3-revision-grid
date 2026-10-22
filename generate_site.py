import json
import os

with open('images_b64.json', 'r') as f:
    images_b64 = json.load(f)

cards_data = [
    # ROW 1
    {
        "id": 1,
        "row": 1,
        "col": 1,
        "colName": "Charge, Current & Time",
        "colSlug": "charge",
        "colIcon": "⚡",
        "qNum": "Q1",
        "question": "Explain how rubbing an insulating object with a cloth causes the object to become positively charged.",
        "answer": "Negatively charged electrons are transferred (move) from the object to the cloth by friction, leaving the object with a net positive charge.",
        "note": "Note: Protons do not move — they are bound inside atomic nuclei!",
        "marks": 2,
        "markScheme": [
            "Friction causes <strong>negatively charged electrons to transfer (move)</strong> from the object to the cloth [1 mark].",
            "Loss of negative electrons leaves the insulating object with an excess of positive charge (<strong>net positive charge</strong>) [1 mark]."
        ],
        "examinerTip": "Common student pitfall: Never state that 'positive charges move' or 'protons move'. Protons are tightly bound in the nuclei of atoms and do not move. Only negative electrons transfer during charging by friction!",
        "diagramKey": "q1_static_charging",
        "diagramCaption": "Electrostatic charging by friction: Electrons transfer from the insulating rod to the cloth, leaving the rod with a net positive charge.",
        "hasCalculation": False,
        "formula": "Static Electricity & Electron Transfer"
    },
    {
        "id": 2,
        "row": 1,
        "col": 2,
        "colName": "Energy & Power",
        "colSlug": "energy",
        "colIcon": "💡",
        "qNum": "Q2",
        "question": "A 4 V power supply is connected to a motor. If 150 C of charge passes through it in 30 s, how much energy is transferred?",
        "answer": "Use E = Q × V: E = 150 C × 4 V = 600 J. (The time of 30 s is a distractor and not needed).",
        "note": "Distractor Alert: Time (30 s) is not required for this formula!",
        "marks": 2,
        "markScheme": [
            "Select formula: <code>E = Q × V</code> [1 mark]",
            "Substitution & calculation: <code>E = 150 C × 4 V = <strong>600 J</strong></code> [1 mark]"
        ],
        "calculation": {
            "formula": "E = Q × V",
            "given": "Potential Difference (V) = 4 V, Charge (Q) = 150 C, Time (t) = 30 s [Distractor]",
            "working": "E = 150 C × 4 V",
            "result": "600 J (or 0.6 kJ)"
        },
        "examinerTip": "Distractor trap! Exam boards frequently provide extra values (like 30 seconds here) to test whether you understand the correct formula. Always identify what you are asked to calculate (Energy, E) and what is given (Q and V).",
        "diagramKey": None,
        "hasCalculation": True,
        "formula": "E = Q × V"
    },
    {
        "id": 3,
        "row": 1,
        "col": 3,
        "colName": "Circuits & Resistance",
        "colSlug": "circuits",
        "colIcon": "🔌",
        "qNum": "Q3",
        "question": "Describe how an ammeter and a voltmeter must be connected in a circuit to find the resistance of a component (like a fixed resistor or LDR).",
        "answer": "The ammeter must be connected in series with the component, and the voltmeter must be connected in parallel across the component.",
        "note": "Ammeter in series (measures current I); Voltmeter in parallel (measures potential difference V).",
        "marks": 2,
        "markScheme": [
            "Ammeter connected in <strong>series</strong> with the component [1 mark].",
            "Voltmeter connected in <strong>parallel</strong> across the component [1 mark]."
        ],
        "examinerTip": "To calculate resistance, use Ohm's Law: <code>R = V / I</code>. The ammeter has very low resistance so it doesn't restrict current in series. The voltmeter has extremely high resistance so negligible current passes through it in parallel.",
        "diagramKey": "q3_circuit_resistance",
        "diagramCaption": "Standard GCSE circuit setup: Ammeter placed in series with resistor; Voltmeter connected in parallel across resistor.",
        "hasCalculation": False,
        "formula": "R = V / I (Ohm's Law)"
    },
    {
        "id": 4,
        "row": 1,
        "col": 4,
        "colName": "Magnetism & Electromagnetism",
        "colSlug": "magnetism",
        "colIcon": "🧲",
        "qNum": "Q4",
        "question": "What two changes would cause the largest increase in the magnetic field strength recorded at a point near a current-carrying wire?",
        "answer": "1. Increase the current in the wire.\n2. Move the detector closer to the wire.",
        "note": "Magnetic flux density B is directly proportional to current (I) and inversely proportional to distance (d).",
        "marks": 2,
        "markScheme": [
            "<strong>Increase the current</strong> flowing through the wire [1 mark].",
            "<strong>Decrease the distance</strong> / move the point/detector <strong>closer to the wire</strong> [1 mark]."
        ],
        "examinerTip": "Field strength formula relationship: <code>B ∝ I / d</code>. Field lines form concentric circles around the wire that get further apart as distance increases.",
        "diagramKey": "q4_magnetic_field_wire",
        "diagramCaption": "Concentric magnetic field lines around a current-carrying wire. Field strength increases with higher current and closer distance.",
        "hasCalculation": False,
        "formula": "B ∝ I / d"
    },

    # ROW 2
    {
        "id": 5,
        "row": 2,
        "col": 1,
        "colName": "Charge, Current & Time",
        "colSlug": "charge",
        "colIcon": "⚡",
        "qNum": "Q5",
        "question": "What two pieces of measuring equipment must a student use to find the total charge transferred when a device is charged?",
        "answer": "An ammeter (to measure current) and a stopwatch (to measure time), using the equation Q = I × t.",
        "note": "Required apparatus: Ammeter (current in Amps) and Stopwatch/Timer (time in seconds).",
        "marks": 2,
        "markScheme": [
            "<strong>Ammeter</strong> (to measure electric current, I) [1 mark].",
            "<strong>Stopwatch / Stopclock / Timer</strong> (to measure elapsed time, t) [1 mark]."
        ],
        "examinerTip": "Whenever an exam asks 'how to measure charge', remember there is no common direct 'charge meter' used in school labs; you measure current with an ammeter and time with a stopwatch, then calculate <code>Q = I × t</code>.",
        "diagramKey": None,
        "hasCalculation": False,
        "formula": "Q = I × t"
    },
    {
        "id": 6,
        "row": 2,
        "col": 2,
        "colName": "Energy & Power",
        "colSlug": "energy",
        "colIcon": "💡",
        "qNum": "Q6",
        "question": "A 12 V battery provides a current of 0.5 A in a circuit for 40 seconds. Calculate the total energy transferred by the battery.",
        "answer": "First find charge: Q = I × t = 0.5 A × 40 s = 20 C. Then find energy: E = Q × V = 20 C × 12 V = 240 J.",
        "note": "Can also be calculated in one step: E = V × I × t = 12 × 0.5 × 40 = 240 J.",
        "marks": 3,
        "markScheme": [
            "Calculate charge: <code>Q = I × t = 0.5 A × 40 s = 20 C</code> [1 mark]",
            "Calculate energy: <code>E = Q × V = 20 C × 12 V</code> [1 mark]",
            "Correct final answer with units: <strong>240 J</strong> [1 mark]"
        ],
        "calculation": {
            "formula": "Method 1: Q = I × t, then E = Q × V | Method 2: E = V × I × t",
            "given": "Potential Difference (V) = 12 V, Current (I) = 0.5 A, Time (t) = 40 s",
            "working": "Q = 0.5 A × 40 s = 20 C\nE = 20 C × 12 V = 240 J\n(Or E = 12 V × 0.5 A × 40 s = 240 J)",
            "result": "240 J"
        },
        "examinerTip": "Both methods are 100% accepted in GCSE Gateway mark schemes. Ensure you always write the units (J for Joules) to secure the final mark.",
        "diagramKey": None,
        "hasCalculation": True,
        "formula": "E = Q × V = V × I × t"
    },
    {
        "id": 7,
        "row": 2,
        "col": 3,
        "colName": "Circuits & Resistance",
        "colSlug": "circuits",
        "colIcon": "🔌",
        "qNum": "Q7",
        "question": "As more identical lamps are added in parallel to a circuit powered by a 6.0 V cell, what happens to the total resistance of the circuit and the current through the cell?",
        "answer": "Adding lamps in parallel decreases the total resistance of the circuit (because there are more pathways for current to flow), which increases the total current flowing through the cell.",
        "note": "More parallel branches = lower total circuit resistance = higher current from the cell.",
        "marks": 2,
        "markScheme": [
            "Total resistance of the circuit <strong>decreases</strong> (more parallel pathways/branches) [1 mark].",
            "Total current through the cell <strong>increases</strong> [1 mark]."
        ],
        "examinerTip": "Think of parallel branches like opening extra toll booths on a motorway: even if each booth is narrow, opening more booths allows more total traffic (current) to pass through per second, reducing overall restriction (resistance).",
        "diagramKey": None,
        "hasCalculation": False,
        "formula": "1 / R_total = 1 / R1 + 1 / R2 + ..."
    },
    {
        "id": 8,
        "row": 2,
        "col": 4,
        "colName": "Magnetism & Electromagnetism",
        "colSlug": "magnetism",
        "colIcon": "🧲",
        "qNum": "Q8",
        "question": "The North pole of a compass needle points towards the Earth's geographic North pole. What type of magnetic pole is located near the Earth's geographic North pole, and what is the direction of magnetic field lines?",
        "answer": "There is a South (S) magnetic pole near the Earth's geographic North pole (since opposite poles attract). Magnetic field lines always point from North to South (N to S).",
        "note": "Opposites attract: North pole of compass is attracted to a magnetic South pole.",
        "marks": 2,
        "markScheme": [
            "The magnetic pole near Earth's geographic North is a <strong>magnetic South (S) pole</strong> [1 mark].",
            "Magnetic field lines always point from <strong>North to South (N to S)</strong> [1 mark]."
        ],
        "examinerTip": "Crucial distinction! A compass needle is a permanent magnet whose North pole is attracted towards the Arctic. Because opposite magnetic poles attract, the magnetic pole in the northern hemisphere is physically a magnetic South pole.",
        "diagramKey": "q8_earth_magnetism",
        "diagramCaption": "The Earth's magnetic field: Showing the internal bar magnet model with magnetic South located near geographic North, and field lines traveling from North to South.",
        "hasCalculation": False,
        "formula": "Opposite poles attract; Field lines: N → S"
    },

    # ROW 3
    {
        "id": 9,
        "row": 3,
        "col": 1,
        "colName": "Charge, Current & Time",
        "colSlug": "charge",
        "colIcon": "⚡",
        "qNum": "Q9",
        "question": "A tablet is charged for 2 hours using a mean charging current of 0.25 A. Calculate the total charge transferred in Coulombs (C).",
        "answer": "First convert time to seconds: t = 2 hours × 60 mins × 60 s = 7200 s. Then use Q = I × t: Q = 0.25 A × 7200 s = 1800 C.",
        "note": "Unit Conversion: Always convert hours to seconds before calculating!",
        "marks": 3,
        "markScheme": [
            "Convert time to seconds: <code>t = 2 × 60 × 60 = 7200 s</code> [1 mark]",
            "Formula & substitution: <code>Q = I × t = 0.25 A × 7200 s</code> [1 mark]",
            "Correct answer with units: <strong>1800 C</strong> [1 mark]"
        ],
        "calculation": {
            "formula": "Q = I × t",
            "given": "Time (t) = 2 hours, Current (I) = 0.25 A",
            "working": "t = 2 × 3600 s = 7200 s\nQ = 0.25 A × 7200 s = 1800 C",
            "result": "1800 C (1.8 × 10³ C)"
        },
        "examinerTip": "Number one cause of lost marks: Forgetting unit conversions! Current must be in Amps (A) and time MUST be in seconds (s). 1 hour = 3600 seconds, so 2 hours = 7200 seconds.",
        "diagramKey": None,
        "hasCalculation": True,
        "formula": "Q = I × t"
    },
    {
        "id": 10,
        "row": 3,
        "col": 2,
        "colName": "Energy & Power",
        "colSlug": "energy",
        "colIcon": "💡",
        "qNum": "Q10",
        "question": "A 2500 W electric heater is switched on for 4 hours. Calculate the energy transferred in kilowatt-hours (kWh).",
        "answer": "First convert power to kilowatts: 2500 W = 2.5 kW. Then use E = P × t: E = 2.5 kW × 4 h = 10 kWh. (Bonus: 1 kWh = 3,600,000 J or 3.6 × 10^6 J).",
        "note": "Notice the unit requested is kWh: keep power in kW and time in hours!",
        "marks": 2,
        "markScheme": [
            "Convert power from Watts to kilowatts: <code>2500 W = 2.5 kW</code> [1 mark]",
            "Calculate energy in kWh: <code>E = P × t = 2.5 kW × 4 h = <strong>10 kWh</strong></code> [1 mark]"
        ],
        "calculation": {
            "formula": "E (kWh) = Power (kW) × Time (hours)",
            "given": "Power (P) = 2500 W = 2.5 kW, Time (t) = 4 hours",
            "working": "E = 2.5 kW × 4 h = 10 kWh\nBonus conversion to Joules: 10 kWh × 3,600,000 J = 3.6 × 10⁷ J (36 MJ)",
            "result": "10 kWh"
        },
        "examinerTip": "Pay close attention to units in the question! If asked for kWh, power must be in kW (divide W by 1000) and time must remain in hours. If asked for Joules, time must be in seconds and power in Watts.",
        "diagramKey": None,
        "hasCalculation": True,
        "formula": "E = P × t (kWh = kW × h)"
    },
    {
        "id": 11,
        "row": 3,
        "col": 3,
        "colName": "Circuits & Resistance",
        "colSlug": "circuits",
        "colIcon": "🔌",
        "qNum": "Q11",
        "question": "In a parallel circuit with two branches, Branch 1 has a resistor with 0.6 A flowing through it, and Branch 2 has an identical resistor with 0.6 A flowing through it. What is the total current in the main circuit before the branches split?",
        "answer": "In a parallel circuit, the current splits at a junction, so the main current is the sum of the currents in the branches: I_total = 0.6 A + 0.6 A = 1.2 A.",
        "note": "Conservation of Charge: Total current entering a junction equals total current leaving it.",
        "marks": 2,
        "markScheme": [
            "Current in parallel branches adds up to give total circuit current: <code>I_total = I₁ + I₂</code> [1 mark]",
            "Calculation: <code>0.6 A + 0.6 A = <strong>1.2 A</strong></code> [1 mark]"
        ],
        "calculation": {
            "formula": "I_total = I₁ + I₂",
            "given": "Branch 1 current (I₁) = 0.6 A, Branch 2 current (I₂) = 0.6 A",
            "working": "I_total = 0.6 A + 0.6 A = 1.2 A",
            "result": "1.2 A"
        },
        "examinerTip": "In parallel circuits: Current is shared between branches (splits at junctions), while potential difference (voltage) is the same across each parallel branch.",
        "diagramKey": "q11_parallel_current",
        "diagramCaption": "Parallel circuit current splitting: Current of 1.2 A splits into 0.6 A across each branch, then recombines to 1.2 A after the junction.",
        "hasCalculation": True,
        "formula": "I_total = I₁ + I₂"
    },
    {
        "id": 12,
        "row": 3,
        "col": 4,
        "colName": "Magnetism & Electromagnetism",
        "colSlug": "magnetism",
        "colIcon": "🧲",
        "qNum": "Q12",
        "question": "Why does a chain of iron nails get attracted to an electromagnet when it is switched on? What type of magnet does each iron nail become?",
        "answer": "The magnetic field of the electromagnet magnetises the iron nails. Each iron nail becomes an induced (temporary) magnet with its own North and South poles, attracting the next nail in the chain.",
        "note": "Key term: Induced magnet / Temporary magnet. Soft iron loses magnetism when current turns off.",
        "marks": 2,
        "markScheme": [
            "The external magnetic field magnetises the nails, making each nail an <strong>induced magnet (or temporary magnet)</strong> [1 mark].",
            "Each nail develops opposite induced poles (North and South), attracting the next nail in sequence [1 mark]."
        ],
        "examinerTip": "Permanent magnets retain their magnetism indefinitely (e.g., steel bar magnet). Induced magnets (like iron nails) only display magnetic properties while inside an external magnetic field and demagnetise once the field is removed.",
        "diagramKey": "q12_electromagnet_nails",
        "diagramCaption": "Induced magnetism in a chain of iron nails suspended from an electromagnet. Each nail develops opposite poles that cling together.",
        "hasCalculation": False,
        "formula": "Induced Magnetism"
    },

    # ROW 4
    {
        "id": 13,
        "row": 4,
        "col": 1,
        "colName": "Charge, Current & Time",
        "colSlug": "charge",
        "colIcon": "⚡",
        "qNum": "Q13",
        "question": "A residual current device (RCD) detects a fault where 150 mA flows through a body for 0.3 s. Calculate the charge flow in Coulombs (C).",
        "answer": "First convert current to Amperes: 150 mA = 0.15 A. Then use Q = I × t: Q = 0.15 A × 0.3 s = 0.045 C.",
        "note": "Unit conversion: 150 mA = 0.15 A (divide by 1000).",
        "marks": 2,
        "markScheme": [
            "Convert milliAmps to Amps: <code>150 mA = 0.15 A</code> [1 mark]",
            "Formula & calculation: <code>Q = I × t = 0.15 A × 0.3 s = <strong>0.045 C</strong></code> (or <code>4.5 × 10⁻² C</code>) [1 mark]"
        ],
        "calculation": {
            "formula": "Q = I × t",
            "given": "Current (I) = 150 mA = 0.15 A, Time (t) = 0.3 s",
            "working": "Q = 0.15 A × 0.3 s = 0.045 C",
            "result": "0.045 C (or 45 mC)"
        },
        "examinerTip": "Milli (m) means one-thousandth (÷ 1000). 150 mA = 150 / 1000 = 0.15 A. Forgetting to divide by 1000 is an immediate penalty!",
        "diagramKey": None,
        "hasCalculation": True,
        "formula": "Q = I × t"
    },
    {
        "id": 14,
        "row": 4,
        "col": 2,
        "colName": "Energy & Power",
        "colSlug": "energy",
        "colIcon": "💡",
        "qNum": "Q14",
        "question": "An LDR has a resistance of 4000 Ω when the potential difference across it is 8.0 V. Calculate the power dissipated by the LDR in Watts (W). (Hint: Use V = I × R and P = V × I or P = V² / R).",
        "answer": "First find current using I = V / R = 8.0 V / 4000 Ω = 0.002 A. Then find power using P = V × I = 8.0 V × 0.002 A = 0.016 W (or 16 mW).",
        "note": "Alternative: P = V² / R = 8.0² / 4000 = 64 / 4000 = 0.016 W.",
        "marks": 3,
        "markScheme": [
            "Calculate current: <code>I = V / R = 8.0 V / 4000 Ω = 0.002 A</code> [1 mark]",
            "Calculate power: <code>P = V × I = 8.0 V × 0.002 A</code> [1 mark]",
            "Final answer with units: <strong>0.016 W</strong> (or <strong>16 mW</strong>) [1 mark]",
            "(Alternative full marks for: <code>P = V² / R = 64 / 4000 = 0.016 W</code>)"
        ],
        "calculation": {
            "formula": "Method A: I = V / R then P = V × I | Method B: P = V² / R",
            "given": "Resistance (R) = 4000 Ω, Potential Difference (V) = 8.0 V",
            "working": "Method A:\nI = 8.0 / 4000 = 0.002 A\nP = 8.0 × 0.002 = 0.016 W\n\nMethod B:\nP = (8.0)² / 4000 = 64 / 4000 = 0.016 W",
            "result": "0.016 W (16 mW)"
        },
        "examinerTip": "Either two-step calculation (Ohm's Law followed by Power) or direct combined formula <code>P = V² / R</code> gains maximum marks. Watch decimal places carefully!",
        "diagramKey": None,
        "hasCalculation": True,
        "formula": "P = V × I = V² / R"
    },
    {
        "id": 15,
        "row": 4,
        "col": 3,
        "colName": "Circuits & Resistance",
        "colSlug": "circuits",
        "colIcon": "🔌",
        "qNum": "Q15",
        "question": "A student wants to investigate how light intensity affects the resistance of an LDR using a lamp and standard lab equipment. Explain one way they could systematically vary the light intensity hitting the LDR.",
        "answer": "They could use a metre ruler to vary the distance between the lamp and the LDR (e.g., moving the lamp 10 cm further away each time), or connect a variable resistor in series with the lamp to change its brightness.",
        "note": "Practical skill: Systematically change distance using a metre ruler or adjust lamp brightness with a rheostat.",
        "marks": 2,
        "markScheme": [
            "Use a <strong>metre ruler</strong> to vary the <strong>distance</strong> between the lamp and the LDR at regular intervals (e.g., in 10 cm increments) [1 mark].",
            "Alternative credit: Connect a <strong>variable resistor (rheostat)</strong> in series with the lamp to adjust current/brightness [1 mark]."
        ],
        "examinerTip": "Key LDR mnemonic to memorise: <strong>LURD</strong> = <em>Light Up, Resistance Down</em>! In darkness, an LDR has high resistance (e.g. 1 MΩ); under bright illumination, its resistance drops to a few hundred Ohms.",
        "diagramKey": "q15_ldr_experiment",
        "diagramCaption": "Investigating LDR resistance vs distance: Using a metre ruler to systematically alter light intensity, alongside the LURD characteristic curve.",
        "hasCalculation": False,
        "formula": "LURD: Light Up, Resistance Down"
    },
    {
        "id": 16,
        "row": 4,
        "col": 4,
        "colName": "Magnetism & Electromagnetism",
        "colSlug": "magnetism",
        "colIcon": "🧲",
        "qNum": "Q16",
        "question": "A wire coil in an electric motor has 0.45 m of wire perpendicular to a magnetic field of flux density 2 × 10⁻⁵ T. If the current in the coil is 500 mA, calculate the force acting on the coil using F = B × I × l.",
        "answer": "First convert current to Amperes: 500 mA = 0.5 A. Then use F = B × I × l: F = (2 × 10⁻⁵ T) × 0.5 A × 0.45 m = 4.5 × 10⁻⁶ N.",
        "note": "Unit conversion: 500 mA = 0.5 A. Formula provided on Gateway formula sheet!",
        "marks": 3,
        "markScheme": [
            "Convert current to Amperes: <code>500 mA = 0.5 A</code> [1 mark]",
            "Formula and substitution: <code>F = (2 × 10⁻⁵ T) × 0.5 A × 0.45 m</code> [1 mark]",
            "Correct final answer with standard form / units: <strong>4.5 × 10⁻⁶ N</strong> (or <code>0.0000045 N</code>) [1 mark]"
        ],
        "calculation": {
            "formula": "F = B × I × l",
            "given": "Magnetic flux density (B) = 2 × 10⁻⁵ T, Current (I) = 500 mA = 0.5 A, Length (l) = 0.45 m",
            "working": "I = 500 / 1000 = 0.5 A\nF = (2 × 10⁻⁵ T) × 0.5 A × 0.45 m\nF = 1 × 10⁻⁵ × 0.45 = 4.5 × 10⁻⁶ N",
            "result": "4.5 × 10⁻⁶ N (0.0000045 N)"
        },
        "examinerTip": "The Motor Effect formula is <code>F = B × I × l</code> where B is in Tesla (T), I is in Amperes (A), and l is in metres (m). Use Fleming's Left-Hand Rule to find the direction of motion/force.",
        "diagramKey": "q16_motor_force",
        "diagramCaption": "The Motor Effect: Conductor carrying current perpendicular to magnetic field B experiences Force F. Illustrated with Fleming's Left-Hand Rule.",
        "hasCalculation": True,
        "formula": "F = B × I × l"
    }
]

print(f"Total cards prepared: {len(cards_data)}")
cards_json_str = json.dumps(cards_data)
images_json_str = json.dumps(images_b64)
print("Data JSON ready!")
