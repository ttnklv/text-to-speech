## -*- coding: utf-8 -*-
import subprocess
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue

#subprocess.call("python listen_GUI.py", shell=True)
#subprocess.call("python listen_GUI.py", shell=True)

def execute(queue):
    proc = Popen("python listen_GUI.py", shell=True, stdout=PIPE)
    proc.wait()
    # дождаться выполнения
    queue.put(proc.communicate()[0])
    ## получить то, что вернул подпроцесс
allProcesses = []
queue = Queue()
for i in xrange(10):
    p = Process(target=execute, args=(queue,))
    allProcesses.append(p)
    p.start()

for p in allProcesses:
    p.join()

for i in xrange(queue.qsize()):
    print queue.get()
# voiceRecording

