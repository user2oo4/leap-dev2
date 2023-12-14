import random
import dimod
import dwave.inspector
import csv
import math
import dwave_networkx as dnx
import networkx as nx
import time
from dwave.cloud import Client
from dwave.system import DWaveSampler, EmbeddingComposite, LazyFixedEmbeddingComposite
from dimod.binary.binary_quadratic_model import BinaryQuadraticModel
from dimod.vartypes import SPIN
from minorminer import find_embedding
from dwave.embedding.chain_strength import uniform_torque_compensation as UTC
from dwave.embedding import embed_bqm, unembed_sampleset, EmbeddedStructure
from functools import partial
from copy import deepcopy

from dwave.samplers import SimulatedAnnealingSampler
SASampler = SimulatedAnnealingSampler()
CSampler = DWaveSampler(solver={'topology__type': 'pegasus'})

hw = dnx.chimera_graph(16,16)

class FakeChimeraSampler(dimod.Sampler, dimod.Structured):
    @property
    def properties(self) -> dict[str, any]:
        return SASampler.properties
    
    
    @property
    def parameters(self) -> dict[str, any]:
        return SASampler.parameters
    
    @property
    def nodelist(self):
        return hw.nodes.keys()
    
    
    @property
    def edgelist(self):
        return hw.edges.keys()
    
    def sample(self, bqm, **parameters):
        return SASampler.sample(bqm, **parameters)

FCSampler = FakeChimeraSampler()

# parameters

DEF_D: float = 0.01
DEF_SIGMA: float = 0.1
DEF_BETA: float = 0.01
DEF_NS: int = 50 # can change this to 10, 20, 50
DEF_LOOP: int = 4
DEF_PASS: float = 4 * (1.0 / (DEF_SIGMA * DEF_SIGMA)) * math.log(1.0 / DEF_BETA)

DEF_LB: float = 0.002
DEF_UB: float = 0.1
DEF_BS_RUNS: int = 15

DEF_STEP: float = 0.032
DEF_TRIES: int = 10
DEF_SPLIT: int = 4
DEF_ROUNDING: float = 0.1

print('reading parameters')

param: str = input()
if param != "default":
    DEF_D = int(param)
param: str = input()
if param != "default":
    DEF_SIGMA = int(param)
param: str = input()
if param != "default":
    DEF_BETA = int(param)
param: str = input()
if param != "default":
    DEF_NS = int(param)
param: str = input()
if param != "default":
    DEF_LOOP = int(param)
param: str = input()
if param != "default":
    DEF_PASS = int(param)
param: str = input()
if param != "default":
    DEF_LB = int(param)
param: str = input()
if param != "default":
    DEF_UB = int(param)
param: str = input()
if param != "default":
    DEF_BS_RUNS = int(param)
param: str = input()
if param != "default":
    DEF_STEP = int(param)
param: str = input()
if param != "default":
    DEF_TRIES = int(param)
param: str = input()
if param != "default":
    DEF_SPLIT = int(param)
param: str = input()
if param != "default":
    DEF_ROUNDING = int(param)

print('reading input')

iname: str = input()

n = int(input())

maxW = 0

model = BinaryQuadraticModel(vartype=SPIN)

for i in range(n):
    model.set_linear(i,int(input()))

while(True):
    line = (input())
    listt = line.split(' ')
    # print(line)
    # print(listt)
    temp = list(map(int,listt))
    if (temp == [-1]):
        break
    # print(temp)
    u,v,a = temp
    model.set_quadratic(u,v,a)
    maxW = max(maxW, a)

optimal_solution = int(input())


print(f'Optimal solution: {optimal_solution}')
print("maxW = ", maxW)



EPS = 1e-9
cached : dict = {}

def fe(S, T, **kwargs):
    return find_embedding(S, T, random_seed=123123)

FC_Composite = LazyFixedEmbeddingComposite(FCSampler, find_embedding=fe)
C_Composite = LazyFixedEmbeddingComposite(CSampler, find_embedding=fe)

def compute(j: float, composite: dimod.Sampler, runs: int) -> dict[str,float]:
    # print('Final run:')
    # print(f'strength: {j}')

    sample_set = composite.sample(model, num_reads = runs, chain_strength = j)

    s1_cnt: float = 0
    s2_cnt: float = 0
    ncb_cnt: float = 0
    best: float = 0

    for r in sample_set.record:           
        if ( r.energy < optimal_solution * 1 + EPS):
            s1_cnt += r.num_occurrences
                                
        if ( r.energy < optimal_solution * 0.97 + EPS):
            s2_cnt += r.num_occurrences
        if (r.energy < best):
            best = r.energy
        ncb_cnt += r.chain_break_fraction

    res: dict[str,float] = {}
    res['0no'] = s1_cnt / runs # success_probability
    res['3no'] = s2_cnt / runs
    res['break'] = ncb_cnt / runs
    res['best'] = best
    # print(res)
    return res



def get_d(j: float, delta: float) -> float:
    f1 = compute(j + delta / 2, FC_Composite, DEF_NS)['break'] * DEF_NS * n
    f2 = compute(j - delta / 2, FC_Composite, DEF_NS)['break'] * DEF_NS * n
    cntloop = DEF_LOOP #Avoid long loop, 10 means maximum of 1000 runs

    while (abs(f1 - f2) < DEF_PASS * DEF_D or min(f1, f2) < DEF_PASS * DEF_D) and cntloop > 0:
        f1 += compute(j + delta / 2, FC_Composite, DEF_NS)['break'] * DEF_NS * n
        f2 += compute(j + delta / 2, FC_Composite, DEF_NS)['break'] * DEF_NS * n
        cntloop -= 1

    return math.log(f1 / f2) / delta



def get_cs_range(lb: float, ub: float) -> tuple:
    start_low = 0.01
    start_high: float = 2 * UTC(model)
    res_lb : float = 0
    res_ub : float = 0
    l: float = 0
    r: float = 0
    
    l = start_low
    r = start_high
    for i in range(DEF_BS_RUNS):
        mid = (l+r)/2
        if (compute(mid, FC_Composite, 200)['break'] < lb):
            r = mid
        else:
            l = mid
    res_lb = (l+r)/2
    
    
    l = start_low
    r = start_high
    for i in range(DEF_BS_RUNS):
        mid = (l+r)/2
        if (compute(mid, FC_Composite, 200)['break'] < ub):
            r = mid
        else:
            l = mid
    res_ub = (l+r)/2
    print(f'result: {res_lb}, {res_ub}')
    return (res_lb, res_ub)


def hill_climb(lb: float, ub: float) -> list[float]:
    result: list[point] = []
    while len(result) < DEF_TRIES:
        point = random.random()*(ub-lb)/DEF_SPLIT+lb+(ub-lb)/DEF_SPLIT*(len(result)%DEF_SPLIT)
        # while True:
        #     point = random.random()*(ub-lb)+lb
        #     if (compute(point, FCSampler, 200)['avg'] < optimal_solution * 0.65):
        #         break

        while True:
            stop = True
            u = DEF_STEP * (ub-lb)
            if get_d(point, DEF_D*(ub-lb)) < get_d(point + u, DEF_D*(ub-lb)):
                point += u
                stop = False
                break
            if get_d(point, DEF_D*(ub-lb)) < get_d(point - u, DEF_D*(ub-lb)):
                point -= u
                stop = False
                break
            if (stop):
                break
        stop = False
        for g in result:
            if (abs(g-point) <= DEF_ROUNDING):
                stop = True
        if (not stop):
            result.append(point)
    return result

start_time = time.time()

cs_range = get_cs_range(DEF_LB, DEF_UB)

result = hill_climb(max(cs_range[1], maxW), cs_range[0])
result.sort()
print(result)

running_time = time.time() - start_time

f = open(f'runtime/findgap_runtime_{DEF_NS}_{DEF_LOOP}.csv', mode='a')
print(f'Run time: {running_time} seconds')
f.write(f'{iname},{running_time}\n')
f.close()

sus: float = UTC(model)

def output(j):
    print(j)
    print(j/sus)
    u = compute(j, C_Composite, 1000)
    print(u)
    f.write(f'{j},{j/sus},{u["0no"]},{u["3no"]},{u["best"]},{u["avg"]},{u["break"]}\n')

final_result: dict[int, float] = {}
compute_result: dict[float, dict] = {}

for cs in result:
    u = compute(cs, C_Composite, 1000)
    final_result[u["0no"] * 1000] = cs
    compute_result[cs] = u

keys = list(final_result.keys())
keys.sort()
print(keys)
sorted_final_result = {i: final_result[i] for i in keys}

print(sorted_final_result)

result = list(sorted_final_result.values())

cs = result[len(result) - 1]
u = compute_result[cs]
u['TTS'] = math.log(1 - 0.99) / math.log(1 - u['0no']) * (20 * 1000 + 1000) / 1000
u['optimality_gap'] = 1 - u["best"]/optimal_solution

f = open(f'results/findgap_results_{DEF_NS}_{DEF_LOOP}/{iname}.csv', 'w', encoding='utf-8')
f.write(f'{cs}, {running_time}, {u["optimality_gap"]}, {u["0no"]}, {u["3no"]}, {u["TTS"]}')
f.write(f'Run time: {running_time} seconds\n')
f.write(f'Chain strength: {cs}\n')
f.write(f'Optimality gap: {u["optimality_gap"]}\n')
f.write(f'Success probability: {u["0no"]}\n')
f.write(f'3% probability: {u["3no"]}\n')
f.write(f'Time to solution: {u["TTS"]} seconds\n')
f.close()

f = open(f'results/all_results', mode='a')
f.write(f'{iname},{DEF_NS}_{DEF_LOOP},{cs},{running_time},{u["optimality_gap"]},{u["0no"]},{u["3no"]},{u["TTS"]}\n')
f.close()

print(UTC(model))   
