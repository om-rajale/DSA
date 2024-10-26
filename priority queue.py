Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import queue
>>> q = queue.PriorityQueue()
>>> q.put(90)
>>> q.put(45)
>>> q.put(32)
>>> q.put(45)
>>> q.put(33)
>>> q
<queue.PriorityQueue object at 0x00000253E8419070>
>>> q.get()
32
>>> q.get()
33
>>> q.get()
45
>>> q.get()
45
>>> q.get()
90
>>> q.get()

