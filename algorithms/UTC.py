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

running_time = 0

sus: float = UTC(model)

cs = sus
u = compute(cs, C_Composite, 1000)
if u['0no'] != 0:
    u['TTS'] = math.log(1 - 0.99) / math.log(1 - u['0no']) * (20 * 1000 + 1000) / 1000
else:
    u['TTS'] = 1000000000
u['optimality_gap'] = 1 - u["best"]/optimal_solution
f = open(f'results/all_results', mode='a')
f.write(f'{iname},dwave,{cs},{running_time},{u["optimality_gap"]},{u["0no"]},{u["3no"]},{u["TTS"]}\n')
f.close()

f = open(f'results/findgap_results_dwave/{iname}.csv', 'w', encoding='utf-8')
f.write(f'{cs}, {running_time}, {u["optimality_gap"]}, {u["0no"]}, {u["3no"]}, {u["TTS"]}')
f.write(f'Run time: {running_time} seconds\n')
f.write(f'Chain strength: {cs}\n')
f.write(f'Optimality gap: {u["optimality_gap"]}\n')
f.write(f'Success probability: {u["0no"]}\n')
f.write(f'3% probability: {u["3no"]}\n')
f.write(f'Time to solution: {u["TTS"]} seconds\n')
f.close()



print(UTC(model))   
