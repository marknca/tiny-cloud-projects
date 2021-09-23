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