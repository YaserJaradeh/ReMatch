# ReMatch
Semantic Lab project

## Installation and Running
### Required packages
* numpy
* glove_python
* sklearn
* practnlptool
* textrazor
* cPickle

### Required data files
* glove precomputed data files
* patty data files (included <not big>)

### Required Data
* text-razor API key

## Code explanation:
PS. File names are self explanatory

1. Tagger: POS tagger
1. Splitter: split the question into combinations
1. Embedder: glove wrapper to convert question into vectors
1. Reader: PATTY data reader
1. Backend: the complete process of reading PATTY data and create embeddings, with the cosine similarity code
1. Frontend: the complete process of reading a question and processing it
1. Textrazor_Api: the API wrapper for the textrazor service
1. JsonQueryParser: the QALD dataset reader (edited)
1. main: where the magic happens


## Any other issues:
Please try solving it before telling me :)

