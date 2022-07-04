
from pyecharts.charts import Map
import pandas as pd
from pyecharts import options as opts

df = pd.read_csv('./pneumoniaView/data.csv' ,encoding='utf-8')
# print(df)

china_map = (
    Map()
    .add('现有确诊',[list(i) for i in zip(df['area'].values.tolist(),df['curConfirm'].values.tolist())],'china')
    .set_global_opts(
        title_opts=opts.TitleOpts(title='各地区确诊人数'),
        visualmap_opts = opts.VisualMapOpts(max_=200, is_inverse=True)
    )
)
china_map.render('demo.html')