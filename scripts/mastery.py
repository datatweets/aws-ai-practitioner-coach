#!/usr/bin/env python3
"""Update a simple AIF-C01 mastery state from answer events.

Usage:
  python scripts/mastery.py state.yaml events.json > updated-state.yaml

events.json example:
[
  {"domain":"D3", "concepts":["rag","fine-tuning"], "correct":false, "confidence":"sure"}
]
"""
import sys, json, yaml
from pathlib import Path

def clamp(x): return max(0.05, min(0.95, x))

def update(value, correct, confidence):
    # Small, interpretable EWMA-style update; confident mistakes penalize more.
    delta = 0.08 if correct else -0.10
    if confidence == 'sure' and not correct: delta -= 0.04
    if confidence == 'guess' and correct: delta -= 0.02
    return clamp(value + delta)

def main():
    if len(sys.argv)!=3:
        raise SystemExit('usage: mastery.py state.yaml events.json')
    state=yaml.safe_load(Path(sys.argv[1]).read_text())
    events=json.loads(Path(sys.argv[2]).read_text())
    for e in events:
        d=e['domain']; ok=bool(e['correct']); conf=e.get('confidence','unsure')
        state['answered_total']=state.get('answered_total',0)+1
        state['correct_total']=state.get('correct_total',0)+(1 if ok else 0)
        state.setdefault('confidence_counts',{}).setdefault(conf,0)
        state['confidence_counts'][conf]+=1
        dm=state.setdefault('domain_mastery',{}).get(d,0.5)
        state['domain_mastery'][d]=round(update(dm,ok,conf),3)
        cm=state.setdefault('concept_mastery',{})
        for concept in e.get('concepts',[]):
            cm[concept]=round(update(cm.get(concept,0.5),ok,conf),3)
        if not ok and e.get('misconception'):
            mis=state.setdefault('misconceptions',[])
            if e['misconception'] not in mis: mis.append(e['misconception'])
    print(yaml.safe_dump(state,sort_keys=False,allow_unicode=True))

if __name__=='__main__': main()
