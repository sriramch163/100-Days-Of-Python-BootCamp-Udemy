# Day 46 - Spotify Playlist from Billboard Hot 100 🎵

## Project Overview
Advanced web scraping application that creates Spotify playlists from Billboard Hot 100 charts for any given date. Combines web scraping with Spotify API integration for automated playlist creation.

## What I Learned
- **Advanced Web Scraping**: Using CSS selectors and custom headers for complex websites
- **Spotify API Integration**: OAuth2 authentication and playlist management
- **API Authentication**: Managing OAuth2 flow with Spotipy library
- **Data Processing**: Handling missing data and API search results
- **Error Handling**: Try-except blocks for robust API interactions
- **User Input Validation**: Date format handling and processing
- **Multi-API Integration**: Combining web scraping with REST API calls

## Key Features
- **Billboard Chart Scraping**: Extracts Hot 100 songs from any historical date
- **Spotify Authentication**: OAuth2 flow for secure API access
- **Song Search**: Intelligent song matching with year filtering
- **Playlist Creation**: Automated private playlist generation
- **Error Handling**: Graceful handling of songs not found on Spotify
- **User Interaction**: Date input for time travel functionality

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up Spotify Developer Account:
   - Create app at https://developer.spotify.com/dashboard
   - Get Client ID and Client Secret
   - Set redirect URI to `http://example.com`
3. Update credentials in `main.py`:
   ```python
   client_id="your_spotify_client_id"
   client_secret="your_spotify_client_secret"
   ```
4. Run the application:
   ```bash
   python main.py
   ```
5. Enter date in YYYY-MM-DD format when prompted
6. Complete OAuth authentication in browser

## Files & Directory Structure
```
Day - 46/
├── main.py
├── requirements.txt
├── token.txt (generated)
└── README.md
```

## Technical Implementation

### 1. Web Scraping with Headers
```python
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url=billboard_url, headers=header)
```

### 2. CSS Selector Usage
```python
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
```

### 3. Spotify OAuth2 Authentication
```python
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR_CLIENT_ID,
        client_secret=YOUR_CLIENT_SECRET
    )
)
```

### 4. Song Search with Error Handling
```python
try:
    uri = result["tracks"]["items"][0]["uri"]
    song_uris.append(uri)
except IndexError:
    print(f"{song} doesn't exist in Spotify. Skipped.")
```

## APIs and Libraries Used
- **Beautiful Soup**: HTML parsing and CSS selector support
- **Requests**: HTTP requests with custom headers
- **Spotipy**: Spotify Web API Python library
- **Spotify Web API**: Playlist creation and song search

## Authentication Flow
1. **OAuth2 Setup**: Configure Spotify app credentials
2. **Authorization**: User grants permission via browser
3. **Token Management**: Automatic token refresh and caching
4. **API Access**: Authenticated requests to Spotify endpoints

## Data Processing Pipeline
1. **User Input**: Date selection for Billboard chart
2. **Web Scraping**: Extract song titles from Billboard
3. **Data Cleaning**: Strip whitespace and format song names
4. **Spotify Search**: Find matching tracks with year filtering
5. **URI Collection**: Gather Spotify track URIs
6. **Playlist Creation**: Create private playlist with collected songs

## Error Handling Strategies
- **Missing Songs**: Skip songs not found on Spotify
- **API Rate Limits**: Built-in handling via Spotipy
- **Authentication Errors**: OAuth2 error management
- **Network Issues**: Request timeout and retry logic

## Practical Applications
- Music discovery and nostalgia
- Historical music analysis
- Automated playlist curation
- Data integration between platforms
- Music recommendation systems

---
*Day 46 of 100 Days of Python Challenge - Advanced API Integration*