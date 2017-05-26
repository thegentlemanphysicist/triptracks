# trip-planner
This project is under development. The goal is to have a unified site to manage trip plans and reports for outdoor trips.

## Setup
- pull the project: `git clone https://github.com/joram/trip-planner.git`
- install the python packages `pip install -r requirements.txt`
- build the docker container `bash ./scripts/services/start`
- migrate your database `python ./scripts/manage migrate --all`
- run the server `bash ./scripts/run`
- (optional) load in some gpx files with `python ./scripts/load/trailpeak`
- visit in the browser <a href="http://localhost:8000">localhost:8000</a>

#### notes:
- if you need to clean up space:
  - Delete all containers `sudo docker rm $(sudo docker ps -a -q)`
  - Delete all images `sudo docker rmi $(sudo docker images -q)`
  - if you really need to scrub, docker's temp folder is at `/var/lib/docker/tmp`
