# Pex-tech-challenge

## Goal

1. To create a dataset of indoor and outdoor images

2. To train a model to identify images as belonging to the indoor or outdoor class

3. To build a CLI tool to input images one by one, and for the tool to predict the class that the image belongs to


## Methodology

I used the script from [this](https://github.com/gsssrao/youtube-8m-videos-frames) codebase to extract relevant videos from the YouTube-8m dataset. The categories I queried for indoor images were Room, Bedroom, Classroom, Office, Gym, Couch, Cooking, and Chair. The categories I queried for outdoor images were Beach, Landscape, Skyscraper, Mountain, Hiking, Skiing, Weather, and Thunderstorm. After obtaining these videos, I extracted 5 frames from each video to create a dataset of images.


I used a pretrained VGG16 model, excluding the fully connected layers. Instead, I added fully connected layers of my own, and trained only those layers on the dataset that I had collected. Due to the lack of compute power on my local machine, I trained it only for 5 epochs. I was able to obtain a validation accuracy of 79.92%. 


I then created a command line tool called "mytool", which would take an image path as an argument, and would output whether the image was taken indoors or outdoors.


## Running the code

1. Install python 2.7
2. Install virtualenv
3. Clone this repository
4. cd into this repository
5. Create a virtual environment
6. Run <code>pip install -r requirements.txt</code>
7. Run <code>python setup.py</code>
8. Run <code>mytool --img img\_name</code> where <code>img\_name</code> is the path to an image of your choice


## Important notes

#### The main source code is contained in the 'src' directory

<code>utils.py</code> was used to create the dataset. It was run as <code>python utils.py indoor</code> or <code>python utils.py outdoor</code> depending upon the data I was creating.

<code>model.py</code> contains the code for training the deep learning model. It took no other arguments, and simply ran with 'python model.py'

<code>unit\_test.py</code> contains a few test units that I wrote


#### All the data related content is contained in the 'data' directory

It contains a directory titled <code>photos</code>, which contains the dataset I created.

It was in this folder that I had two other folders, each containing the indoor and outdoor videos respectively. Due to the size of the videos, I did not upload them onto github.

It also has two bash scripts, which were used to make the data processing more convenient.
