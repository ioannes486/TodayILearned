# git 01

## ※ WARNING
1. **현재 위치를 잘 확인한다.**
2. **Repo 안에서 repo (master)를 만들지 않는다. (Master 떠있으면 `git init` X)**
3. **Home(`~`)에서 init 하지 않는다.**
4. **(지금은) github에서 직접 수정하지 않는다.**

---
## 프로젝트 초기화 진행

### 계정 세팅

```sh
# (계정당 1회) 서명이 등록되지 않았다면, 계정용 서명 등록
$ git config --global user.name '내이름'
$ git config --global user.email 'github에서@쓸메일주소'
# 서명이 정상적으로 등록되었는지 확인
$ cat ~/.gitconfig  
```

### 프로젝트 생성부터 push까지

```sh
# 프로젝트 폴더 생성
$ mkdir new_project

# 프로젝트 폴더로 이동
$ cd new_project

# README 파일 & .gitignore 생성
$ touch README.md .gitignore

# gitignore.io 에 접속하여 필요한 내용 복-붙

# 폴더를 리포로 초기화
$ git init

# README & .gitignore 파일 add(tracking)
$ git add .

# commit
$ git commit -m 'first commit'

# github에서 원격 저장소 직접 생성

# 생성한 원격 저장소 등록  (origin 은 alias - 변경 가능)
$ git remote add origin <URL>

# 등록된 저장소 확인
$ git remote -v

# 지금까지의 commit들 모아서 push
$ git push origin master
```
---

## 명령어 정리

1. 리포 초기화 시점에 1회 입력

```sh
$ git init 
```

2. 작업 후 스테이징

```sh
# 특정 파일만 add 할 때
$ git add <filename>
# 현재 폴더 전체를 add 할 때
$ git add .
```

3. 커밋 진행

```sh
# 메시지는 짧고 정확하게
$ git commit -m 'MESSAGE'
```


4. 모니터링 명령어

```sh
# 현재 Working Dir 과 Stage 상황 확인 (주기적으로 확인하자!)
$ git status

# commit 로그 
$ git log     
# commit 로그 짧게 (작업내용 확인 가능)
$ git log --oneline
```

5. github 에 원격 저장소 생성하기 (github site에서 `New Repository`)
  
6. 원격 저장소(remote repo) 추가하기

```sh
$ git remote add origin <URL>
```

7. 원격 저장소 확인하기

```sh
$ git remote -v
```

8. 원격 저장소에 지금까지의 commit 들 PUSH 하기

```sh
$ git push origin master
```

9. 새로운 컴퓨터에서 기존 원격 저장소 복제하기 (비슷한 개념: init)
```sh
$ git clone <URL>
```

10. 원격 저장소의 내용 받아오기 (다른 컴퓨터에서 사용할 때)
```sh
$ git pull origin master
```

|상황|명령어|
|--|--|
|집에서 새로운 프로젝트 시작|`$ mkdir project`|
|프로젝트 폴더로 이동|`$ cd project`|
|리포 초기화|`$ git init`|
|README, .gitignore 생성|`$ touch README.md .gitignore`|
|파일 스테이징|`$ git add .`|
|커밋|`$ git commit -m 'first commit'`|
|원격저장소 생성|github 사이트에서 진행|
|원격 저장소 등록|`$ git remote add origin <URL>`|
|원격 저장소 PUSH|`$ git push origin main`|
|다른 컴퓨터에서 원격저장소 복제|`$ git clone <URL>`|
|작업|`add`, `commit`|
|귀가 직전|`$ git push origin main`|
|집 도착 이후|`$ git pull origin main`|
|작업|`add`, `commit`|
|작업 종료|`$ git push origin main`|
|다른 컴퓨터에서 반복|`$ git pull origin main`|
