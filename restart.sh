ps -elf | grep stream | grep -v grep | awk '{print $4}' | xargs kill -9
# export PYTHONPATH=$PYTHONPATH:/data/project/data-storyteller/
source venv/bin/activate && nohup python ./crawler_sts/sts.py > /dev/null 2>&1 &
source venv/bin/activate && nohup streamlit run app.py &