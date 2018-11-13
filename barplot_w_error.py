# Configure plot 
error_cfg = dict(ecolor='black',alpha=.6, lw=1, capsize=7, capthick=1)

n_groups = 2

compet_means = (data_low_compet.compet.mean(), data_low_cooper.compet.mean())
compet_std = (data_low_compet.compet.std(), data_low_cooper.compet.std())

cooper_means = (data_low_compet.cooper.mean(), data_low_cooper.cooper.mean())
cooper_std = (data_low_compet.cooper.std(), data_low_cooper.cooper.std())

fig, ax = plt.subplots(figsize=(8,6))

index = np.arange(n_groups)
bar_width = 0.4

rects1 = ax.bar(index, compet_means, bar_width,
                yerr=compet_std, error_kw=error_cfg,
                label='Competitive choice', color='#008fd5')

rects2 = ax.bar(index + bar_width, cooper_means, bar_width,
                yerr=cooper_std, error_kw=error_cfg,
                label='Cooperative choice', color='#88d0f7')

ax.set_xlabel('Feedback', fontsize=14, alpha=.5)
ax.set_ylabel('Mean rank', fontsize=14, alpha=.5)
ax.set_title('Low level group')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Competitive', 'Cooperative'))
ax.set_ylim(1,11)
ax.legend()

fig.tight_layout()
plt.show()
