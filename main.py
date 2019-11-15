import threading
from App.Modules.Speech.sr import process
from App.server import app

t1 = threading.Thread(target=process)
t2 = threading.Thread(target=app.run)

t2.start()
t1.start()

t2.join()
t1.join()
print('done')
