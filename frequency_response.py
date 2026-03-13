import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Data
freq = [20, 25, 31, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500,
        630, 800, 1000, 1200, 1600, 2000, 2500, 3100, 4000, 5000, 6300, 8000,
        10000, 12000, 16000, 20000]

db = [34, 32, 30, 26, 21, 18, 16, 14, 13, 11.5, 10.5, 10.0, 9.0, 8.0, 7.75,
      7.5, 7.5, 7.0, 6.7, 6.4, 6.0, 5.5, 5.0, 4.5, 4.0, 3.25, 2.5, 2.0,
      1.25, 0.5, 0]

fig, ax = plt.subplots(figsize=(14, 7))

# Plot line
ax.semilogx(freq, db, color='#2196F3', linewidth=2.5, marker='o', markersize=4,
            markerfacecolor='#1565C0', markeredgecolor='#1565C0')

# Fill under curve
ax.fill_between(freq, db, alpha=0.12, color='#2196F3')

# Axis config
ax.set_xscale('log')
ax.set_xlim(20, 20000)
ax.set_ylim(-2, 38)
ax.set_xlabel('Частота, Гц', fontsize=13, fontweight='bold')
ax.set_ylabel('Уровень, дБ', fontsize=13, fontweight='bold')
ax.set_title('Частотная характеристика (АЧХ)', fontsize=16, fontweight='bold', pad=15)

# X ticks
major_ticks = [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
ax.set_xticks(major_ticks)
ax.set_xticklabels([f'{f:,}'.replace(',', ' ') if f >= 1000 else str(f) for f in major_ticks])
ax.xaxis.set_minor_formatter(ticker.NullFormatter())

# Y ticks
ax.set_yticks(range(0, 36, 2))

# Grid
ax.grid(True, which='major', linestyle='-', alpha=0.3)
ax.grid(True, which='minor', linestyle=':', alpha=0.15)

# Annotate endpoints
ax.annotate('+34 дБ', xy=(20, 34), xytext=(28, 35.5),
            fontsize=10, fontweight='bold', color='#D32F2F',
            arrowprops=dict(arrowstyle='->', color='#D32F2F', lw=1.2))
ax.annotate('0 дБ', xy=(20000, 0), xytext=(13000, 1.8),
            fontsize=10, fontweight='bold', color='#D32F2F',
            arrowprops=dict(arrowstyle='->', color='#D32F2F', lw=1.2))

plt.tight_layout()
plt.savefig('/home/user/shadowrocket/frequency_response.png', dpi=150, bbox_inches='tight')
print('Saved: frequency_response.png')
