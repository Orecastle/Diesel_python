
from plotnine import ggplot, aes, geom_histogram, labs, geom_density, theme_bw
from Data_loader import diesel_df

histogram_uni = (
    ggplot(diesel_df) +
    geom_histogram(aes(x=diesel_df['R2']),binwidth=0.05, color='black',
                   size=0.1 , fill='red', alpha = 0.4) +
    labs(title='Histogram of ratios', x='Values', y='Frequency')+
    theme_bw()
)

histogram_uni.show()

histogram = (
    ggplot(diesel_df) +
    geom_histogram(aes(x=diesel_df['R1']),binwidth=0.05, color='black',
                   size=0.1 , fill='blue', alpha = 0.4) +
    geom_histogram(aes(x=diesel_df['R2']),binwidth=0.05, color='black',
                   size=0.1 , fill='red', alpha = 0.4) +
    labs(title='Histogram of ratios', x='Values', y='Frequency')+
    theme_bw()
)

histogram.show()

density_plot = (
    ggplot(diesel_df) +
    geom_density(aes(x='R1'), color='blue', fill='blue', alpha=0.2, bw = 0.1 ) +
    geom_density(aes(x='R2'), color='red', fill='red', alpha=0.2, bw = 0.1) +
    labs(title='Density Plot of Ratios', x='Values', y='Density') +
    theme_bw()
)

# Display the plot
density_plot.show()

