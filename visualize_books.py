import requests
import plotly.graph_objects as go

print("Starting visualization script...")

try:
    print("Fetching books from API...")
    response = requests.get('http://127.0.0.1:5000/books')
    print(f"API Response status code: {response.status_code}")
    print(f"API Response content: {response.text}")
    
    books = response.json()['books']
    print(f"Number of books: {len(books)}")
    print(f"Books: {books}")

    print("Counting books per country...")
    country_counts = {}
    for book in books:
        country = book.get('country')
        if country:
            country_counts[country] = country_counts.get(country, 0) + 1
        else:
            print(f"Warning: Book without country: {book}")

    print(f"Country counts: {country_counts}")

    if not country_counts:
        print("No country data available. Exiting.")
        exit(1)

    print("Creating map...")
    fig = go.Figure(data=go.Choropleth(
        locations = list(country_counts.keys()),
        locationmode = 'country names',
        z = list(country_counts.values()),
        text = [f"{country}: {count} book(s)" for country, count in country_counts.items()],
        colorscale = 'Viridis',
        autocolorscale = False,
        reversescale = True,
        marker_line_color = 'darkgray',
        marker_line_width = 0.5,
        colorbar_title = 'Number of Books',
    ))

    fig.update_layout(
        title_text = 'Books Map by Country by Song',
        geo = dict(
            showframe = False,
            showcoastlines = True,
            projection_type = 'equirectangular'
        )
    )

    print("Displaying map...")
    fig.show()
    print("Script completed.")

except Exception as e:
    print(f"An error occurred: {e}")