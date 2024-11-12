import pandas as pd
from plotnine import (ggplot, aes, geom_histogram,
                      labs, geom_density, theme_bw,
                      xlim)
from Euclidian import distance_within_df, distance_between_df

within_density_plot = (
    ggplot(distance_within_df) +
    geom_density(aes(x='Distance'), color='black', fill='blue', alpha=0.2, bw = 0.1 ) +
    labs(title='Within distribution', x='Distance', y='Density') + xlim(0,5) +
    theme_bw()
)

max_value = distance_between_df['Distance'].max()
print(max_value)

between_density_plot = (
    ggplot(distance_between_df) +
    geom_density(aes(x='Distance'), color='black', fill='red', alpha=0.2, bw = 0.1 ) +
    labs(title='Between distribution', x='Distance', y='Density') + xlim(0,5) +
    theme_bw()
)

within_density_plot.show()

between_density_plot.show()

combined_data = pd.concat([distance_within_df,
                                  distance_between_df], ignore_index=True)
print(combined_data)

combined_density_plot = (
    ggplot(combined_data) +
    geom_density(aes(x='Distance', fill='Type'), color='black', alpha=0.2, bw=0.1) +
    labs(title='Distance Distributions', x='Distance', y='Density') + xlim(0,5) +
    theme_bw()
)

combined_density_plot.show()

