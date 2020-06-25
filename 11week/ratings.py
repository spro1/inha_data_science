"""
다음 조건에 맞는 파이썬 코드 1개를 제출해주세요.
1. ratings.dat 파일을 이용하여 movie_id 별로 user_id 가 영화를 보았는지 아닌지를 표시하는 테이블을 표시하시오 .
2. 이후에 movie_id 별로 영화를 본 사람 수를 상위 20개의 영화에 대해 내림차순으로 정렬해서 bar 차트로 표현하시오.
"""

import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


# 파일 불러오기
ratings = pd.read_csv('ratings.dat', engine='python', sep='::', header=None, names=["user_id", "movie_id", "score", "timestamp"])
users = pd.read_csv('users.dat', engine='python', sep='::', header=None, names=['user_id', 'gender', 'age', 'occupation', 'zip'])
movies = pd.read_csv('movies.dat', engine='python', sep='::', header=None, names=['movie_id', 'title', 'generes'])


# zero행렬
# user_id x movie_id
# [3883 rows x 6040 columns]
zero = np.zeros((len(users), len(movies)))

# zero행렬을 DataFrame으로 변환
dummy = pd.DataFrame(zero, columns=movies.movie_id)
# users_id index 1 start
dummy.index = np.arange(1, len(dummy)+1)


for n, p in enumerate(ratings.user_id):
    #print(n, p, ratings.movie_id[n])
    dummy.loc[p, ratings.movie_id[n]] = 1
    # user_id, movie_id column에 1 넣음

# Term Document Matrix형식으로 변경
TDM = dummy.T   # dummy Martrix를 Transpose 함
print(TDM)

# movie_id 별로 내림차순 정렬
movie_counter = TDM.sum(axis=1)
movie_counter = movie_counter.sort_values()
print(movie_counter)

# 상위 20개 그래프 시각화
movie_counter[-20:].plot(kind='barh', title='movie most view counter')
plt.show()
