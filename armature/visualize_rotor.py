import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as mpatches

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_aspect('equal')
ax.set_xlim(-1300, 1300)
ax.set_ylim(-1300, 1300)
ax.grid(True, alpha=0.3)
ax.set_title("🌍 EARTH'S INNER CORE: CRYSTAL ALIGNMENT MAP", fontsize=16, fontweight='bold', pad=20)

# Draw the inner core boundaries
outer_radius = 1221  # km
inner_inner_radius = 650  # km

# Outer inner core (1221 km radius)
outer_core = Circle((0, 0), outer_radius, fill=False, 
                   edgecolor='darkred', linewidth=2, linestyle='--')
ax.add_patch(outer_core)

# Inner inner core (650 km radius)
inner_core = Circle((0, 0), inner_inner_radius, fill=False, 
                   edgecolor='gold', linewidth=3)
ax.add_patch(inner_core)

# Label the regions
ax.text(0, 0, 'INNER INNER CORE\n(650 km radius)\nStrong E-W alignment', 
        ha='center', va='center', fontsize=10, color='gold', fontweight='bold')
ax.text(900, 0, 'OUTER INNER CORE\n(1221 km total radius)\nWeaker N-S alignment', 
        ha='center', va='center', fontsize=9, color='darkred', fontweight='bold')

# Draw coordinate axes
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
ax.axvline(x=0, color='gray', linestyle='-', alpha=0.5)
ax.text(1250, 0, 'E', fontsize=12, fontweight='bold', va='center')
ax.text(-1250, 0, 'W', fontsize=12, fontweight='bold', va='center')
ax.text(0, 1250, 'N', fontsize=12, fontweight='bold', ha='center')
ax.text(0, -1250, 'S', fontsize=12, fontweight='bold', ha='center')

# Draw seismic wave paths through different directions
def draw_wave_path(start_angle, color, label):
    """Draw a seismic wave path through the core"""
    start_x = 1300 * np.cos(np.radians(start_angle))
    start_y = 1300 * np.sin(np.radians(start_angle))
    end_x = -start_x
    end_y = -start_y
    
    # Draw the path
    ax.plot([start_x, end_x], [start_y, end_y], 
            color=color, alpha=0.6, linewidth=2, label=label)
    
    # Add speed indicators (exaggerated for visualization)
    mid_x = (start_x + end_x) / 4
    mid_y = (start_y + end_y) / 4
    
    # Determine if path is more E-W or N-S
    angle = start_angle % 180
    if angle < 45 or angle > 135:  # More N-S
        speed = "≈10.2 km/s"
        ax.text(mid_x, mid_y, speed, fontsize=8, color=color, 
                ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", 
                facecolor='white', alpha=0.8))
    else:  # More E-W
        speed = "≈11.1 km/s"
        ax.text(mid_x, mid_y, speed, fontsize=8, color=color, 
                ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", 
                facecolor='white', alpha=0.8))

# Draw example wave paths
draw_wave_path(0, 'blue', 'E-W path (fast)')      # East-West
draw_wave_path(90, 'green', 'N-S path (slow)')    # North-South
draw_wave_path(45, 'purple', 'NE-SW path')       # Diagonal

# Draw crystal alignment patterns
# Inner inner core: Strong E-W alignment (horizontal lines)
for y in np.linspace(-inner_inner_radius, inner_inner_radius, 15):
    if abs(y) < inner_inner_radius:
        x_range = np.sqrt(inner_inner_radius**2 - y**2)
        ax.plot([-x_range, x_range], [y, y], 
                color='gold', alpha=0.7, linewidth=1.5)

# Outer inner core: Weaker N-S alignment (vertical lines)
for x in np.linspace(-outer_radius, outer_radius, 20):
    if inner_inner_radius < abs(x) < outer_radius:
        y_range = np.sqrt(outer_radius**2 - x**2)
        ax.plot([x, x], [-y_range, y_range], 
                color='darkred', alpha=0.4, linewidth=1)

# Add legend and annotations
legend_elements = [
    mpatches.Patch(color='gold', label='Inner Inner Core (Strong E-W alignment)'),
    mpatches.Patch(color='darkred', label='Outer Inner Core (Weaker N-S alignment)'),
    plt.Line2D([0], [0], color='blue', label='E-W Seismic Path (fast)'),
    plt.Line2D([0], [0], color='green', label='N-S Seismic Path (slow)'),
    plt.Line2D([0], [0], color='purple', label='Diagonal Path')
]

ax.legend(handles=legend_elements, loc='upper left', fontsize=9)

# Add explanatory text
explanation = """CRYSTAL ALIGNMENT MAP:
• Lines show iron crystal orientation (like wood grain)
• E-W aligned crystals in inner inner core: Waves travel ~3% faster east-west
• N-S aligned crystals in outer inner core: Waves travel slower north-south
• Seismic waves measure these speed differences to map the structure

DATA SOURCE: Seismic anisotropy studies (Ishii & Dziewonski 2002, 
Sun & Song 2008, Waszek et al. 2011)"""
ax.text(-1280, -1100, explanation, fontsize=8, 
        bbox=dict(boxstyle="round,pad=1", facecolor='lightyellow', alpha=0.9))

plt.tight_layout()
plt.show()
