# In "PancakeSwap: Factory v2" contact - getPair methog


token0 = '0x55d398326f99059ff775485246999027b3197955'
token1 = '0x23ce9e926048273ef83be0a3a8ba9cb6d45cd978'

dec0 = 18
dec1 = 18

res0 = 8733948
res1 = 7821803214644692429

if token0 < token1:
    print('swapped!')
    res0, res1 = res1, res0

res = (res0/ 10**dec0) / (res1/10**dec1)

print(res)
