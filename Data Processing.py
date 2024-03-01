import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
file_path = "C:\\Users\\dhami\\Downloads\\scheme---trends-in-receipts (1).csv"
df = pd.read_csv(file_path)
# Define the data
data = {
    "Scheme Type": ["Core of the Core Schemes"]*10,
    "Scheme Name": ["National Social Assistance Progam", 
                    "Mahatma Gandhi National Rural Employment Guarantee Program", 
                    "Umbrella Scheme for Development of Scheduled Castes",
                    "Umbrella Programme for Development of Scheduled Tribes",
                    "Umbrella Programme for Development of Minorities",
                    "Umbrella Programme for Development of Other Vulnerable Groups",
                    "Pradhan Mantri Awas Yojna (PMAY)",
                    "Jal Jeevan Mission (JJM)/National Rural Drinking Water Mission",
                    "National Health Mission",
                    "National Education Mission"],
    "Actuals 2022-2023": [9651.27, 90805.93, 5157.83, 3825.01, 222.75, 1571.59, 73614.95, 54699.8, 33802.86, 32875.19],
    "Budget Estimates 2023-2024": [9636.32, 60000, 9409.14, 4295.4, 610, 2193.97, 79590.03, 70000, 36785.26, 38953.47],
    "Revised Estimates 2023-2024": [9652, 86000, 6780, 3285.86, 555, 1918, 54103.04, 70000, 33885.74, 33500],
    "Budget Estimates 2024-2025": [9652, 86000, 9559.98, 4241.47, 912.9, 2150, 80670.75, 70162.9, 38183, 37500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate summary statistics
summary_stats = df.describe()

# Data filtering based on specific criteria (e.g., filtering by scheme type)
filtered_data = df[df["Scheme Type"] == "Core of the Core Schemes"]

# Calculate mean, median, and mode for numeric columns
mean_values = df.mean(numeric_only=True)
median_values = df.median(numeric_only=True)
mode_values = df.mode(numeric_only=True)

# Print mean, median, and mode values
print("Mean values:\n", mean_values)
print("\nMedian values:\n", median_values)
print("\nMode values:\n", mode_values)

# Generate data visualizations

# Plot histogram of Actuals 2022-2023
plt.figure(figsize=(10, 6))
plt.hist(df["Actuals 2022-2023"], bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of Actuals 2022-2023")
plt.xlabel("Actuals 2022-2023")
plt.ylabel("Frequency")
plt.grid(True)  
# Add grid lines for better readability
plt.show()

# Bar chart for Budget Estimates

# Set the figure size
plt.figure(figsize=(12, 8))

# Plotting
bar_width = 0.35
index = df.index

plt.bar(index, df["Budget Estimates 2023-2024"], bar_width, label='Budget Estimates 2023-2024', color='skyblue')
plt.bar(index + bar_width, df["Budget Estimates 2024-2025"], bar_width, label='Budget Estimates 2024-2025', color='lightgreen')

# Adding labels and title
plt.xlabel('Scheme Name', fontsize=12)
plt.ylabel('Budget Estimates', fontsize=12)
plt.title('Budget Estimates by Scheme Name', fontsize=14)
plt.xticks(index + bar_width / 2, df["Scheme Name"], rotation=90)
plt.legend()

# Displaying the plot
plt.tight_layout()
plt.show()

# Saving the processed data to new files
summary_stats.to_csv("summary_statistics.csv", index=False)
filtered_data.to_csv("filtered_data.csv", index=False)


