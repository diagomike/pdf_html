from JsonUtils import *
from datetime import datetime

# the only one made to use '/' in filename as hierarchy to prev in the .md obsidian data
def get_month_year(date_string):
    date = datetime.strptime(date_string, '%Y-%m-%d')
    month = date.strftime('%B')
    return f'{date.year}/{month}'


all_rhapha = loadJson('run/alldata')
sum_cue = {}
for rhapha in all_rhapha.keys():
    title_id = all_rhapha[rhapha]['title'],all_rhapha[rhapha]['id']
    key = get_month_year(rhapha)
    if (f'{key}/Cues' not in sum_cue.keys()):
        sum_cue[f'{key}/Cues'] = {'name':f'{key}/Cues'};sum_cue[f'{key}/Summary'] = {'name':f'{key}/Summary'}
    sum_cue[f'{key}/Cues']['body'] = sum_cue[f'{key}/Cues'].get('body', '') + f'[[{rhapha}#{title_id[0]}]] ^{title_id[1]}\n\n'
    sum_cue[f'{key}/Summary']['body'] = sum_cue[f'{key}/Summary'].get('body', '') + f'[[{rhapha}#{title_id[0]}]] ^{title_id[1]}\n\n'

saveJson('to_obs/sum_cue',sum_cue)