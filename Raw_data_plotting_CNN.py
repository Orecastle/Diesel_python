from plotnine import ggplot, aes, geom_histogram, labs, geom_density, theme_bw
import sys
sys.path.append('D:\Python\Diesel\Diesel_python')
from Data_loader import CNN_df

from Data_loader import CNN_df

CNN_df['is_same_substances?'] = CNN_df['is_same_substances?'].astype(str)

print(CNN_df.info())

histogram_LR = (
    ggplot(CNN_df) +
    geom_histogram(aes(x='LR', fill = "is_same_substances?"),
                   binwidth=0.05, color='black',
                   size=0.1 , alpha = 0.4)  +
    labs(title='Histogram of LRs', x='Values', y='Frequency')+
    theme_bw()
)

histogram_LR.show()