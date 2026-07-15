"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.9}),
        ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.3}),
        ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.95}),
        ("Conflicting Mood", {"genre": "pop", "mood": "sad", "energy": 0.9}),
    ]

    for name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\n{name}:\n")
        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{index}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Why: {explanation}")
            print()


if __name__ == "__main__":
    main()
