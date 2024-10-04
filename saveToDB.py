from text2vec import SentenceModel
import psycopg2
import  json
def connect2PG():
   conn = psycopg2.connect(
       user="zxq",
       password="xtvjxk163",
       host="localhost",
       port=5432,  # The port you exposed in docker-compose.yml
       database="postgres"
   )
   return conn
def execSQL(conn,sql):
   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()
   cur.close()
   conn.close()

def querySQL(conn,sql):
   cur = conn.cursor()
   cur.execute(sql)
   # conn.commit()
   r = cur.fetchall()
   cur.close()
   conn.close()
   return r

def generatedEmbedding(text):
   sentences = [text]
   model = SentenceModel(r"D:\Code\text2vec-base-chinese")
   embeddings = model.encode(sentences)
   return json.dumps(embeddings.tolist()[0])
   #print(json.dumps(embeddings.tolist()[0]))
   #print('dimension size of vector is: {}'.format(len(json.dumps(embeddings.tolist()[0]).split(","))))
def loadVec2DB(id,text):
   embeddings = generatedEmbedding(text)
   # print(embeddings)
   sql =  """ insert into product(id,name,embedding) values({},'{}','{}')""".format(id,text,embeddings)
   # print(sql)
   conn = connect2PG()
   execSQL(conn,sql)

def querySimiliary(text):
   embeddings = generatedEmbedding(text)
   # print(embeddings)
   sql = """
   SELECT id, name, 1 - (embedding <=> '{}') AS cosine_similarity
              FROM product
              ORDER BY cosine_similarity DESC LIMIT 2
   """.format(embeddings)
   conn = connect2PG()
   # print(sql)
   return querySQL(conn,sql)


if __name__ == '__main__':
   #  loadVec2DB(1,'苹果')
   #  loadVec2DB(2,'香蕉')
   #  loadVec2DB(3,"足球")
   #  loadVec2DB(4,"篮球")
   l = querySimiliary("体育运动器械")
   print(l)