# README



## 1. 프로젝트 소개 :mega:

- :movie_camera:영화 정보 기반 추천 서비스 구성
- :speech_balloon:커뮤니티 서비스 구성
- :facepunch:HTML, CSS, JavaScript, Django, DataBase 등을 활용한 실제 서비스 설계
- :boom:서비스 배포 및 관리





## 2. TEAM :couple:

### 2-1 TEAM Infomation

- 팀장: 이경석
- 팀원: 김문석
- 팀명: SSUCKK(썪)



### 2-2 업무 분담 내역

- **이경석**

  - TMDB 영화 데이터 수집 및 추출
  - Django accounts App 설계 및 구현
  - Django movies App 설계 및 구현
    - date-recommend algorithm
    - 리뷰 상세 페이지
    - 좋아요 기능 구현
  - 공동 front 단 작업

  

- **김문석**

  - TMDB 영화 데이터 수집

  - Django movies App 설계 및 구현

    - index (첫 화면)
	  - select-recommend algorithm
    
	  - 영화 상세 페이지
	  - 리뷰, 댓글 수정 및 삭제
	
	- 공동 front 단 작업





## 3. 목표 서비스 및 실제 구현 기능 :gift:

### 3-1 목표 서비스

- 기본적인 signup, login,  logout 기능

- user 간의 follow 기능

- date-recommend algorithm

- select-recommend algorithm

- 영화 상세 페이지 및 리뷰 작성 기능

- 리뷰 상세 페이지 및 댓글 작성 기능

- 영화, 리뷰 좋아요 기능

- user 가 좋아하는 영화, 리뷰 표시 기능



### 3-2 실제 구현 기능

#### 3-2-1 개발 일지

![notion1](https://user-images.githubusercontent.com/60080675/84895780-cfdf4b80-b0dd-11ea-9beb-8911c8173c71.JPG)
![notion2](https://user-images.githubusercontent.com/60080675/84895766-c9e96a80-b0dd-11ea-8466-755fed6fb9f0.JPG)
![notion3](https://user-images.githubusercontent.com/60080675/84895833-e38ab200-b0dd-11ea-8cfc-445cfaf9817b.JPG)


#### 3-2-2 실제 구현 화면

- ##### Signup (회원 가입)

![signup](https://user-images.githubusercontent.com/60080675/84895883-fbfacc80-b0dd-11ea-99c5-fb9f87d1d92c.JPG)




- ##### login

![login](https://user-images.githubusercontent.com/60080675/84895934-10d76000-b0de-11ea-9213-cf1fabe218dd.JPG)




- ##### index

![index](https://user-images.githubusercontent.com/60080675/84895938-13d25080-b0de-11ea-8654-3239e671ea31.jpg)



- ##### profile

![profile](https://user-images.githubusercontent.com/60080675/84896025-2b113e00-b0de-11ea-9bcf-ba22c6ab854f.jpg)



- ##### date-recommend

![date-recommend](https://user-images.githubusercontent.com/60080675/84896032-2fd5f200-b0de-11ea-8ecb-6e285aa7328d.jpg)

![description1](https://user-images.githubusercontent.com/60080675/84896035-32384c00-b0de-11ea-928f-87619788920a.jpg)



- ##### select-recommend

![select-recommend-start](https://user-images.githubusercontent.com/60080675/84896103-4e3bed80-b0de-11ea-90fb-b454193716d2.jpg)

![description2](https://user-images.githubusercontent.com/60080675/84896111-5005b100-b0de-11ea-9034-b7fa21cdc1b9.jpg)

![select-recommend-result](https://user-images.githubusercontent.com/60080675/84896114-5136de00-b0de-11ea-87cf-65dd0b29824f.jpg)



- ##### movie_detail ( 영화 상세, 리뷰 작성 및 수정삭제, 리뷰 목록)

![movie-detail](https://user-images.githubusercontent.com/60080675/84896157-69a6f880-b0de-11ea-8bbe-10d318a7761c.jpg)



- ##### review_detail (리뷰 상세, 댓글 작성 및 수정삭제, 댓글 목록)

![review-detail](https://user-images.githubusercontent.com/60080675/84896161-6b70bc00-b0de-11ea-9c30-e788d42e6f38.jpg)



## 4. 데이터 베이스 모델링 (ERD) :hammer:

![ERD](https://user-images.githubusercontent.com/60080675/84896164-6d3a7f80-b0de-11ea-907d-f206b12f5f9d.JPG)




## 5. 배포 서버 URL :airplane:

- 





## 6. 고찰 및 느낀점 :hotsprings:

- ##### 이경석

  - 처음에 TMDB 영화 API를 사용하기로 결정하고, data를 수집하는 과정해서부터 시행착오가 많았다.  우리가 원하는 data는 영화와 장르였는데 장르는 TMDB 사이트에서 JSON data를 그대로 복사해서 넣었는데, 영화 data를 똑같이 하기에는 무리가 있었다. 그래서, requests를 이용하여 요청을 보내서 JSON 형태로 data를 가져왔다.
  - modeling을 진행 후, data를 load 하는 과정에서 한번 더 걸림 돌이 있었다. 처음에 data를 가져올 때 생각없이 많은 부분을 가져와서 설계한 data에 맞추기 위한 작업이 필요했다. 그래서, 파이썬으로 가져왔던 data를 재정립 하는 프로그램을 작성하여 loaddate 작업을 진행하였다. data를 추출하고 우리 DB에 load 하는 작업에 하루를 쏟아 부었다. 힘들고 어려웠지만 API를 통해 data를 가져오고 DB에 load 하는 작업에 대해 많이 공부할 수 있었다.
  - accounts App 설계는 많이 해왔던 작업이여서 수월하게 했다. 다만, profile 페이지 구성하는데 있어서 user들이 프로필 이미지를 업로드 할 수 있는 기능을 구현하고 싶었는데 시간이 부족해서 하지 못했다. 시간이 나면 따로 작업해야겠다.
  - movies App 설계에서는 어떤 알고리즘을 구현할 지 많은 고민이 됬다. 처음에는 너무 많이 생각하고 잘하려고 해서 점점 산으로 갔다. 그래서, 욕심을 버리고 날짜에 따라 알아서 추천해주는 알고리즘을 우선 구현하였다. 오늘의 날짜와 월, 일 모두 같은 날에 개봉한 영화를 우선적으로 추천해주고, 없다면 일만 같은 영화, 또 없다면 월만 같은 영화를 추천하는 로직으로 설계하였다. 매우 간단하지만, 정말 별 생각 없이 아무 영화나 보고 싶을 때 나쁘지 않은 알고리즘이라고 생각한다.
  - 두 번째로 조원인 문석이가 장르 선택과 평점을 입력하여, 선택과 장르와 입력한 평점 이상의 영화들을 추천해주는 알고리즘을 설계하였다. 평점을 중요시하는 사람이면 꽤 쓸만한 추천 시스템이 될 것 같다.
  - 전체적으로 django를 이용하여 서버 단을 구현하는 과정은 많은 시행착오 없이 구현할 수 있었다. 그렇지만 눈에 보이는front 단을 구현하는데 너무 힘들었다. 시간도 부족하고 생각하는대로 되지는 않고 bootstrap을 이용하여 최선을 다하여 구현하기는 했지만 부족하다고 생각한다. web의 꽃은 front 인 것 같고, 그만큼 정말 어렵고 할 수 있는 것이 많아야 한다는 것을 느끼게 되었다. 또한, web 개발자가 되기에는 많이  부족하고 더 많은 노력이 필요하다는 생각이 들었다.
  - 최종 프로젝트를 하면서, 가장 오랫동안 팀을 이루어 협업을 진행했다. 내 생각엔 훌륭한 팀웍으로 프로젝트를 진행한 것 같다. 업무 분담 후, github을 이용하여 공동으로 진행하였고, 진행 과정에서 모르는 부분은 zoom을 통해 대화하며 해결하였다. 힘들었지만, 나름 재미도 있었고 부족하지만 처음으로 프로젝트 다운 결과물을 만들어내어 기분이 좋았다.

  

- ##### 김문석

  - TMDB의 데이터를 수집하는 것부터 난관이었다. 기존의 프로젝트들은 json형태로 주어져 loaddata만 했으면 됬었지만 TMDB사이트에서 JSON data로 가져오기위해 Python파일로 data를 원한는 형식으로 가져올 수 있도록 설계 했고 data를 추출했다. 이후에 fixures를 만들어 loaddata를 하면서 프로젝트를 시작하게 되었다.
  - 기존의 프로젝트들과 다른점이 크게 없었기 때문에 modeling에서 어려움은 없었다. 하지만 프로젝트들을 만들어 나갈수 록 원하는 기능들이 생기면서 modeling을 자주 바꾸게 되었다. 하지만 결국엔 유저들의 프로필 사진을 올리는 기능과 영화의 평점을 별점으로 표시하는 기능을 넣기에는 시간적 여유가 없었다. 배포이후 업데이트를 통해 기능을 추가해볼 생각이 있다.
  - 사실 algorithm에는 cos 유사성을 이용한 추천 알고리즘을 생각했다. 하지만 진행하면서 오류가 많았고 views.py에서 적용이 안되는 오류가 있었다. 결국 다른 알고리즘을 생각하게 되었고 앞으로의 학습 계획을 수립할 수 있게 되었다. 케글이나 AI 서적을 통해 공부하고 직접 앱에 적용하는 것들을 공부해보고 싶어졌다.
  - 알고리즘에대해 경석이형은 번뜩이는 아이디어로 date값을 받아 날짜 월 일이 같은 것을 우선적으로 추천하고 다음에는 월만 추천하는 로직을 설계했고 나는 데이터베이스에 있는 장르와 평점으로 선택하여 보여주는 알고리즘을 택했다.
  - 전반적인 PJT는 너무 좋았다. 팀워크도 좋았고 일이 진행되는것이 눈에 보일정도로 순탄했지만 가장 힘들었던 점은 github을 이용한 협업이 처음이라 많이 부딪혔다. 처음에는 branch를 몰라 찾아보고 공부하며 진행했고 도중 conflct에러가 아닌 merge조차 안되는 에러가 발생하기도 했다. 처음으로 협업다운 프로젝트여서 너무 뿌듯했다.