# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender is designed for classroom use and simple music discovery experiments. It suggests songs that match a user’s preferred genre, mood, and energy level. It assumes that a user can be described by a few simple preferences rather than by a complex history of listening behavior.

---

## 3. How the Model Works  

The recommender looks at each song and compares it to a user’s taste profile. It gives the strongest points for matching genre, then adds points for matching mood and for having energy close to the target level. It also uses acousticness as a smaller signal, especially when the user prefers less acoustic music. The system then ranks all songs and returns the best matches.

---

## 4. Data  

The model uses a small catalog of 16 songs. The dataset includes features like genre, mood, energy, tempo, valence, danceability, and acousticness. I expanded the original starter file with more songs so the system could be tested with a wider range of styles. Even so, the catalog is still small and does not cover every genre or every kind of listener preference.

---

## 5. Strengths  

The system works well for simple, clear profiles. It gives sensible results for users who want a specific genre, mood, or energy level. It also makes it easy to see why a song was ranked highly, because the output explains the reason for the score.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The current system can over-prioritize genre and mood, which creates a filter-bubble effect for users with more unusual or conflicting tastes. In the experiments, a profile that mixed pop with a sad mood still received strong pop-heavy recommendations, showing that the scoring can be too rigid. The dataset is also small, so a few songs with similar energy or genre values can dominate the top results and make the system feel less diverse. This means the recommender works best as a simple classroom example rather than a fully realistic music discovery tool.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested several user profiles, including a high-energy pop profile, a chill lofi profile, a deep intense rock profile, and a conflicting profile that mixed pop with a sad mood. The high-energy pop profile strongly favored upbeat songs like Sunrise City and Gym Hero, which makes sense because both the genre and energy matched the request. The chill lofi profile shifted toward calmer songs such as Library Rain and Midnight Coding, showing that the system can pick up lower-energy preferences when the mood and genre align.

The deep intense rock profile mostly preferred Storm Runner, which also makes sense because the genre and mood were both a good match. The conflicting profile was more interesting: even though the mood was sad, the system still kept surfacing pop-style tracks because the genre match was still strong. That is a good example of how the current logic can over-emphasize one feature and make the output feel less intuitive.

I also ran a small experiment by increasing the importance of energy and reducing the genre bonus. This made the output change noticeably, especially for the high-energy and chill profiles, because songs with closer energy values rose in the rankings. The change made the system feel more sensitive to intensity, but it also showed that the current catalog is still small enough that a few high-energy songs can dominate the list.

---

## 8. Future Work  

I would improve this model by adding more songs and more detailed user behavior data. I would also like to test more features, such as tempo and valence, and make the explanations more natural and easier to understand. Another next step would be to reduce over-reliance on genre so the system can support more varied tastes.

---

## 9. Personal Reflection  

This project helped me understand that even a simple recommender can feel surprisingly convincing when it uses a few clear signals. My biggest learning moment was seeing how much genre and mood can dominate the results, even when a user’s other preferences are different. I also learned that AI tools were very helpful for turning ideas into working code quickly, but I still had to check the results carefully because simple rules can produce unexpected or overly rigid recommendations. If I extended this project, I would try a larger dataset and more nuanced scoring so the system could feel more like a real music app.
