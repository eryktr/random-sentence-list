# random-sentence-list

## Description
This project provides an intuitive API for generating any number of files containing random sentences. All languages are supported.

## Installing dependencies

    pip install -r requirements.txt
    
## API

### ListGenerator.set_language(language)
Sets the language of the metawiki from which the sentences are downloaded. It uses the standard language codes.

### ListGenerator.random_sentence_files(sentences_per_file, num_files, output_path="")
Generates *num_files* files, each consisting of *sentences_per_file* sentences.
The output path should specify the absolute path to the directory where the files should be saved.

## Output file
The output file is a valid, ready-to-compile LaTeX file containing all of the generated sentences in an enumeration environment. Every file is assigned a unique name, composed of the current timestamp in seconds, formatted to human-readable date.

