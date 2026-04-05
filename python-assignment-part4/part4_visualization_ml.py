#Task 1 — Data Exploration with Pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"e:\YASH\Certificate Course\Assignment3\python-assignment-part4\students.csv")
print(df.head())

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nData types:")
print(df.dtypes)

print("\nSummary statistics:")
print(df.describe())

print("\nPassed/Failed count:")
print(df["passed"].value_counts())

subject_cols = ["math", "science", "english", "history", "pe"]

print("\nAverage scores for passing students:")
print(df[df["passed"] == 1][subject_cols].mean())

print("\nAverage scores for failing students:")
print(df[df["passed"] == 0][subject_cols].mean())

df["overall_average"] = df[subject_cols].mean(axis=1)

top_student = df.loc[df["overall_average"].idxmax()]

print("\nStudent with highest overall average:")
print(top_student[["name", "overall_average"]])

#Task 2 — Data Visualization with Matplotlib

subject_cols = ['math', 'science', 'english', 'history', 'pe']
df['avg_score'] = df[subject_cols].mean(axis=1)

avg_subject_scores = df[subject_cols].mean()

plt.figure(figsize=(8, 5))
plt.bar(avg_subject_scores.index, avg_subject_scores.values, label='Average Score')
plt.title("Average Score per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.legend()
plt.tight_layout()
plt.savefig("plot1_bar.png")
plt.show()

math_mean = df['math'].mean()

plt.figure(figsize=(8, 5))
plt.hist(df['math'], bins=5, label='Math Scores')
plt.axvline(math_mean, linestyle='--', label=f'Mean = {math_mean:.2f}')
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("plot2_histogram.png")
plt.show()

pass_students = df[df['passed'] == 1]
fail_students = df[df['passed'] == 0]

plt.figure(figsize=(8, 5))
plt.scatter(pass_students['study_hours_per_day'], pass_students['avg_score'], label='Pass')
plt.scatter(fail_students['study_hours_per_day'], fail_students['avg_score'], label='Fail')
plt.title("Study Hours per Day vs Average Score")
plt.xlabel("Study Hours per Day")
plt.ylabel("Average Score")
plt.legend()
plt.tight_layout()
plt.savefig("plot3_scatter.png")
plt.show()

pass_attendance = df[df['passed'] == 1]['attendance_pct'].tolist()
fail_attendance = df[df['passed'] == 0]['attendance_pct'].tolist()

plt.figure(figsize=(8, 5))
plt.boxplot([pass_attendance, fail_attendance], tick_labels=['Pass', 'Fail'])
plt.title("Attendance Percentage: Pass vs Fail")
plt.xlabel("Result")
plt.ylabel("Attendance Percentage")
plt.tight_layout()
plt.savefig("plot4_boxplot.png")
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df['name'], df['math'], marker='o', linestyle='-', label='Math')
plt.plot(df['name'], df['science'], marker='s', linestyle='--', label='Science')
plt.title("Math and Science Scores by Student")
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("plot5_line.png")
plt.show()

#Task 3 — Data Visualization with Seaborn

subject_cols = ['math', 'science', 'english', 'history', 'pe']
df['avg_score'] = df[subject_cols].mean(axis=1)

df['result'] = df['passed'].map({1: 'Pass', 0: 'Fail'})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(data=df, x='result', y='math', ax=ax1)
ax1.set_title('Average Math Score by Result')
ax1.set_xlabel('Result')
ax1.set_ylabel('Average Math Score')

sns.barplot(data=df, x='result', y='science', ax=ax2)
ax2.set_title('Average Science Score by Result')
ax2.set_xlabel('Result')
ax2.set_ylabel('Average Science Score')

plt.tight_layout()
plt.savefig("plot6_seaborn_bar.png")
plt.show()

plt.figure(figsize=(8, 5))

sns.scatterplot(data=df, x='attendance_pct', y='avg_score', hue='result')

sns.regplot(
    data=df[df['passed'] == 1],
    x='attendance_pct',
    y='avg_score',
    scatter=False,
    label='Pass Trend'
)

sns.regplot(
    data=df[df['passed'] == 0],
    x='attendance_pct',
    y='avg_score',
    scatter=False,
    label='Fail Trend'
)

plt.title('Attendance Percentage vs Average Score')
plt.xlabel('Attendance Percentage')
plt.ylabel('Average Score')
plt.legend()
plt.tight_layout()
plt.savefig("plot7_seaborn_scatter.png")
plt.show()


#Task 4 — Machine Learning with scikit-learn

feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']

X = df[feature_cols]
y = df['passed']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

train_accuracy = model.score(X_train_scaled, y_train)
print("Training Accuracy:", train_accuracy)

y_pred = model.predict(X_test_scaled)
test_accuracy = accuracy_score(y_test, y_pred)

print("\nTest Accuracy:", test_accuracy)

print("\nPredictions on Test Set:")
test_names = df.loc[X_test.index, 'name']

for name, actual, predicted in zip(test_names, y_test, y_pred):
    status = "✅ correct" if actual == predicted else "❌ wrong"
    actual_label = "Pass" if actual == 1 else "Fail"
    predicted_label = "Pass" if predicted == 1 else "Fail"
    print(f"{name}: Actual = {actual_label}, Predicted = {predicted_label} -> {status}")

coefficients = model.coef_[0]

coef_df = pd.DataFrame({
    'Feature': feature_cols,
    'Coefficient': coefficients
})

coef_df['Abs_Coefficient'] = coef_df['Coefficient'].abs()
coef_df = coef_df.sort_values(by='Abs_Coefficient', ascending=False)

print("\nFeature Coefficients (sorted by absolute value):")
for _, row in coef_df.iterrows():
    direction = "Pass" if row['Coefficient'] > 0 else "Fail"
    print(f"{row['Feature']}: {row['Coefficient']:.4f} ({direction})")

colors = ['green' if coef > 0 else 'red' for coef in coef_df['Coefficient']]

plt.figure(figsize=(10, 6))
plt.barh(coef_df['Feature'], coef_df['Coefficient'], color=colors)
plt.title("Logistic Regression Feature Coefficients")
plt.xlabel("Coefficient Value")
plt.ylabel("Features")
plt.tight_layout()
plt.savefig("plot8_feature_coefficients.png")
plt.show()

new_student = pd.DataFrame(
    [[75, 70, 68, 65, 80, 82, 3.2]],
    columns=feature_cols
)

new_student_scaled = scaler.transform(new_student)
new_prediction = model.predict(new_student_scaled)[0]
new_probabilities = model.predict_proba(new_student_scaled)[0]

predicted_label = "Pass" if new_prediction == 1 else "Fail"
print("\nNew Student Prediction:", predicted_label)
print(f"Probability of Fail: {new_probabilities[0]:.4f}")
print(f"Probability of Pass: {new_probabilities[1]:.4f}")