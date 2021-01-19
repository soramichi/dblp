# What is it
Categorize DBLP records to "1st-author papers" and "other papers"

# Prerequisites
- python (3.x)
  - urllib3
- gcl (GNU Common Lisp)
- bash

# Example
```
$ ./run.sh Soramichi Akiyama
dblp_Soramichi_Akiyama.lsp
1st-author papers:
(("Diagnosing Performance Fluctuations of High-Throughput Software for Multi-core CPUs."
  "IPDPS Workshops" (1293 1302))
 ("Quantitative Evaluation of Intel PEBS Overhead for Online System-Noise Analysis."
  "ROSS@HPDC" (1 8))
 ("Fast Live Migration for IO-Intensive VMs with Parallel and Adaptive Transfer of Page Cache via SAN."
  "IEICE Transactions" (3024 3034))
 ("Performance Prediction of Memory Access Intensive Apps with Delay Insertion: A Vision."
  "CloudCom" (492 496))
 ("Fast Live Migration with Small IO Performance Penalty by Exploiting SAN in Parallel."
  "IEEE CLOUD" (40 47))
 ("Evaluating Impact of Live Migration on Data Center Energy Saving."
  "CloudCom" (759 762))
 ("Fast Wide Area Live Migration with a Low Overhead through Page Cache Teleportation."
  "CCGRID" (78 82))
 ("MiyakoDori: A Memory Reusing Mechanism for Dynamic VM Consolidation."
  "IEEE CLOUD" (606 613))) 

Other papers:
(("Reactive NaN Repair for Applying Approximate Memory to Numerical Applications."
  "CoRR" (0 0))
 ("Towards write-back aware software emulator for non-volatile memory."
  "NVMSA" (1 6))
 ("Optimizing distributed actor systems for dynamic interactive services."
  "EuroSys" (1 15)))
```
