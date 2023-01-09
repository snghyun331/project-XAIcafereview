from konlpy.tag import Okt
import os
os.environ['JAVA_HOME']=r'C:\Program Files\Java\jdk-19\bin\server'
print('JAVA_HOME' is os.environ)
okt = Okt()

text = "설치테스트"

print(okt.morphs(text))