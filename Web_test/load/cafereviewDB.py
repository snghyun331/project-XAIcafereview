# cafereviewDB 데이터를 불러오는 파일
import pymysql
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# 요청받은 지역, 카페명 변수로 해당 카페의 정보를 불러오는 함수
def load_infos(region, cafe_name):
    connect = pymysql.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "sng24678@",
        database='cafe_reviewDB'
    )
    cursor = connect.cursor()  
    query = f"""
            Select region, cafe_name, average_star, review_text from reviews 
            where region = '{region}' and cafe_name = '{cafe_name}'
            """
    cursor.execute(query)
    raws = cursor.fetchall()    
    connect.close()
    
    List = []
    for raw in raws:
        dict = {}
        dict['region'] = raw[0]
        dict['cafe_name'] = raw[1]
        dict['average_star'] = raw[2]
        dict['review_text'] = raw[3]
        List.append(dict)
        
    return List



# # 요청받은 지역, 카페명 변수로 해당 카페의 정보를 불러오는 함수
# def load_infos(region, cafe_name):
#     df = pd.read_csv('C:/Users/USER/PycharmProjects/origin_data.csv',encoding = 'utf8',index_col = 0)
#     df = df[(df['region'] == region)&(df['cafe_name'] == cafe_name)]
#     List = df.to_dict('records')
#     return List




##############
# 확인용
# print(load_infos('동작','카페퍼블리코 본점'))
# <출력결과>
# [{'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '밀크티 동윤영밀크티 모두 맛있어요 매장이 넓지 않아서 테이크아웃 했습니다'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '지나다니다가 꼭 한번 가보고싶어서  분당에서 온 친구들 3명과 빗속을 뚫고 갔습니다  9시
# 30분쯤 가서 주문하니 10시까지 영업한다고하여 30분도채못있었습니다 방문동기는 흰색 타일을 발라놓은 외관에서 내부가 너무 궁금해서였는데  밀크티맛집은 아니었구요  행
# 남자기 커피잔도 조금은 아쉬웠습니다 학생들이 좋아할만한 요소가 분명히 있겠지만 ...복고적 분위기를 좋아하시는분은 나쁘지않을것같습니다'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '뽀로야우왜케맛있어요...? 미쳤어요완전 분위기는 느낌있는 완존 인스타 감성의 화장실인테리어 캬캬 근데 주말에
#  1시간? 정도 지나면 나가달라고 정중하게 말씀하시는 걸 들었는데 2시간인지 1시간인지 기억이안나네욤 물론 저는 두명이서 빵3개를 30분만에 먹구 갔음니다 ㅎ 포장까지 했
# 죠 캬캬 힝 암튼 존맛이여요 ???? 또먹구싶닭닭'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '맛있음. 커피도 맛있고, 밀크티도  
# 맛있고. 근데 빵은 잘 모르겠음. 특별하진 않음.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '골목에 있어 더 홍콩의 느낌이 나 
# 는 곳! 뽀로야오 굿 그리고 밀크티는 부드러워서 그레잇~'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '12시에 나오는 빵이 맛있 
# 어요 ! 12시에 맞춰서 가면 따듯하게 맛잇게 먹을 수 있습니다 전반적으로 카페 분위기도 좋아요'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '근처에서 찾기 어려운 모처럼 트렌디한 내부의 카페지만 고즈넉하게 머물다가기에는 조금 아쉬웠다. 커피와 베이커리 모두 맛있었고 부담되지 않는 가격대였다. 넓지 않은 공간이라 금방 만석이 될 수 있겠다.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '갓 나온 뽀로야우는 버터가 촉촉하
# 게 빵에 스며들어 달콤함과 고소함이 어우러져 환상의 맛을 보여줍니다. 밀크티의 달달함과도 아주 잘어울려요 다시 방문할 의사 100프로 입니다.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '흠..무난 하네요 레트로 감성도 있고..근데 대학가에 골목에 있는 곳 치고는 커피가격이 비싸요 ㅜ'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '인테리어에 독특한 감성과 공기가 좋은 카페, 파인애플번과 음료도 좋았다. 다만 바닥에 전선 
# 이 마감처리가 안되어 있어서 걸릴 수도 있다는 점과 차가 예전과 달리 양이 많이 줄었다는 점이 아쉽..'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '버터두툼하게 껴둔 파인애플빵이 핵심! 진짜 살살녹는 악마의맛... 전 헤이즐넛라떼랑 같이먹는걸 좋아해요'}, {'region': '동작', 'cafe_name': '오후 
# 홍콩', 'average_star': 4.1, 'review_text': '맛있는 뽀로야우. 그리고 쿨한 분위기! 진정 흑석동의 핫플레이스.. Thumbs up for it'}, {'region': '동작', 'cafe_name': ' 
# 오후홍콩', 'average_star': 4.1, 'review_text': '분위기 좋음. 그러나 조용한 카페는 아님. 완전 개방형 공간이라 테이블 마다 말하는 소리가 뒤섞여 시끌벅쩍 함.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '이날 그린티라떼가 너무 마시고 싶었기에 그린티라떼 주문 친절친절 그리고 굉장히 진하게 
# 타주셨는데 제대로 다 안녹아서 잔 바닥에 가루덩어리들ㅠ 아까비ㅜ 친구가 마시던 아메리카노 한입 마셔봤는데 나쁘지 않았다 그리고 난 못먹어봤지만 파인애플 번이 그리  
# 맛잇다는데 버터를 넣은건 핵짱맛탱이라는데 조만간 시험끝나고 먹으러 가줘야지 그리규 알바생님 사장님두 다 잘생겼..??'}, {'region': '동작', 'cafe_name': '오후홍콩', 
# 'average_star': 4.1, 'review_text': '중앙대 근처에 몇 없는 감성 카페 ?? 밀크티도 맛있고 특히 뽀로야우는 최고다 사장님도 친절하시고 왜 장사가 잘되는지 알 것 같은  
# 카페'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '11시에 와서 빵은 못 먹어봄. 커피는 맛있음. 밀크티 추천이 있었으나 커피가 
# 너무 먹고 싶어서.. 담을 기약하며...'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '핫 밀크티와 뽀로야우 번 추천합니다. 커피맛
# 은 평범..커피는 추천하지 않습니다.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '코렐 클래식 플레이트에 내주는 작은 성의에서
#  마음이 열렸음. 오후이긴 한데 여긴 그래도 검은돌 마을'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '따뜻한 밀크티, 꼭 드셔보
# 세요~ 앙버터가 들어있는 빵도 꼭.꼭.꼭 드셔보세요~ 젊은 주인분께서 직접 빵도 만드시고 있고 음료도 주시고 계산도 하시던데~ 마스크넘어 미소가 따뜻한 분입니다. 차를  
# 새우고 좀 걸어야하는 아쉬움이 있어요~^^'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '밀크티가 우려낸게 아닌 가루로 만들어진
# 것 같습니다 일박 밀크티 대비 단맛이 강합니다'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '분위기 좋고 수다 떨기 좋은 곳??'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '친구학교앞에 놀러간거였는데 이쁜카페가 있어서 너무 좋았습니다!! 단걸 좋아하는데
#  제 기준에선 헤이즐넛라떼도 맛있고 빵도 맛있었어요~'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '매일 12시에 나오는 빵 중에
#  뽀로야우빵 사이 버터 한장 들어있는 빵는 단짠의 끝판왕.. 밀크티나 아메리카노 한잔과의 궁합은 디저트 끝판왕 충분... 내부 분위기는 흰색 목욕탕룩... 의자와 테이블은 
# 다소 불편... 오직 뽀로야우 하나 보고 간다.. 그 맛은 정말... 잡솨봐... 5점 잘 안주는데 뽀로야우는 5점 줍니다..'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '분위기 정말 좋아, 밀크티는 생각 보다 light한거같애'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '흑리단길 어쩌구 저쩌구의 초석이 된 것 같은, 다른 곳에 비해 비교적 있은 지 오래 됐지만 흑석에서 맛과 분위기가 가장 괜찮은 카페. 정체성이 아주 확실하다.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '중앙대 주변의 레트로풍 카페. 밀크티와 빵이 맛있다. 한쪽 벽이 온통 유리인데 유리 밖으
# 로 보이는 골목벽도 예쁘다.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '중앙대 앞의 작은 카페. 깔끔한 인테리어에 무난히 맛 
# 있는 음료들.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '인스타그램 맛집. 근데 딱 인스타그램용 맛집. 의외로 사진보다 실제 
# 론 별로였습니다. 집앞이라서 괜찮았지만, 10키로 이상 떨어진곳에서 여길위해 온다면 후회하실겁니다... 다만 빵은 맛있더라구요.'}, {'region': '동작', 'cafe_name': '오 
# 후홍콩', 'average_star': 4.1, 'review_text': '파인애블빵, 밀크티 맛있어요. 타일로 인테리어가 되어있고 깔끔합니다.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '그냥 그런 장소~특별히 좋은거 모르겠던데, SNS에서 유명세 있는 이유를 찾아볼래도 찾을수없었던,그런곳'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '특이한 분위기 인테리어와 홍콩스타일 번 과 커피 도 좋네요.'}, {'region': '동작', 'cafe_name': '오후홍콩', 
# 'average_star': 4.1, 'review_text': '빵이 맛있다고 하나 이때 방문했을때 음료만 먹었음. 음료는 무난'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 
# 4.1, 'review_text': '따둣한 밀크티 맛있어용'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '버터빵  맛있음 ~~매'}, {'region': 
# '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '인스타 갬성....사진이 이쁘게 잘 찍힙니당! 자리에 비해 사람이 많은 편!'}, {'region': '동작', 
# 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '밀크티도 좋고 뽀로야우는 최고에요'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '인테리어가 이쁘다 빵이 단짠단짠의 극치! 음료는 평범'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '분위기도
#  좋고, 맛도 좋아요!'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '자리는 조금 협소하지만 뽀로야우가 맛있습니다'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '오래 앉아 있는듯한 학생들을 쫓아내고, 나가는 손님에게 트레이반납을 소리쳐서 요청하는 광경을
#  목격.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '빵이 진짜 맛있어요'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '맛있고 종업원들이 친절함'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '12시에 나오는 빵이 맛
# 있습니다.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '아주 맛있음! 밀크티 굳'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '가격은 후덜덜이지만 맛은 있다'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '밀크티는 
# 좀 달아요'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '화장실 분위기쓰'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '분위기좋고 좋아요'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '맛있는 빵과 밀크티'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '빵 맛 있어요.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '맛있어요'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '굿'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '감성가득 포토존'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '분위기 좋아요'}, {'region': '동작
# ', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '나름 보통'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '빵 
# 굿굿굿'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': '특이..'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': " 서울에서 버터 ?蘿 油로 홍콩 파인애플 롤빵을 맛볼 수있는 좋은 장소.   Nice place to taste Hong Kong's pineapple bun with butter ?蘿油 in Seoul."}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': ' 특별한 분위기를 즐기고 홍콩 스타일의 사막을 먹을 수 있습니다.   You can enjoy special atmosphere and eat some hongkong style desert.'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': ' 밀크티크는 분유를  
# 사용하는 것과 조금 다릅니다!   ?茶有点像用?粉?的！'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': ' 주인이 자주 떠나라고   Owner often asks you to leave'}, {'region': '동작', 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': ' 좋은 밀크티   Good milk tea'}, {'region': '동작', 
# 'cafe_name': '오후홍콩', 'average_star': 4.1, 'review_text': ' 맛있는   おいしいい'}]