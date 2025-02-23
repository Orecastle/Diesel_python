import numpy as np
from plotnine import ggplot, aes, geom_density, labs, theme_bw, scale_y_continuous, scale_x_continuous
from Data_loader import CNN_df

print(CNN_df.info())

CNN_df_sample = CNN_df.sample(1000)  # Random sample of 1,000 rows
CNN_df_sample['log_LR'] = np.log10(CNN_df_sample['LR'])  # Apply log10 transformation

density_LR = (
    ggplot(CNN_df_sample) +
    geom_density(aes(x='log_LR', fill="is_same_substances?"),
                 color='black', alpha=0.4) +
    labs(title='Density of Log10 LRs', x='Log10(LR)', y='Density') +
    scale_x_continuous(limits=(-10,10)) +
    theme_bw()
)

density_LR.show()

