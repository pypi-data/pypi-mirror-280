# Live webcam narration

By combining a few Scalify tools, you can quickly create a live narration of your webcam feed. This example extracts frames from the webcam at regular interval, generates a narrative, and speaks it out loud.

!!! info "Video and audio extras"
    This example requires the `audio` and `video` extras to be installed in order to record video and play sound:

    ```bash
    pip install scalify[audio,video]
    ```



!!! example "Webcam narrator"
    ```python
    import scalify
    import scalify.audio
    import scalify.video

    # keep a narrative history
    history = []
    frames = []

    # begin recording the webcam
    recorder = scalify.video.record_background()

    # iterate over each frame
    for frame in recorder.stream():
        
        frames.append(frame)
        
        # if there are no more frames to process, generate a caption from the most recent 5
        if len(recorder) == 0:
            caption = scalify.caption(
                frames[-5:],
                instructions=f"""
                    You are a parody of a nature documentary narrator, creating an
                    engrossing story from a webcam feed. Here are a few frames from
                    that feed; use them to generate a few sentences to continue your
                    narrative.
                    
                    Here is what you've said so far, so you can build a consistent
                    and humorous narrative:
                    
                    {' '.join(history[-10:])}
                    """,
            )
            history.append(caption)
            frames.clear()

            # generate speech for the caption         
            audio = scalify.speak(caption)

            # play the audio
            audio.play()
    ```