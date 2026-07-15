# 🎵 Music Recommender Simulation

## Project Summary

This project builds a small music recommender simulation that mirrors the basic idea behind real streaming platforms: songs are described by features such as genre, mood, and energy, while a user profile captures taste preferences. The recommender scores songs based on how closely they match the user’s preferred style and returns the best matches first.

---

## How The System Works

This recommender uses a simple content-based approach. Each song is represented by attributes such as genre, mood, energy, tempo, valence, danceability, and acousticness, while each user profile stores a preferred genre, preferred mood, a target energy level, and whether the user likes acoustic music. The recommender gives higher scores to songs that match the user’s genre and mood most closely, and it also rewards songs whose energy level is near the user’s target. After scoring all songs, the system ranks them and recommends the top matches.

### Sample user profile

A sample taste profile for the simulation is:

- favorite_genre: pop
- favorite_mood: happy
- target_energy: 0.75
- likes_acoustic: false

This profile is intended to distinguish between upbeat, bright songs and more relaxed or intense ones. It is broad enough to prefer pop and indie pop while still allowing the system to separate cheerful songs from darker or calmer tracks.

### Features used

- `Song`: genre, mood, energy, tempo_bpm, valence, danceability, acousticness
- `UserProfile`: favorite_genre, favorite_mood, target_energy, likes_acoustic

### Recommendation logic

The scoring recipe for a single song is:

1. Add 2.0 points if the song genre matches the user’s favorite genre.
2. Add 1.0 point if the song mood matches the user’s favorite mood.
3. Add a similarity bonus based on how close the song energy is to the target energy. For example, a song with energy 0.75 receives the highest bonus when it is exactly at the target, while songs farther away receive smaller bonuses.
4. Add a small bonus for additional features such as acousticness when the user prefers non-acoustic music.
5. Rank all scored songs from highest to lowest and return the top recommendations.

This recipe gives the strongest weight to genre, then mood, and uses energy as a softer but important signal for matching the user’s overall vibe.

### Data flow sketch

User preferences → loop through each song in the CSV → score the song using the recipe above → rank all songs → return the top recommendations.

A simple flow is:

Input (user prefs) → Process (score every song) → Output (ranked top recommendations)

### Biases and limitations

This system is intentionally simple, so it may over-prioritize genre and mood while underusing other musical signals. It could also miss songs that are genuinely good matches but do not fit the user’s exact preferred genre or energy range. In a real recommender, these limitations would be reduced by using larger datasets and more detailed user behavior signals.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Example terminal output for the default pop/happy profile:

```text
Loaded songs: 16

Top recommendations:

1. Sunrise City by Neon Echo
   Score: 3.98
   Why: genre match (+2.0); mood match (+1.0); energy similarity (+0.98)

2. Gym Hero by Max Pulse
   Score: 2.87
   Why: genre match (+2.0); mood mismatch; energy similarity (+0.87)

3. Rooftop Lights by Indigo Parade
   Score: 1.96
   Why: genre mismatch; mood match (+1.0); energy similarity (+0.96)
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



