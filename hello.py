# 1. Load the dataset
from preswald import connect, get_df
connect()
df = get_df("FIFA_21")

# 2. Query or manipulate the data
from preswald import query
# top 10 players
sql = "SELECT name, age, hits, team FROM FIFA_21 ORDER BY CAST(hits AS INTEGER) DESC LIMIT 10"
top_10 = query(sql, "FIFA_21")

# 3. Build an interactive UI
from preswald import table, text
text("# Top 10 FIFA 2021 Players")
table(top_10, title="Top 10 FIFA 2021 Players")

# 4. Create a visualization
from preswald import plotly
import plotly.express as px
fig = px.scatter(
    top_10,
    x="age",
    y="hits",
    hover_name="name"
)
plotly(fig)