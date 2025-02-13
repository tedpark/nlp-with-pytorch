from pororo import Pororo

Pororo.available_tasks()

# ocr = Pororo(task="ocr")
# print(ocr("./ocr-test.png"))


mt = Pororo(task="translation", lang="multi")
# text1 = "퍼서비어런스(Perseverance)는 화성 탐사차로 2020년 7월 30일 발사하여 2021년 2월 18일 화성에 착륙하였다. 화성의 생명체 거주 여부, 화성의 고대 환경 조사, 화성 지표의 역사 등을 밝히는 것이 이 탐사선의 목표다. 더불어 중요한 목표는 미래의 인류가 화성을 유인 탐사할 때 위험한 것이 없는지 탐색하고, 대기의 조성을 알려주어 미래의 기지를 건설하는 데 도움을 주는 것이다. 또 인간이 어떤 조건으로 착륙해야 되는지 등을 탐색한다. 예산은 원래 15억 달러를 배정했는데, 지금은 더 늘어나서 25억 달러다. 특이사항으로는 인사이트가 마스 큐브 원과 화성에 함께 갔던 것과 비슷하게 인제뉴어티와 함께 발사되었다. 또한 큐리오시티의 디자인을 많이 재사용했다. 따라서 새로운 기술보다는 이전 로버들의 좋은 점을 합친 것이라고 보면 된다. 참고로, 마스 2020(Mars 2020)은 퍼서비어런스와 인제뉴어티 드론 헬리콥터를 포함한, NASA의 화성 지표면 로봇 탐사 계획의 명칭이다. 최초로 화성의 바람소리를 녹음했다."
text1 = "안녕하세요"

print(mt(text1, src="ko", tgt="en"))
