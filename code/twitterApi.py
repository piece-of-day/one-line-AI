# 패키지 파일 다운로드
# 아래 코드 terminal에 한 줄씩 입력

# pip install python-twitter
# pip install environ

twitter_consumer_key = ""
twitter_consumer_secret = ""  
twitter_access_token = ""
twitter_access_secret = ""

from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# main code start
import twitter, time

# twitter api connect
twitter_consumer_key = env('twitter_consumer_key')
twitter_consumer_secret = env('twitter_consumer_secret')
twitter_access_token = env('twitter_access_token')
twitter_access_secret = env('twitter_access_secret')

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

# 특정 계정의 타임라인 긁어오기

account = "@bts_bighit"
timeline = twitter_api.GetUserTimeline(screen_name=account, count=200, include_rts=True, exclude_replies=False)
print(f'{account}계정 타임라인 긁어오기')
print(timeline)
# 텍스트만 긁어오고 싶은 경우
# print(timeline.text)




# 검색하기(해시태그 검색 가능)
query = "방탄소년단"
search = twitter_api.GetSearch(term=query, count=100)

for i in search:
    print(i.text) # 텍스트만 출력하기



# 실시간 수집
query = ["방탄소년단"]
stream = twitter_api.GetStreamFilter(track=query)
        
for tweet in stream:
	print(tweet['text'])

