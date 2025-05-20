import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import zipfile
import os

# File paths
DATA_ZIP = os.path.join(os.path.dirname(__file__), "../data/data.zip")
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/")
FLIGHTS_FILE = os.path.join(DATA_DIR, "Flights.csv")
TICKETS_FILE = os.path.join(DATA_DIR, "Tickets.csv")
AIRPORTS_FILE = os.path.join(DATA_DIR, "Airport_Codes.csv")

# Define chunk size
CHUNK_SIZE = 100000

# Function to extract ZIP file if not already extracted
def extract_data():
    if not os.path.exists(FLIGHTS_FILE) or not os.path.exists(TICKETS_FILE) or not os.path.exists(AIRPORTS_FILE):
        if not os.path.exists(DATA_ZIP):
            raise FileNotFoundError(f"Missing data.zip file at {DATA_ZIP}")
        
        with zipfile.ZipFile(DATA_ZIP, "r") as zip_ref:
            for file in zip_ref.namelist():
                if "__MACOSX" not in file:
                    zip_ref.extract(file, DATA_DIR)

# Function to read large CSV files in chunks
def read_large_csv(file_path, chunk_size=CHUNK_SIZE):
    data_chunks = []
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, low_memory=False):
        data_chunks.append(chunk)
    return pd.concat(data_chunks, ignore_index=True)

# Function to load and process data
def load_data():
    extract_data()

    # Read CSVs
    flights_df = read_large_csv(FLIGHTS_FILE)
    tickets_df = read_large_csv(TICKETS_FILE)
    airports_df = pd.read_csv(AIRPORTS_FILE)  # Small dataset

    # Normalize column names
    flights_df.columns = flights_df.columns.str.lower().str.strip()
    tickets_df.columns = tickets_df.columns.str.lower().str.strip()
    airports_df.columns = airports_df.columns.str.lower().str.strip()

    # Convert 'cancelled' to integers
    flights_df['cancelled'] = flights_df['cancelled'].astype(int)

    # Convert 'distance' to numeric, handling errors
    flights_df['distance'] = pd.to_numeric(flights_df['distance'], errors='coerce')

    # Drop rows where 'distance' conversion failed
    flights_df = flights_df.dropna(subset=['distance'])

    # Handle missing values
    flights_df.loc[:, 'dep_delay'] = flights_df['dep_delay'].fillna(0)
    flights_df.loc[:, 'arr_delay'] = flights_df['arr_delay'].fillna(0)

    # Filter out canceled flights
    flights_df = flights_df[flights_df['cancelled'] == 0]

    # Ensure we only use valid airports
    airports_df = airports_df.dropna(subset=['iata_code'])

    # Profit Calculation
    if 'itin_fare' in tickets_df.columns:
        # Convert itin_fare to numeric, handling errors
        tickets_df['itin_fare'] = pd.to_numeric(tickets_df['itin_fare'], errors='coerce')
        tickets_df = tickets_df.dropna(subset=['itin_fare'])

        revenue_per_ticket = tickets_df.groupby(['origin', 'destination'])['itin_fare'].mean().reset_index()
        revenue_per_ticket.rename(columns={'itin_fare': 'avg_ticket_price'}, inplace=True)

        busiest_routes = flights_df.groupby(['origin', 'destination']).size().reset_index(name='num_flights')
        busiest_routes = busiest_routes.sort_values(by='num_flights', ascending=False).head(10)
        busiest_routes = busiest_routes.merge(revenue_per_ticket, on=['origin', 'destination'], how='left')

        # Ensure avg_ticket_price is numeric and fill NaNs with a default value
        busiest_routes['avg_ticket_price'] = busiest_routes['avg_ticket_price'].fillna(busiest_routes['avg_ticket_price'].median())

        # Calculate total revenue and total cost
        busiest_routes['total_revenue'] = busiest_routes['num_flights'] * busiest_routes['avg_ticket_price'] * 200
        avg_distance = flights_df.groupby(['origin', 'destination'])['distance'].mean().reset_index()
        busiest_routes = busiest_routes.merge(avg_distance, on=['origin', 'destination'], how='left')
        busiest_routes['total_cost'] = busiest_routes['num_flights'] * (8 + 1.18) * busiest_routes['distance']

        # Ensure total_cost is valid (no NaN values)
        busiest_routes.loc[:, 'total_cost'] = busiest_routes['total_cost'].fillna(0)

        # Compute profit
        busiest_routes['profit'] = busiest_routes['total_revenue'] - busiest_routes['total_cost']

        # Avoid division by zero or negative profits in break-even calculation
        airplane_cost = 90_000_000
        busiest_routes['break_even_flights'] = airplane_cost / busiest_routes['profit']

        # Replace invalid values with a high number
        busiest_routes.loc[:, 'break_even_flights'] = busiest_routes['break_even_flights'].replace([float('inf'), -float('inf')], 1e6)
        busiest_routes.loc[:, 'break_even_flights'] = busiest_routes['break_even_flights'].fillna(1e6)

        # Convert to integer
        busiest_routes['break_even_flights'] = busiest_routes['break_even_flights'].astype(int)
    else:
        raise KeyError("Column 'itin_fare' not found in Tickets dataset.")

    return busiest_routes

# Function to create Dash app
def create_dash_app(busiest_routes):
    app = dash.Dash(__name__)

    # Visualization (Top 10 Busiest Routes)
    fig_busiest = px.bar(
        busiest_routes, x='origin', y='num_flights', color='destination',
        title='Top 10 Busiest Round-Trip Routes'
    )

    fig_profit = px.bar(
        busiest_routes, x='origin', y='profit', color='destination',
        title='Top 10 Most Profitable Routes'
    )

    fig_break_even = px.bar(
        busiest_routes, x='origin', y='break_even_flights', color='destination',
        title='Break-even Analysis for Recommended Routes'
    )

    # Dash Layout
    app.layout = html.Div([
        html.H1("Airline Data Analysis"),
        dcc.Graph(figure=fig_busiest),
        dcc.Graph(figure=fig_profit),
        dcc.Graph(figure=fig_break_even),
    ])
    
    return app

# Main function to start the app
def main():
    busiest_routes = load_data()
    app = create_dash_app(busiest_routes)
    app.run_server(debug=True)

if __name__ == "__main__":
    main()