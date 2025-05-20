# capital-one-airline-challenge
Cap One Data Challenge 2025

### What it does:
1. **Extracts data** from `data.zip` if needed.
2. **Reads large datasets in chunks** to handle memory constraints.
3. **Cleans and processes the data** by:
   - Normalizing column names.
   - Converting data types.
   - Handling missing values.
   - Filtering out canceled flights.
4. **Performs key analyses**, including:
   - Identifying the **10 busiest round-trip routes**.
   - Finding the **10 most profitable routes**.
   - Calculating the **break-even point** for aircraft investments.
5. **Visualizes insights with Dash (Plotly)**, including:
   - Busiest routes:
     ![busiest_routes](airline_app/images/busiest_routes.png)
   - Profitability analysis.
     ![profitable_routes](airline_app/images/profitable_routes.png)
   - Break-even analysis.

### Thoughts during the challenge:
1. I'm gonna build this with **Python, Poetry, and Dash (Plotly)**.
2. Gonna use the magic of 4o. Who the heck writes code anymore, am I right?
3. Have to read **Flights.csv in chunks**, cos it's too large.
4. Ideally, you'd do this with **Spark SQL or Snowflake SQL**, but we're handling it with Pandas for now.
5. Fixed **chained assignment warnings** in Pandas by using `.loc[]` and `.assign()`.
6. Implemented **error handling** for missing or malformed data.

### TODOs:
1. Write test cases.
2. Understand why the break-even analysis is empty.

### How to Run:
```sh
poetry install
poetry run airline_app