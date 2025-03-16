# Mini Trading System (MTS) Project

### 프로젝트 소개
PostgreSQL 사용법을 익히기 위한 미니 프로젝트로 <br>
HTS(Home Trading System), MTS(Mobile Trading System)에서의 기본적인 주식 거래 기능을 구현하고<br>
주식 거래 양도 차익에 대한 선입선출 방식의 계산 기능, 보유 종목에 대한 섹터별 비중 조회 등의 추가 기능을 구현

### 개발기간
2024-11-07 ~ 2024-12-08

### 개발환경
사용언어: 파이썬 (버전: 3.12.7)<br>
추가 설치 라이브러리: psycopg2, tabulate<br>
```
pip install psycopg2 
pip install tabulate
```
DBMS: PostgreSQL

### 주요 기능
누적 양도소득 계산: 매매 내역을 DB에 저장하여 매도 시 발생하는 양도소득(차익)을 선입선출 방식으로 계산하여 계좌 당 누적하여 조회 <br>
포트폴리오 비중 조회: 로그인한 계좌에서 종목별 비중이 아닌 보유 종목들의 섹터별 비중을 조회 <br>

### 개발자 정보
e-mail: newalfo1006@gmail.com
