prompt = """<div class="col-xs-11 paper-box">
    <div class="col-xs-6 container">
        <div class="child">
            <img src="./pictures/model/(picture_name).png" style="max-height:300px;max-width: 100%;">
        </div>
    </div>
    <div class="col-xs-6">
        <a href="(Source code URL)"><b style="font-size: 22px;">
                (Model name)</b></a><br>
        (Source code description)
    </div>
</div>
"""

prompt_no_code = """<div class="col-xs-11 paper-box">
    <div class="col-xs-6 container">
        <div class="child">
            <img src="./pictures/model/(picture_name).png" style="max-height:300px;max-width: 100%;">
        </div>
    </div>
    <div class="col-xs-6">
        (Model name)<br>
        (Source code description)
    </div>
</div>
"""
import os
import pandas as pd
count = 0
data = pd.read_csv('NLP.csv')
for i in range(len(data)-1, 0, -1):
    picture_name = data['Model name'][i][:15].strip().replace(' ', '_').replace('-', '').replace(':', '_').replace('\n', '').replace('—', '')
    model_name = data['Model name'][i]
    source_code_url = data['Source code URL'][i]
    source_code_description = data['Source code description'][i]
    # print(i+1, picture_name)
    count += 1
    if "https" not in str(source_code_url) :
        # print(prompt_no_code.replace('(picture_name)', picture_name).replace('(Model name)', model_name).replace('(Source code description)', source_code_description))
        # print(model_name)
        continue
    else:
        print(prompt.replace('(picture_name)', picture_name).replace('(Model name)', model_name).replace('(Source code URL)', source_code_url).replace('(Source code description)', source_code_description))
# print(count)