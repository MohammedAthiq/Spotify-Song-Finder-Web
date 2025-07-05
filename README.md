

# 🎶 Spotipy Lyrics Finder

A simple Flask web app that finds a song based on its lyrics using the Spotify API.

---

## 🚀 Features

- Input partial song lyrics
- Searches for the best matching song
- Displays:
  - 🎵 Song name
  - 🎤 Artist
  - 🔗 Spotify link

---

## 🛠️ Tech Stack

- Python
- Flask
- Requests
- Spotipy(lyrics-based search)
- HTML (Jinja2 templating)

---

## 🧪 Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/MohammedAthiq/Spotify-Song-Finder-Web.git
cd Spotify-Song-Finder-Web
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file and add your API keys:

```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
```

### 5. Run the app

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📂 Project Structure

```
spotipy-web/
├── app.py
├── spotify_a.py
├── templates/
│   └── index.html
├── .env              # (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧾 License

This project is open source and available under the [MIT License](LICENSE).

---

## 💡 Future Improvements

- Deploy to Render / Vercel / Railway
- Add YouTube preview or search link (optional)