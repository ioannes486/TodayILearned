
# git 기초

## git의 개념과 학습 이유
- VCS (Version Control System, 버전 관리)를 할 수 있는 시스템 
- VCS를 통하여 동시 다발적인 작업이 가능하며, 수정 내역 관리 편리성 증대
### VCS란?
- VCS (Version Control System, 버전 관리): 변경사항만 저장하여 용량 간소화 및 사용자, 수정내용 등 관리
### Working Directory
- 모든 작업을 할 수 있는 디렉토리 (ex) 분장실
### Stage
- 작업이 완료된 파일이 커밋되기 전 대기할 수 있는 공간 (ex) 무대
### Commit
- staging 된 파일을 스냅샷 함 (ex) 촬영

## git 사용법
```
git init
- init (initialize): 비어있는 directory에 .git/이라는 폴더를 만들어 줌.
- repository: git이라는 프로그램이 관리를 시작한 폴더, .git/폴더가 있음
- respository → 폴더: .git/을 지우면 됨

git add
- 스테이지에 추가

git commit
- git commit -m ‘message’ 형식
- 스냅샷(사진) 찍음
- stage 전체를 찍음 (명시할 필요 X)
- 스테이징 된 상태만 커밋 가능함

git status
-변동된 사항 확인 가능 

git log
-커밋 완료된 파일 확인

git config --global user.name "name"
- git에서 사용할 user name 설정

git config --global user.email "email@com"
- git에서 사용할 user email 설정

```