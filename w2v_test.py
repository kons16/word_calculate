
from gensim.models import KeyedVectors

file_name = "../entity/entity_vector/entity_vector.model.bin"
model = KeyedVectors.load_word2vec_format(file_name, binary=True)

out = model.most_similar(positive=['[王]', '[女]'],
                         negative=['[男]'])

print(out)


'''
from gensim.models.word2vec import Word2Vec

model_path = '../entity/shiroyagi/word2vec.gensim.model'
model = Word2Vec.load(model_path)

out = model.most_similar(positive=['国王', '女'],
                         negative=['男'])

print(out)
'''
