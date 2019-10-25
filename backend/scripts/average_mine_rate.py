import time
from backend.blockchain.blockchain import Blockchain
from backend.config import SECONDS

blockchain = Blockchain()
mining_times = []

for i in range(1000):
  start = time.time_ns()
  blockchain.add_block(i)
  end = time.time_ns()

  time_to_mine = (end - start) / SECONDS
  mining_times.append(time_to_mine)

  average_time_to_mine = sum(mining_times) / len(mining_times)

  print(f'New block difficulty: {blockchain.chain[-1].difficulty}')
  print(f'Time to mine last block: {time_to_mine}s')
  print(f'Average time to mine: {average_time_to_mine}s\n')