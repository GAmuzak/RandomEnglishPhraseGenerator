# RandomPhraseGenerator

Shows random english phrases based on the [Mackenzie phrase set](https://www.yorku.ca/mack/chi03b.html)

## Usage

To run this program, clone the repository, and run the following commands

```py
pip install requirements.txt
```

```py
python phrase_generator.py
```

Once the window appears, right click to generate a random phrase.

Close the program anytime to exit.

## Functioning

The script automatically fetches the phrase set from the [permanent download link](http://www.yorku.ca/mack/PhraseSets.zip) and unzips its contents in the Data folder. It fetches the phrase set from there. If the phrases are ever updated, or if a different dataset is to be provdided, please edit the target url and target file in the header of the main script as required.
