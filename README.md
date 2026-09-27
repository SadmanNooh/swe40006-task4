Folder	Level	What it is
01-hello	4.1	Commands used to check Docker with ‘hello-world’
02-deadline-web	4.2	Flask page showing my SWE40006 deadlines
03-study-board	4.3	Flask study group board with an optimised Dockerfile, hosted on Azure Container Apps
04-grade-check	4.4	Script that reads my marks from a CSV and works out what I need on the rest of the unit
Md Sadman Isfar, 103849251

	
Run
bash
docker run -d -p 8080:5000 sadmannooh/deadline-web:1.0
docker run -d -p 8000:8000 -e APP_TITLE="SWE40006 Study Board" sadmannooh/study-board:1.0
docker run -v "$PWD/04-grade-check/data:/data" sadmannooh/grade-check:1.0
