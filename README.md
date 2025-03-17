# AIDD_course
materials for AIDD course

## Configure a jupyter notebook and start it
```bash
docker run -it --gpus all --name jpt_test --network=host -v /home:/home image_name:tag bash
```

in the container
```bash
pip install jupyter
```

```bash
ipython
In [1]: from IPython.lib import passwd 
In [2]: passwd() 
Enter password: 
Verify password: 
```

```bash
ipython profile create myserver
cd ~/.ipython/profile_myserver
vim ipython_notebook_config.py
```

```vim
c = get_config()
# Kernel config
c.IPKernelApp.pylab = 'inline'
# Notebook config
c.NotebookApp.ip='*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:df04061b16ebd97bacaf7f1199'# 将前面生成的密码替换掉这段字符串
c.NotebookApp.port = 8888  #设置端口号，我这里设置的是8888，可以设置成任意喜欢的
```

now start the notebook
```bash
jupyter notebook --config .ipython/profile_myserver/ipython_notebook_config.py
```

final step, find the IP address of the server
```bash
ifconfig
```

then input the IP:8888 in your local web browser (google chrome usually works better)
