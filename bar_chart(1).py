import matplotlib.pyplot as plt
import random

# Create sample data
genders = ['Male', 'Female', 'Other']
gender_data = [random.choice(genders) for _ in range(200)]
ages = [random.randint(18, 65) for _ in range(200)]

# ----- Bar Chart: Gender Distribution -----
gender_counts = {g: gender_data.count(g) for g in genders}

plt.figure(figsize=(6, 4))
plt.bar(gender_counts.keys(), gender_counts.values(), color=['blue', 'pink', 'gray'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ----- Histogram: Age Distribution -----
plt.figure(figsize=(6, 4))
plt.hist(ages, bins=10, color='green', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show() 