#!/usr/bin/env python3
'''
Programming challenge description:
We say a portfolio matches the benchmark when the number of shares of each asset in the portfolio matches the number of shares of each asset in the benchmark. Your question is to write a program that determines the transactions necessary to make a portfolio match a benchmark.

A portfolio is a collection of assets such as stocks and bonds. A portfolio could have 10 shares of Vodafone stock, 15 shares of Google stock and 15 shares of Microsoft bonds. A benchmark is also just a collection of assets. A benchmark could have 15 shares of Vodafone stock, 10 shares of Google stock and 15 shares of Microsoft bonds.

A transaction is when you “buy” or “sell” a particular asset of certain asset type (“stock” or “bond”). For instance, you can decide to buy 5 shares of Vodafone stock which, given the portfolio described above, would result in you having 15 shares of Vodafone stock. Correspondingly, you decide to sell 5 shares of Microsoft bonds, which would result in 10 shares of Microsoft bonds in the above portfolio.

Assumptions:

Shares are positive decimals
There will always be at least 1 asset present in the Portfolio and Benchmark
A particular asset can be bond, stock, or both. For example, 5 shares of Microsoft bonds and 10 shares of Microsoft stock can both be present in the portfolio/benchmark
The trades should be sorted in alphabetical order based on the names of the assets; if both bonds and stock are present for an asset, list bonds first
Input:
The first part of the input is the Portfolio holdings (in the format Name,AssetType,Shares where each asset is separated by ‘|’ symbol)
The second part of the input is the Benchmark holdings (in the format Name,AssetType,Shares where each asset is separated by ‘|’ symbol)
Example input: Vodafone,STOCK,10|Google,STOCK,15|Microsoft,BOND,15:Vodafone,STOCK,15|Google,STOCK,10|Microsoft,BOND,15

Note that the two parts are separated by the ‘:’ symbol.

Output:
The output is a list of transactions (separated by new line) in the format TransactionType,Name,AssetType,Shares. Note that the TransactionType should only be BUY or SELL.

Example output: SELL,Google,STOCK,5 BUY,Vodafone,STOCK,5

Test 1
Test Input
Download Test 1 Input
Vodafone,STOCK,10|Google,STOCK,15|Microsoft,BOND,15:Vodafone,STOCK,15|Google,STOCK,10|Microsoft,BOND,15
Expected Output
Download Test 1 Input
SELL,Google,STOCK,5
BUY,Vodafone,STOCK,5
Test 2
Test Input
Download Test 2 Input
Vodafone,STOCK,10|Google,STOCK,15:Vodafone,STOCK,15|Vodafone,BOND,10|Google,STOCK,10
Expected Output
Download Test 2 Input
SELL,Google,STOCK,5
BUY,Vodafone,BOND,10
BUY,Vodafone,STOCK,5
'''
import bisect
def benchmark_portfolio(input):
    portfolio, benchmark = input.split(":", 1)
    portfolio = portfolio.split("|")
    benchmark = benchmark.split("|")
    d = {}
    for p in portfolio:
        name, asset, quant = p.split(",",2)
        d[name +"," + asset] = int(quant)
    for b in benchmark:
        name, asset, quant = b.split(",",2)
        if name+","+asset in d:
            d[name+","+asset] -= int(quant)
        else:
            d[name+","+asset] = -int(quant)
    output = []
    for key, val in d.items():
        name, asset = key.split(",",1)
        idx = bisect.bisect(output, name+","+asset +","+str(val))
        output[idx:idx] = [name+","+asset +","+str(val)]
    for x in output:
        name, asset, quant = x.split(",",2)
        action = "BUY"
        if int(quant) < 0:
            action = "SELL"
            quant = -int(quant)
        if int(quant) != 0:
            print("{action},{name},{asset},{quant}".format(action=action, name=name, asset=asset, quant=quant))
from collections import Counter
def benchmark_portfolio_v2(inputString):
        result = Counter()
        portfolio, benchmark = inputString.split(':')

        def processAsset(asset, mult):
            company, assetType, count = asset.split(',')
            result[f'{company},{assetType}'] += mult * int(count)

        for asset in portfolio.split('|'):
            processAsset(asset, -1)

        for asset in benchmark.split('|'):
            processAsset(asset, 1)

        return '\n'.join(
            f'{"BUY" if result[assetId] > 0 else "SELL"},{assetId},{abs(result[assetId])}'
            for assetId in sorted(result)
            if (result[assetId]) != 0
        )
#benchmark_portfolio("Vodafone,STOCK,10|Google,STOCK,15|Microsoft,BOND,15:Vodafone,STOCK,15|Google,STOCK,10|Microsoft,BOND,15")
print(benchmark_portfolio_v2("Vodafone,STOCK,10|Google,STOCK,15|Microsoft,BOND,15:Vodafone,STOCK,15|Google,STOCK,10|Microsoft,BOND,15"))
print(benchmark_portfolio_v2("Vodafone,STOCK,10|Google,STOCK,15:Vodafone,STOCK,15|Vodafone,BOND,10|Google,STOCK,10"))