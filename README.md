# Run AI.

## Summary
Using an ImageNet Classification Neural Network ([AlexNet](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)), the AI was trained to take in live screen capture of a game (Run 2) and output an action that would allow the player character to survive.

### How the game works
The player character, sprite, runs on some platforms in open space. The sprite can not slow down and can only move in 3 directions; left, right and upwards (jump). Given that the sprite is moving at a constant pace and there is no time restrictions, the primary objective should be to survive (don't fall off).

![Image from CoolMathGames](https://www.coolmathgames.com/sites/default/files/run-2.png)

## The AI

### Step 1: Image Processing
Although seemingly simple, there were too many inputs from the screen capture to be able to adequately train the model. The input needed to be broken down as much as possible to adapt to the processing capabilities a 2nd rate laptop.

In reality, the AI does not need to see the platforms, only their edges. So the first step was to apply **canny edge detection**. This is done in the process_img() function in grabscreen_opencv.py. For each frame, the image was first converted to grayscale. Then an initial run of cv2's .Canny() function followed by a gaution blur then a second modified Canny function; auto_canny(). 

![Canny Output](https://github.com/msheroubi/run-AI/blob/main/images/canny%20edge%20-%20run%20ai.png?raw=true)

These steps are necessary for the next step, **line detection**. This is done using [probabilistic hough transform](https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html). After fine tuning the inputs and threshholds (maxLineGap, minLineLength), a setting was reached that worked perfectly for this use case. The result was an array of lines that highlighted the edges of the platforms in the game.

![Hough Output](https://raw.githubusercontent.com/msheroubi/run-AI/main/images/hough%20line%20-%20run.png)

The final step of the image processing was an **optimization step**. Notice in the previous image, there is a lot of data on that screen that would not help the AI "survive" or make moves. As a matter of fact, most of the frame is not needed to beat the levels in the game. To **find the region of interest** (ROI), I tested on myself the limits of these bounds, obscuring as much of the screen as possible while still beating each level. After rigorous testing, the shape that worked best was an upside down trapezoid. Isolating the ROI cut down processing time by over 60%.

![ROI Isolation](/images/roi_runai.png)

_This is a rough representation of the shape and size of the isolated region_

### Step 2: Training

Not much is unique in this section. I used a pre-existing convolutional neural network called AlexNet. The model was trained by feeding it hours of playtime with the inputs being the line arrays and the outputs being keystrokes (left, right, jump). A portion of the training data was taken out to be used for testing.

### Results

While the AI managed to beat the first few levels quite easily, it ran into problems with more complicated levels. Some levels required the sprite to do a full rotation, jump onto platforms that the AI doesn't know are there (ceiling jumps), and some required some forethought, which calculating was outside the project scope & hardware capabilities.

