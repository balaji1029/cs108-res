'''Import required modules'''
import json

with open('../evaluate.json','w',encoding='utf-8') as f:
    json.dump({'comment': 'No auto-evaluation for this lab. Only SAFE quiz.'},f,indent=4)