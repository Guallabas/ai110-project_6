import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Recommend the top-k songs for a user profile."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dicts = [
            {
                "id": song.id,
                "title": song.title,
                "artist": song.artist,
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "tempo_bpm": song.tempo_bpm,
                "valence": song.valence,
                "danceability": song.danceability,
                "acousticness": song.acousticness,
            }
            for song in self.songs
        ]
        ranked = recommend_songs(user_prefs, song_dicts, k=k)
        return [self._song_from_dict(song_dict) for song_dict, _, _ in ranked]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song was recommended for a user profile."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dict = {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "tempo_bpm": song.tempo_bpm,
            "valence": song.valence,
            "danceability": song.danceability,
            "acousticness": song.acousticness,
        }
        _, reasons = score_song(user_prefs, song_dict)
        return "; ".join(reasons)

    def _song_from_dict(self, song_dict: Dict) -> Song:
        return Song(
            id=song_dict["id"],
            title=song_dict["title"],
            artist=song_dict["artist"],
            genre=song_dict["genre"],
            mood=song_dict["mood"],
            energy=song_dict["energy"],
            tempo_bpm=song_dict["tempo_bpm"],
            valence=song_dict["valence"],
            danceability=song_dict["danceability"],
            acousticness=song_dict["acousticness"],
        )

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        songs = []
        for row in reader:
            row = dict(row)
            for key in ["energy", "tempo_bpm", "valence", "danceability", "acousticness"]:
                row[key] = float(row[key])
            row["id"] = int(row["id"])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a single song against a user preference profile."""
    genre_key = "genre" if "genre" in user_prefs else "favorite_genre"
    mood_key = "mood" if "mood" in user_prefs else "favorite_mood"
    energy_key = "energy" if "energy" in user_prefs else "target_energy"

    preferred_genre = user_prefs.get(genre_key, "")
    preferred_mood = user_prefs.get(mood_key, "")
    target_energy = float(user_prefs.get(energy_key, 0.0))

    score = 0.0
    reasons: List[str] = []

    if song.get("genre") == preferred_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")
    else:
        reasons.append("genre mismatch")

    if song.get("mood") == preferred_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")
    else:
        reasons.append("mood mismatch")

    song_energy = float(song.get("energy", 0.0))
    energy_gap = abs(song_energy - target_energy)
    energy_score = max(0.0, 1.0 - energy_gap)
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic", False)
    acousticness = float(song.get("acousticness", 0.0))
    if likes_acoustic and acousticness > 0.6:
        score += 0.25
        reasons.append("acoustic preference (+0.25)")
    elif not likes_acoustic and acousticness > 0.7:
        score -= 0.2
        reasons.append("acoustic penalty (-0.20)")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score and rank songs to produce the top-k recommendations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked[:k]
