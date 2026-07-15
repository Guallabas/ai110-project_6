# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the agent to extend the recommender with a more realistic set of song features and to verify the change end to end. The goal was to make the scoring logic react to richer metadata such as popularity, release decade, detailed mood tags, and instrumentalness while keeping the project simple and testable.

**Prompts used:**

- “Extend the music recommender to use richer song features such as popularity, release decade, mood tags, and instrumentalness.”
- “Add or update tests so the new features are exercised.”
- “Run the tests and the CLI to confirm the recommender still works.”

**What did the agent generate or change?**

- Updated [src/recommender.py](src/recommender.py) to score songs using the new metadata signals.
- Expanded [data/songs.csv](data/songs.csv) to include richer fields and quoted the mood-tag column so it could be parsed safely.
- Added and verified a regression test in [tests/test_recommender.py](tests/test_recommender.py).
- Ran the project with Python to confirm the CLI still emitted ranked recommendations.

**What did you verify or fix manually?**

The first pass surfaced a CSV parsing issue because one of the new mood-tag values contained a comma and was being interpreted as multiple columns. I fixed that by quoting the CSV values and by ensuring only numeric fields were converted to floats during loading. I then verified the result with pytest and by running the CLI.

---

## Step 1 Research Summary

**What task did you give the AI assistant?**

I asked for a summary of how major streaming platforms such as Spotify and YouTube predict what a user will enjoy next, with a focus on the difference between collaborative filtering and content-based filtering.

**Prompts used:**

- “Explain how Spotify or YouTube recommend music to users. Compare collaborative filtering and content-based filtering in simple terms.”
- “What kinds of data do these systems use, such as likes, skips, playlists, tempo, mood, and genre?”

**What did the AI assistant generate or change?**

- It described how real platforms use both explicit signals (likes, saves, playlists) and implicit signals (skips, replays, listening time, completion rate).
- It explained that collaborative filtering recommends songs by finding users with similar behavior patterns, while content-based filtering recommends songs based on their attributes and the user’s past preferences.
- It identified key data types for a music recommender simulation, including:
  - categorical features such as genre and mood
  - numeric features such as energy, tempo, valence, danceability, and acousticness
  - behavioral signals such as likes, skips, playlists, and repeated listens

**What did I verify or fix manually?**

I checked that the summary matches the structure of this project’s starter data in [data/songs.csv](data/songs.csv), which already includes genre, mood, energy, tempo, valence, danceability, and acousticness.

---

## Step 2 Feature Analysis

**What task did you give the AI assistant?**

I asked for help analyzing the available song attributes in [data/songs.csv](data/songs.csv) and identifying which features would be most effective for a simple content-based recommender.

**Prompts used:**

- “Analyze the columns in this songs dataset and suggest which features are most useful for a simple content-based music recommender.”
- “Which features best capture a song’s vibe: genre, mood, energy, valence, tempo, danceability, or acousticness?”

**What did the AI assistant generate or change?**

- It suggested prioritizing categorical features such as genre and mood because they are easy to interpret and strongly influence user taste.
- It recommended using numeric features like energy and valence as secondary signals because they help describe intensity and positivity.
- It noted that tempo, danceability, and acousticness can be useful, but they are less intuitive than genre and mood for a beginner-friendly simulator.

**What did I verify or fix manually?**

I checked the dataset and confirmed that the file already includes the main features needed for a simple recommender: genre, mood, energy, tempo, valence, danceability, and acousticness. For this project, genre and mood are the clearest starting features, while energy and valence help refine the recommendation quality.

---

## Step 3 Algorithm Recipe

**What task did you give the AI assistant?**

I asked for help designing a simple mathematical scoring rule for a content-based music recommender that rewards songs that closely match a user’s preferences.

**Prompts used:**

- “How can I design a scoring rule for a simple recommender that rewards songs that are close to a user’s preferred genre, mood, and energy?”
- “Why do we need both a scoring rule for an individual song and a ranking rule for a list of songs?”
- “Should matching genre be weighted more heavily than matching mood in a small recommender?”

**What did the AI assistant generate or change?**

- It suggested building a score from several small components, such as:
  - genre match bonus
  - mood match bonus
  - energy closeness bonus
  - optional bonus for valence or acousticness
- It recommended using a distance-based approach for numeric features so that a song with energy close to the user’s target earns more points than one that is far away.
- It explained that the scoring rule evaluates one song at a time, while the ranking rule sorts all songs to decide which ones appear first in the recommendation list.

**What did I verify or fix manually?**

I mapped this idea to the starter project structure and decided that the simple version will prioritize genre and mood most strongly, then use energy closeness as a supporting signal. This makes the logic easy to explain and consistent with the project’s starter tests.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
