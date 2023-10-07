import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import datetime

# Title of the web app
st.title("Random Garlic Sales Data")

# Generate random sales data
num_days = 30  # Number of days for the data
dates = [datetime.date(2023, 1, 1) + datetime.timedelta(days=i) for i in range(num_days)]
sales = [random.randint(50, 200) for _ in range(num_days)]
data = pd.DataFrame({'Date': dates, 'Sales': sales})

# Display the data
st.write("## Sales Data")
st.write(data)

# Create a simple line chart
st.write("## Sales Chart")
fig, ax = plt.subplots()
ax.plot(data["Date"], data["Sales"], marker='o')
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Sales")
st.pyplot(fig)

# Display text related to garlic sales
st.write("## Garlic Sales Information")
st.write("Our garlic sales have been steadily increasing over time. Check out the chart above to visualize the sales trends.")
