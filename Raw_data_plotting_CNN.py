from plotnine import ggplot, aes, geom_histogram, labs, geom_density, theme_bw

from Data_loader import CNN_df


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