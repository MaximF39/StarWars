import time
start = time.time()
import uuid
for i in range(200):
    uuid.uuid4()

end = time.time()
print(end - start)