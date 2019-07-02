# random-sentence-list

## Description
This project provides an intuitive API for generating any number of files containing random sentences. All languages are supported.

## Installing dependencies

    pip install -r requirements.txt
    
## API

### ListGenerator.set_language(language)
Sets the language of the metawiki from which the sentences are downloaded. It uses the standard language codes.

### ListGenerator.random_sentence_files(sentences_per_file, num_files)
Generates *num_files* files, each consisting of *sentences_per_file* sentences.
