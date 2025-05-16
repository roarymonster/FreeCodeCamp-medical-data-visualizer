import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
#df['BMI'] = df['weight']/((df['height']/100)**2)
#df['overweight'] = (df['BMI'] > 25).astype(int)
df['overweight'] = (df['weight']/((df['height']/100)**2) > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] != 1).astype(int)
df['gluc'] = (df['gluc'] != 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = sorted(df[['cholesterol','gluc','smoke','alco','active','overweight']])


    # 6
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=df_cat)
    

    # 7
    #sns.catplot(df_cat,x='variable', col = 'cardio', kind='count', hue = 'value')
    

    # 8
    fig = sns.catplot(df_cat,x='variable', col = 'cardio', kind='count', hue = 'value')
    

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo']<=df['ap_hi']) &
                 (df['height']>=df['height'].quantile(0.025)) &
                 (df['height']<=df['height'].quantile(0.975)) &
                 (df['weight']>=df['weight'].quantile(0.025)) &
                 (df['weight']<=df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr))



    # 14
    fig, ax = plt.subplots(figsize = (8,8))

    # 15
    ax = sns.heatmap(corr,mask = mask, annot = True)


    # 16
    fig.savefig('heatmap.png')
    return fig
