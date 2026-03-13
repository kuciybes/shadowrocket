import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Curve 1 data
freq1 = [20, 25, 31, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500,
         630, 800, 1000, 1200, 1600, 2000, 2500, 3100, 4000, 5000, 6300, 8000,
         10000, 12000, 16000, 20000]

db1 = [34, 32, 30, 26, 21, 18, 16, 14, 13, 11.5, 10.5, 10.0, 9.0, 8.0, 7.75,
       7.5, 7.5, 7.0, 6.7, 6.4, 6.0, 5.5, 5.0, 4.5, 4.0, 3.25, 2.5, 2.0,
       1.25, 0.5, 0]

# Curve 2 — Audiofrog Target Curve (normalized to 1 kHz = 0 dB)
freq2 = [20, 25, 32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 320, 400, 500,
         640, 800, 1000, 1280, 1600, 2000, 2560, 3200, 4000, 5120, 6400, 8000,
         10240, 12900, 16250, 20480]

db2 = [10.2, 9.3, 9.4, 9.0, 8.2, 6.7, 4.8, 3.1, 1.6, 0.8, 0.6, 0.3, -0.1,
       0.4, 0.2, -0.2, 0.0, 0.0, -0.3, -0.2, 0.0, -0.7, -0.6, -0.8, -1.2,
       -1.5, -2.2, -3.4, -4.6, -5.7, -5.9]

fig, ax = plt.subplots(figsize=(14, 7))

# Plot curve 1
ax.semilogx(freq1, db1, color='#2196F3', linewidth=2.5, marker='o', markersize=4,
            markerfacecolor='#1565C0', markeredgecolor='#1565C0',
            label='Кривая 1 (исходная)')

# Plot curve 2
ax.semilogx(freq2, db2, color='#E65100', linewidth=2.5, marker='s', markersize=4,
            markerfacecolor='#BF360C', markeredgecolor='#BF360C',
            label='Audiofrog Target Curve')

# Fill under curves
ax.fill_between(freq1, db1, alpha=0.10, color='#2196F3')
ax.fill_between(freq2, db2, alpha=0.10, color='#E65100')

# Axis config
ax.set_xscale('log')
ax.set_xlim(20, 21000)
ax.set_ylim(-8, 38)
ax.set_xlabel('Частота, Гц', fontsize=13, fontweight='bold')
ax.set_ylabel('Уровень, дБ', fontsize=13, fontweight='bold')
ax.set_title('Частотная характеристика (АЧХ)', fontsize=16, fontweight='bold', pad=15)

# X ticks
major_ticks = [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
ax.set_xticks(major_ticks)
ax.set_xticklabels([f'{f:,}'.replace(',', ' ') if f >= 1000 else str(f) for f in major_ticks])
ax.xaxis.set_minor_formatter(ticker.NullFormatter())

# Y ticks
ax.set_yticks(range(-8, 38, 2))

# Grid
ax.grid(True, which='major', linestyle='-', alpha=0.3)
ax.grid(True, which='minor', linestyle=':', alpha=0.15)

# Zero line
ax.axhline(y=0, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)

# Legend
ax.legend(fontsize=12, loc='upper right', framealpha=0.9)

plt.tight_layout()
plt.savefig('/home/user/shadowrocket/frequency_response.png', dpi=150, bbox_inches='tight')
print('Saved: frequency_response.png')
