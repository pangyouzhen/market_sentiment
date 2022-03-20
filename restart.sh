ps -elf | grep stream | grep -v grep | awk '{print $4}' | xargs kill -9
source venv/bin/activate && nohup streamlit run app.py &