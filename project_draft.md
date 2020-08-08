#주알못 리서치
##기획의도

-주식 검색 시, 키워드 정보제공  
-전문가(애널리스트)의 목표주가 및 의견을 모아보기  
-뉴스 기사의 톤을 토대로 상승모멘텀 살펴보기  

##구현 기능
####1.애널리스트 목표 주가 및 의견을 모아보기  
1)[링크](http://consensus.hankyung.com/apps.analysis/analysis.list) 에서 *목표가/제목/증권사/애널리스트이름/일자*를 크롤링: 최대 20개   
2)해당 데이터를 mobgodb에 저장  
**?저장 데이터를 주기적으로 업데이트 해줘야 하는지?**   
셀레니움 크롤링

####2.뉴스 기사의 톤을 토대로 상승모멘텀 살펴보기
1)뉴스 기사 제목 크롤링  
2)뉴스 기사 제목의 형태소 분리  
3)형태소분리의 감성사전을 이용한 감정분석:관련 방법 링크 참조    
[링크](https://github.com/mrlee23/KoreanSentimentAnalyzer)  
[링크](https://m.blog.naver.com/PostView.nhn?blogId=jjys9047&logNo=221599162443&proxyReferer=https:%2F%2Fwww.google.com%2F)  
[링크](https://m.blog.naver.com/jjys9047/221586527508)  
4)score 부여 및 계산을 통해 긍정/중립/부정 signal 생성  
**?score로직검증필요**
Konlpy, eKonlpy

####3.javascript 워드 클라우드 라이브러리   
1)뉴스 기사 제목 크롤링 데이터를 기반으로 가장 빈번히 등장하는 워딩 카운트  


####4. 레이아웃 mobile first로 잡기