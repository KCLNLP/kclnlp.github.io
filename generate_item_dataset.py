prompt = """<div class="col-xs-11 paper-box">
    <div class="col-xs-6 container">
        <div class="child">
            <img src="./pictures/model/(picture_name).png" style="max-height:300px;max-width: 100%;">
        </div>
    </div>
    <div class="col-xs-6">
        <a href="(Dataset URL link)"><b style="font-size: 22px;">
                (Dataset Name)</b></a><br>
        (Dataset description)
    </div>
</div>
"""

import os
import pandas as pd
count = 0
data = pd.read_csv('NLP.csv')
for i in range(len(data)-1, 0, -1):
    picture_name = data['Model name'][i][:15].strip().replace(' ', '_').replace('-', '').replace(':', '_').replace('\n', '').replace('—', '')
    dataset_name = data['Dataset Name'][i]
    dataset_url = data['Dataset URL link'][i]
    dataset_description = data['Dataset description'][i]
    # print(i+1, picture_name)
    if type(dataset_url) is str:
        print(prompt.replace('(picture_name)', picture_name).replace('(Dataset Name)', dataset_name).replace('(Dataset URL link)', dataset_url).replace('(Dataset description)', dataset_description))
        count += 1
print(count)