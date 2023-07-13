# Importing modules 

import spacy


# Function to open and read the file movies.txt

def load_movie_descriptions(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Function to find the most similar movies 

def get_most_similar_movie(description, movie_descriptions):
    nlp = spacy.load('en_core_web_md')
    description_doc = nlp(description)

    movie_similarities = []
    for movie_description in movie_descriptions:
        movie_doc = nlp(movie_description)
        similarity = description_doc.similarity(movie_doc)
        movie_similarities.append(similarity)

    most_similar_index = max(range(len(movie_similarities)), key=movie_similarities.__getitem__)
    most_similar_movie = movie_descriptions[most_similar_index].strip()

    return most_similar_movie

# If Statement used to prince what is recommended to watch.

if __name__ == '__main__':
    movie_descriptions = load_movie_descriptions('movies.txt')
    description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    most_similar_movie = get_most_similar_movie(description, movie_descriptions)
    print("You should watch:", most_similar_movie)
