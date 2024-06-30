# Rassam - Live Drawing App ✨🖌️

![Omar using Rassam](assets/rassam-demo.gif)

*Magic in action*

## Backstory

Hey there! 👋 Welcome to Rassam (that's Arabic for "artist", BTW). 

It's a lazy weekend afternoon, chilling with my little brother and sister, and they're going on and on about how cool it would be to have magical powers. "What if you could draw in the air?" And there I am, thinking about my AI professor who said in the very introductory lecture: "AI is not magic."

Fast forward through a Claude Sonnet 3.5 coding spree, some hair-pulling debugging sessions, and more hand gestures in front of my webcam than I'd like to admit, and voilà! Rassam was born.

Now they think I'm a wizard (don't tell them otherwise), and we've got this cool app that lets you wave your hand around like a wand and create digital art. It might not be "real" magic, but the smiles on their faces when they tried it? That feels magical enough for me.


## What's This Magic All About?

Rassam uses your webcam to track your hand movements and turns them into digital drawings on your screen. It's like having a magic wand, but instead of saying "Wingardium LevioSA" you just wiggle your fingers!

Here's what you can do with it:
- Draw in the air with your index finger (no wand required)
- Choose any color you want 
- Make your lines as thick or thin as you like
- See cool hand landmarks if you're into that sort of thing
- Clear the canvas when you want a fresh start (or when your "masterpiece" looks more like a mess)

## Try It Out

1. Clone this repo:
    ```bash
    git clone https://github.com/Bushrxh/rassam.git
    cd rassam
    ```
2. Set up a virtual environment (because we're responsible coders):
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Install the goods:
    ```bash
    pip install -r requirements.txt
    ```
4. Finally, type this spell:
    ```bash
    streamlit run rassam_app.py
    ```

## How to Become a Rassam Artist

1. Run the app and grant it access to your webcam (don't worry, we're not secretly recording)
2. Check out the sidebar to pick your color and line thickness.
3. Raise your index finger above your middle finger to start drawing.
4. Pew, move your hand around.
5. Open your whole hand (or just lower your index finger) when you want to stop drawing.
6. Hit "Clear Canvas" if you want a do-over (we all make mistakes, right?).
7. Click "Stop" when you're done creating your masterpiece.

## Contributions

Got ideas? Awesome! Whether it's adding sparkles, or making it work with your toes (hey, no judgment), all contributions are welcome!

## What's Next?

I've got big dreams for Rassam (or maybe that's just the 12 AM talking). Here's what I'm thinking:
- Multiple colors (on the same canvas)
- Save and load drawings (so you can prove to your friends that you're the next Picasso)
- Undo/Redo 
- Multi-hand support (collaborative drawing, anyone?)

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for their hand tracking solution
- [Streamlit](https://streamlit.io/) for the app framework
- [OpenCV](https://opencv.org/) for computer vision capabilities
