#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
### Yunqiu (Julie) Li Problem Set 2

Created on Mon Oct  1 02:03:16 2018

@author: liyunqiu
"""

def costsWithSpreadGenerator(bidSpread, askSpread):
    costs = {
            'EUR': {'USD':1.2202 * (1-bidSpread)},
            'USD': {'CNY':1/(0.1557438 * (1+askSpread)),'JPY':1/(0.0092636 * (1+askSpread)),'GBP': 1/(1.3687 *(1+askSpread)), 'CAD': 1/(0.821086* (1+askSpread)), 'EUR':1/(1.2202*(1+askSpread))},
            'CNY': {'USD':0.1557438 * (1-bidSpread)},
            'GBP': {'USD': 1.3687 * (1-bidSpread)},
            'CAD': {'USD': 0.821086 * (1-bidSpread)},
            'JPY': {'USD': 0.0092636 * (1 - bidSpread)}
             }
    return costs

def dijkstraCurrencyMarket(costs, startNode, startCost):
    nodes = {'EUR', 'USD','CNY','JPY','GBP', 'CAD'}
    
    start_node = startNode
    unvisited_nodes = {node: None for node in nodes} 
    visited_nodes = {}
    current_node = start_node
    current_cost = startCost
    unvisited_nodes[current_node] = current_cost
    
    while True:
        for neighbor, cost in costs[current_node].items():
            if neighbor not in unvisited_nodes:
                continue
            new_cost = current_cost * cost
            if unvisited_nodes[neighbor] is None or new_cost < unvisited_nodes[neighbor]:
                unvisited_nodes[neighbor] = new_cost
                
        visited_nodes[current_node] = current_cost
        
        del unvisited_nodes[current_node]
        if not unvisited_nodes:
            break
        candidates = [node for node in unvisited_nodes.items() if node[1]]
        current_node,current_cost = sorted(candidates, key=lambda x: x[1])[0]
    
    
    return (visited_nodes)
def simulateExchangeForOneStartCurrency(startCurrency):
    print("current start currency is:" + startCurrency)
    for bidSpread in [0.01,0.02,0.05]:
        for askSpread in [0.01,0.02,0.05]:
            costs = costsWithSpreadGenerator(bidSpread, askSpread)
            firstRoundExchange = dijkstraCurrencyMarket(costs, startCurrency, 1)
            print("Now for bidSpread as: %4.2f and askSpread as: %4.2f" %(bidSpread,askSpread))
            for secondRoundStartNode, secondRoundStartCost in firstRoundExchange.items():
                secondRoundCosts = costsWithSpreadGenerator(bidSpread, askSpread)
                if secondRoundStartNode == (startCurrency) or secondRoundStartNode ==('USD'):
                    continue
                print("target currency is:",secondRoundStartNode)
                secondRoundExchange = dijkstraCurrencyMarket(secondRoundCosts, secondRoundStartNode, secondRoundStartCost)
                print("the amount of "+ startCurrency+" we got is:")
                print (secondRoundExchange[startCurrency])
    print("simulate for " + startCurrency + " ends here")

for currency in {'EUR', 'USD','CNY','JPY','GBP', 'CAD'}:
    if currency == 'USD':
        continue
    else:
        simulateExchangeForOneStartCurrency(currency)

print("No arbitrage found. Exchange rate of currency and type of exchanged currency will not affect the result.")

