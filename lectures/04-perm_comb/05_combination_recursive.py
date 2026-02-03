def comb(arr, n):
   result = []
   # base
   if n == 1:
      return [[elem] for elem in arr]

   for idx in range(len(arr)):
      elem = arr[idx]
      for rest in comb(arr[idx + 1:], n - 1):
          result.append([elem] + rest)

   return result



print(comb([1, 2, 3, 4], 2))  # [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] 출력
