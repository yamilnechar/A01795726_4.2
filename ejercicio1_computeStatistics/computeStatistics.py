import sys
import time

def read_numbers(file_name):
  numbers = []
  try:
    file = open(file_name, 'r')
    for line in file:
      try:
        numbers.append(float(line.strip()))
      except:
        print("Ignoring invalid value:", line.strip())
    file.close()
  except:
    print("Error: Cannot open file", file_name)
    sys.exit(1)
  return numbers

def mean(nums):
  return sum(nums)/len(nums)

def median(nums):
  nums.sort()
  n = len(nums)
  if n % 2 == 0:
    return (nums[n//2-1] + nums[n//2]) / 2
  else:
    return nums[n//2]

def mode(nums):
  freq = {}
  for num in nums:
    if num in freq:
      freq[num] += 1
    else:
      freq[num] = 1
  highest_freq = max(freq.values())
  modes = [k for k, v in freq.items() if v == highest_freq]
  return modes if len(modes) < len(nums) else None

def variance(nums, avg):
  total = 0
  for num in nums:
    total += (num - avg) ** 2
  return total / len(nums)

def stddev(var):
  return var ** 0.5

if __name__=="__main__":
  if len(sys.argv)!=2:
    print("Usage: python computeStatistics.py file.txt")
    sys.exit(1)

  file_name=sys.argv[1]
  start_time = time.time()

  numbers=read_numbers(file_name)
  
  if len(numbers)==0:
    print("Error: No valid numbers in file")
    sys.exit(1)

  avg=mean(numbers)
  med=median(numbers)
  mod=mode(numbers)
  var=variance(numbers, avg)
  std=stddev(var)

  elapsed_time = time.time() - start_time

  results=f"""
  Statistics:
  Mean: {avg}
  Median: {med}
  Mode: {mod}
  Variance: {var}
  Std Dev: {std}
  Execution Time: {elapsed_time:.5f} sec
  """

  print(results)

  result_file=open("StatisticsResults.txt","w")
  result_file.write(results)
  result_file.close()
