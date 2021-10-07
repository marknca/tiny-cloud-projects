# Tiny Cloud Project

Code from my Tiny Cloud Projects

## Live Text

In the latest update to iOS and iPad OS, the camera can now auto-detect text in pictures (yes, this has been in Android for a while). 

This is a handy feature that I'd like on my Mac as well. But it's not out yet, so let's have some fun and build a little tool to do the same thing!

We're going to using a couple of Google Cloud services to build out a simple command line application that takes an image file and returns any text inside.

This was [live streamed](https://youtu.be/k1vO8DJBzD0) on Thursday, 23-Sep to YouTube.

### Goal

`live-text.py -i PATH-TO-IMAGE-FILE`

This command will take the specified image file, send it to [Google Cloud's Vision API](https://cloud.google.com/vision), and prints the text in the image to the command line. 

`live-text.py -i PATH-TO-IMAGE-FILE -c`

...does the same but also copies the text to the macOS clipboard.

`live-text.py -i PATH-TO-IMAGE-FILE -c -o NEW-IMAGE-FILE-WITH-OVERLAY`

...creates an output image highlighting where in the image the text was found.

### Sample Images

The sample images in the repository are from Apple's September 2021, "[California Streaming](https://www.apple.com/apple-events/september-2021/)" event that announced the iPhone 13's and a lot more. I usually live tweet events like that and have a script that automatically takes these screen captures. 

It would be useful in this use case and many others, to be able to automatically extract the text from any given image.

---

## Transcription

I often deal with videos and audio recordings of talks that I've given and want to do more with. The most obvious thing is to create a closed captioning file to help with accessibility and usability on mobile.

Google Cloud (and others) offer an API that can help with this. The [Speech-to-Text API](https://cloud.google.com/speech-to-text/docs/libraries) is very straight forward to deal with once you are aware of some of it's quirks.

In this project, we build the code required to send an audio file to the API, get the results, and then generate a captioning file formated as [.srt](https://en.wikipedia.org/wiki/SubRip). 

This was [live streamed](https://youtu.be/6S6vQDdonAs) on Thursday, 07-Oct to YouTube.

### Goal 

This project was built in a [Jupyter notebook](https://jupyter.org/) to make it easier to explain on stream. That notebook contains all of the required code to build a simple command line script or a web function.

That exercise is left to the viewer.

### Sample Audio

I've recorded some sample audio in the transcription/samples folder to use with the API if you don't have anything handy. The `.m4a` will generate an error with the API. The `.wav` will both transcribe correctly.