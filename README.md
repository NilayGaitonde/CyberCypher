# Spoiler Detection System for Avengers Endgame

## Overview
This project presents a spoiler detection system designed for Avengers Endgame using a combination of web scraping and natural language processing (NLP) techniques. The algorithm extracts the plot synopsis from the IMDb page for Avengers Endgame, cleans the text, and identifies potential spoilers using n-grams. To enhance accuracy, only phrases occurring at most twice are labeled as spoilers, minimizing false positives.It was built as part of a 24 hour hackathon in which it placed 3rd.

## Implementation
The algorithm is implemented in Python, utilizing libraries such as NumPy, Selenium, and Tkinter for the graphical user interface (GUI). The core functionality involves:
- Retrieving the IMDb plot synopsis.
- Cleaning the text by focusing on the second half of the plot.
- Generating n-grams and counting their occurrences.
- Identifying potential spoilers based on occurrence count.

## Usage
1. Ensure the required libraries (NumPy, Selenium, Tkinter) are installed.
2. Run `app.py` on your machine to launch the GUI.
3. Input or paste a text to be analyzed for spoilers.
4. The algorithm will process the input and display whether it contains potential spoilers.

## Demo
[Click here](https://drive.google.com/file/d/1rQLgaRgWbysg4NxA--htFNbnuG9CL8PZ/view?usp=sharing) for a demo of the spoiler detection system.
