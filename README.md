# data-science

cd into dd-perf
run once `docker build --no-cache -t dd-perf .`

run once `docker run -v $(PWD)/main/:/main -it dd-perf bash`

once in bash run `python main/run.py`