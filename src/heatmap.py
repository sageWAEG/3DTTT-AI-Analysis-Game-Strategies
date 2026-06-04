import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

# Read CSV data
df = pd.read_csv("opening_moves5.csv")

# Calculate win rate
df["win_rate"] = df["wins"] / df["total_games"]

# Create a figure with subplots for each board
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot heatmaps for all 3 boards
for board in range(3):
    # Filter data for the current board
    board_data = df[df["board"] == board]
    
    # Pivot to create a 3x3 grid for rows and columns
    heatmap_data = board_data.pivot_table(
        index="row", 
        columns="column", 
        values="win_rate", 
        fill_value=0  # Handle missing combinations
    )
    
    # Plot heatmap
    sns.heatmap(
        heatmap_data, 
        annot=True, 
        cmap="YlGnBu", 
        vmin=0, 
        vmax=1,  # Fix color scale between 0% and 100%
        ax=axes[board]
    )
    axes[board].set_title(f"Board {board} Win Rate Heatmap")
    axes[board].set_xlabel("Column")
    axes[board].set_ylabel("Row")

plt.tight_layout()
plt.savefig("heatmap5.png")