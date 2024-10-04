from text2vec import SentenceModel
import  json
sentences = ['苹果']
model = SentenceModel(r"D:\Code\text2vec-base-chinese")
embeddings = model.encode(sentences)
# print(embeddings.shape)
# print(json.dumps(embeddings.tolist()[0]))
out = embeddings.tolist()
out1 = out[0]
print(len(out))
print(len(out1))
print(type(out1))
# print('dimension size of vector is: {}'.format(len(json.dumps(out1))))

# model.encode("如何更换花呗绑定银行卡")