Real-time music recommendation
🎶 In this project, I'm creating a platform that's similar to Spotify but with some unique twists and features. Let me walk you through what I've been working on:

Phase #1: Getting the Music Data Ready 
The Dataset

First things first, I needed some music to work with. I found this amazing dataset called the Free Music Archive (FMA), which has over 100,000 tracks covering a wide range of genres. It's a hefty dataset, around 93 GiB when compressed, but it's perfect for what I need.
What I Did

Using Python magic, I set up an Extract, Transform, Load (ETL) pipeline to handle this massive amount of data. I extracted features like Mel-Frequency Cepstral Coefficients (MFCC) from the audio files, transformed them into numerical data, and then loaded everything into MongoDB for easy access later on.

Phase #2: Building the Music Recommendation Model 

Getting Smart with the Data

Now that I had all this music data nicely stored away, it was time to get smart with it. I used Apache Spark to train a recommendation model. Think of it like the brain behind suggesting what song you might like next based on what you're currently listening to.
Making It Work

I played around with different strategies to make my recommendations as accurate as possible. Then, I evaluated the model using various metrics to make sure it was doing its job well.
Phase #3: Making It User-Friendly
Bringing It All Together

Here's where the magic happens! I built a web application that lets you stream music, just like Spotify. But what sets it apart is the real-time suggestions. Using Apache Kafka, I'm able to give you recommendations on the fly, based on your listening habits. 
How It Works

You won't find any boring forms here asking you to upload audio files. Nope! Instead, the app tracks what you're listening to and tailors suggestions specifically for you. It's like having your own personal DJ!
