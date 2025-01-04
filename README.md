## InterviewSense Backend

Contains serverless handlers for InterviewSense's website and video-based note-takers

**Website Note Taker**
This InterviewSense features allows users to paste in a website and have notes be automatically generated using AI. This is done by calling a handler on a FastAPI endpoint, which scrapes the relevant webpage using Selenium, extracts all relevant text, and feeds it to an LLM through a MapReduce chain, eventually generating a summary of the website

**Video Note Taker**
This feature allows users to paste in a video link or upload a video file to have notes be taken. This handler transcribes the audio part of the video and passes the text through a MapReduce LLM chain to create a detailed summary of the video's auditory contents.
