# How to avoid disappointing shows as GOT Season 8 and find your favored ones?--A Emotional Arc Approach by means of Natural Language Processing 

We all have had such experience as we are watching new movies or shows with high expectations, only to find our expectations subverted after the hours which seem like ages. But by then, those hours in our life had already gone, leaving us with only the disapointment and regrets. 

## A REALLY DISAPPOINTING WATCHING EXPERIENCE(EMPHAZING AND DEFINING)

For years, I have been a big fan of the HBO series, [Game of Thrones](https://en.wikipedia.org/wiki/Game_of_Thrones). Once upon a time, I have even travelled to Ireland to ‘worship’ the show’s shooting scene.

![This is an image](https://github.com/ZeyuCao/Sentiment_Analysis_on_GOT/blob/main/README_Photos/1.png)


![This is an image](https://github.com/ZeyuCao/Sentiment_Analysis_on_GOT/blob/main/README_Photos/2.jpg)

So it wouldn't be hard to imagine the joy and the expectation I had in 2019 when the last season of the show was premiered. 

However, the joy did not last long. it then turned out that the last season was the worst among all the seasons and received a great amount of complaints. Frankly speaking, I would rather haven’t watched the Game of Thrones season 8 so that it would have remained my favorite show ever till now!

I am not the only disappointed fan. A [petition](https://www.change.org/p/hbo-remake-game-of-thrones-season-8-with-competent-writers) was started in the [Change.org](https://www.change.org/p/hbo-remake-game-of-thrones-season-8-with-competent-writers) Wesite, hoping to "Remake Game of Thrones Season 8 with competent writers." Up till now, more than 1.8 million people have signed on the Internet.

![This is an image](https://github.com/ZeyuCao/Sentiment_Analysis_on_GOT/blob/main/README_Photos/Petition.png)

Then a question bumped into my head: how can we avoid disappointing shows such as the last season of Game of Thrones and locate our favoured ones? 

## WE HAVE WAYS TO AVOID DISAPPOINTING SHOWS, BUT...(THE GAP)

Normally, we use the ways below to "filter" our favored shows:

***By watching the trailers***

--The trailer is re-edited, so it can be considered a completely different story from the original one. (BTW, even the last episode of the last season of GOT seems not bad)

***By reviewing the points and the recommendations on websites such as imdb***

--It helps， but most of the time the results are based on machine learning of labels and features on our viewing history on the website. As a result, the recommendations are highly genre-orientated, which is obviously not satisfying because a good story is narrative based rather than genre based. To make matters worse, the ratings are often somehow overated or under-estimated or "just not my type".  

***Through comments***

--I don’t want to take the risk of seeing spoilers. 

Unfortunately, we are faced with the fact that few of the current ways is satisfying. So new approach is supposed to be involved.

## A NARRATIVE APPROACH: THE EMOTIONAL ARC(IDEATATION AND METHODOLOGY)

Is there a new way to tell whether the show or the movie is "interesting" or "breath-taking" or just "dull", before you even watch it? 

It seems impossible at the first glance, as the saying goes: ‘You can’t have your cake and eat it too.’ 

But the digital technology has enabled us to use computational tools to analyse and generate the information we want from the screenplay script.

Think out about the question from very beginning: What is the most significant thing that contributes to the processing of the story?

Enjoying a story, regardless of the format such as reading a book or watching a TV show, is getting various emotional experiences throughout the process, which is so called "The reader-perceived emotional content".

Researchers have found the emotional arc of the given story plays a very important role in the popularity of that story(Reagan et al. EPJ Data Science). Taking Harry Potter as an example, the movie Harry Potter and the Deathly Hallows can be described using the level of happiness.  

![This is an image](https://github.com/ZeyuCao/Sentiment_Analysis_on_GOT/blob/main/README_Photos/harrypotter_emoational_arc.webp)

This approach has inspired me in terms of the methodology. The process of enjoying a movie is getting a unique and certain type of emotional experience, which decomposes into the changing of emotions such as happiness, sadness, anger, hope etc.

So by analysing the changing of each primary emotion of the story, also known as the emotional arc, we can tell what the story would be like before actually watching it. This can be achieved by digital tools and programming languages.

## BEGIN TO 'SWIM' IN THE DIGITAL TOOLS!(PROTOTYPING)
### Web data scraping
I use Python (IDE: Jupyter Notebook) to collect the web data. I download the scripts of GOT from the website below. Firstly, import the packages, set the working directory and scrap the data using beautiful soup and save the text as 'txt' file.

### Data cleaning for word cloud
Remove the inequivalent content, blanks and symbols. Then save the clean files for later use of word cloud. 

### Word Cloud
Word cloud enables the audience to get to know the main characters and the most frequent words of the episode. After importing the packages and setting the directory, I generated the first word cloud and removed the stop words that had been customized by myself. For some cases, the duplicate words shall be merged. 

### Mask
To make the word cloud more visually pleasant, I reshaped it with the selected picture. I chose the icon of house Stark as the mask. I then customized the colour by specifying the colour map, making the style of the word cloud resemble the house icons. Finally, I managed getting the output of the wordcloud. (See in the file ["wordcloud of the first episodes for all season"](https://github.com/ZeyuCao/The_Emotional_Arc_Of_GOT_Scripts/tree/main/wordcloud%20of%20the%20first%20episodes%20for%20all%20season) and ["wordcloud_S1"](https://github.com/ZeyuCao/The_Emotional_Arc_Of_GOT_Scripts/tree/main/wordcloud_S1). 

### Data cleaning for emotional arc
In the data preparation process in Python(IDE: JupyterNotebook), I converted the scripts of the story from 'txt' files to 'csv' files, separating the text by lines.

### Emotional arc: sentiment analysis(NLP)
I used R programming language (IDE: RStudio) to analyse the emotional arc of GOT. I did a Sentiment Analysis from Natural Language Processing to achieve the goal. 

### Data set for emotional arc
I created a new data set("dataset_4") step by step, adding a new column one by one(from "dataset_1" to "dataset_4").

### Emotional arc graphs
I generated the first graph by putting all the sentiments together to see how the density of the sentiments change as the story goes. The dictionary I used was "NRC Word-Emotion Association Lexicon". Then I drew the graph of the separated emotions.

### The stop words
Then I customized the stop words by adding the most frequent overlapping words among sentiments into the original stop words list.

### New emotional arc graphs
The new graph of the emotional arc(the change of density of all the sentiments as the story goes). The new graph of the emotional arc(the change of single sentiment as the story goes). I removed the "positive" and "negative" because they contribute more to the values of the story rather than the emotional experience.

### Polished outcome and interpretation
Finally, I polished the graph by using the functions of "RColorBrewer" and "ggthemes". [Here](https://github.com/ZeyuCao/The_Emotional_Arc_Of_GOT_Scripts/tree/main/S1E1_Sentiment_Analysis) is the separated emotional arc graph.
![This is an image](https://github.com/ZeyuCao/The_Emotional_Arc_Of_GOT_Scripts/blob/main/S1E1_Sentiment_Analysis/S1E1.tiff)

And finally I could interpret the story:

At the beginning, we can hardly see the joy or anger scenes, instead, the fear and the disgust soar. In the end, we may experience emotions combined with joy and sadness, with trust involved. This is rather a satisfying outcome, because the emotional arc we anticipate counters the plots in the show. For example, the opening scene consists with horror, fear and something that man dares not to be angry--which is the white walker. In the end, Ned agreed to go to King's Landing to be Robert's Hand, which corresponds with the emotional arc we guessed.  

### Post-editing: Adobe After Effects and Premier Pro

![This is an image](https://github.com/ZeyuCao/Sentiment_Analysis_on_GOT/blob/main/README_Photos/ae.png)
![This is an image](https://github.com/ZeyuCao/Sentiment_Analysis_on_GOT/blob/main/README_Photos/pr.png)

### How bad is the last season?
S8E5 and S8E6 are the most ones in the last season. Firstly, by reviewing the graph of the emotional density. I found that the S8E5 lacked in an accumulative strong ending. Despite of the fact that the emotional density of S8E5 is quite high, the too strong middle has diluted the intensity of the ending. The similar situation as S8E6, where the emotional intensity seems to be gradually descending from the first 1/4 part of the story.

One opposite example is the Show's highest rated episode, The Rains of Castamere, where the emotional density falls towards the lowest point in the middle and ascends to the strongest point in the end--The Red Wedding.

When considering the change of separated emotions, the peak also seems be in the middle where the audience experience the fear, anger and a bit of sadness and surprise(Daenerys and Drogon destroying king's landing). After that, the audience only see the anticipation soar in the end, which means the audience get more and more bored. Similar as in S8E6, the most impressive scene is in the middle, with the joy and trust vanishing and fear climbing towards the peak. (Jon killing Daenerys) After that, only the anticipation climbs, which is far from making an impressive season ending--no sadness, no joy or fear.
The positive example is also S3E9. During the red wedding, the emotions are complicated, the joy and trust going down meanwhile the anger, fear and sadness going the opposite direction. Only then, can the audience be impressed.

### What about other stories?
I decided to choose another story to see how this emotional arc approach can tell whether the movie is worth watching. The movie I chose was The Great Wall, directed by Zhang Yimou, a really famous director in China, The introduction of the movie at IMBd goes as below:

In ancient China, a group of European mercenaries encounters a secret army that maintains and defends the Great Wall of China against a horde of monstrous creatures.
I choose this movie because it is also of the same genre as GOT and coincidently it also tells a story on fighting against monstrous creatures.

The first step is also generating the word cloud to see the most frequent words mentioned in the film. At first glance, the emotional density seems quite high, but the emotional peaks are somehow evenly distributed. As a result, the audience keep concentrated most of the time, therefore feel frustrated. As for the separated emotional arc graph, the problem remains. The anger, fear and trust have multiple peaks which scatter. This may make the triggers of the narrative from the outward rather from inward, which makes the motivations pushing the story less convincing and the narrative lacking in rhyme. As one comment says: trying to put together too many things. After watching the film, I confirmed my guess and found it corresponding with the movie. 

## REFERENCES
Sentiment Dictionary: [Saif, Mohammad (2013). "NRC Word-Emotion Association Lexicon".](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)

Script of Game of Thrones: ["Genius Lyrics"](https://genius.com/artists/Game-of-thrones)

Reagan, A.J., Mitchell, L., Kiley, D. et al. The emotional arcs of stories are dominated by six basic shapes. EPJ Data Sci. 5, 31 (2016). https://doi.org/10.1140/epjds/s13688-016-0093-1

## TAKE AWAYS AND FUTURE IMPROVEMENTS

Expand my expertise in the programming language(R, Python)

Understand the Sentiment Analysis(NLP) better

Improve my mindset of design thinking

Be more professional in video production soft wares(AE, PR Pro)

Practice lighting setup in the studio and shooting with Sony camera

The project can be developed into an interactive app to see the emotional arc of given shows in the future
