import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file_path = askopenfilename(title="Select your Excel file", filetypes=[("Excel files", "*.xlsx *.xls")])
if not file_path:
    print("No file selected. Exiting...")
    exit()

data = pd.read_excel(file_path)
print(data.head())

target_column = input("\nEnter the target column name for regression (or leave blank for unsupervised): ")
if target_column == "":
    target_column = None

if target_column and target_column in data.columns:
    X = data.drop(columns=[target_column])
    y = data[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("R^2 Score:", r2)

else:
    X = data.select_dtypes(include='number')
    n_clusters = int(input("Enter number of clusters (e.g., 3): "))
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)
    data['Cluster'] = kmeans.labels_
    print(data[['Cluster']].head(20))