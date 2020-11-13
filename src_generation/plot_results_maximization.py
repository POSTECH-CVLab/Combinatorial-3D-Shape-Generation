import numpy as np
import matplotlib.pyplot as plt
import os

import constants

list_str_exp = [
    'maximize_height',
    'maximize_width',
    'maximize_depth',
    'maximize_contacts',
]

if __name__ == '__main__':
    for str_exp in list_str_exp:
        path_results = os.path.join(constants.PATH_RESULTS, str_exp)
        list_files = os.listdir(path_results)
        print(len(list_files))

        scores_random = []
        scores_randomeval = []
        scores_bo = []

        for str_file in list_files:
            path_file = os.path.join(path_results, str_file)

            results = np.load(path_file, allow_pickle=True)
            results = results[()]

            scores = np.array(results['list_scores'])
            scores *= -1.0
            print(scores)

            if 'random_' in str_file:
                scores_random.append(scores)
            elif 'randomeval_' in str_file:
                scores_randomeval.append(scores)
            elif 'bo_' in str_file:
                scores_bo.append(scores)
            else:
                raise ValueError

        scores_random = np.array(scores_random)
        scores_randomeval = np.array(scores_randomeval)
        scores_bo = np.array(scores_bo)

        scores_random = np.concatenate((np.zeros((scores_random.shape[0], 1)), scores_random), axis=1)
        scores_randomeval = np.concatenate((np.zeros((scores_randomeval.shape[0], 1)), scores_randomeval), axis=1)
        scores_bo = np.concatenate((np.zeros((scores_bo.shape[0], 1)), scores_bo), axis=1)

        if str_exp == 'maximize_height':
            scores_oracle = np.arange(0, scores_bo.shape[1])
        elif str_exp == 'maximize_width':
            scores_oracle = 3.0 * np.arange(0, scores_bo.shape[1]) - np.concatenate(([0], np.ones((scores_bo.shape[1] - 1))), axis=0)
        elif str_exp == 'maximize_depth':
            scores_oracle = 4.0 * np.arange(0, scores_bo.shape[1]) - np.concatenate(([0], np.arange(0, scores_bo.shape[1] - 1)), axis=0)
        elif str_exp == 'maximize_contacts':
            scores_oracle = np.arange(0, scores_bo.shape[1] - 1) * 8.0
            scores_oracle = np.concatenate(([0], scores_oracle), axis=0)

        scores_oracle = np.tile(scores_oracle, (scores_bo.shape[0], 1))

        print(scores_random.shape)
        print(scores_randomeval.shape)
        print(scores_bo.shape)
        print(scores_oracle.shape)

        scores = np.array([
            scores_oracle,
            scores_random,
            scores_randomeval,
            scores_bo,
        ])

        list_str_labels = [
            r'\textrm{Oracle}',
            r'\textrm{Random}',
            r'\textrm{Random w/ Eval.}',
            r'\textrm{BO}',
        ]
    
        print(scores.shape)

        plt.rc('text', usetex=True)
        fig = plt.figure(figsize=(8, 7))
        ax = plt.gca()
        size_font = 24
        range_shade = 1.96

        ax.set_xlabel(r'\textrm{\#Primitives}', fontsize=size_font)
        ax.tick_params(labelsize=20)

        for ind_scores, cur_scores in enumerate(scores):
            mean_min = np.mean(cur_scores, axis=0)
            std_min = np.std(cur_scores, axis=0)

            print('mean', mean_min)
            print('std', std_min)

            x_data = range(0, mean_min.shape[0])
            y_data = mean_min
            std_data = std_min
            ax.plot(x_data, y_data,
                label=list_str_labels[ind_scores],
                linewidth=4,
                marker='None'
            )

            ax.fill_between(x_data,
                y_data - range_shade * std_data,
                y_data + range_shade * std_data,
                alpha=0.3
            )

        ax.set_xlim([0, np.max(x_data)])

        if str_exp == 'maximize_height':
            ax.set_ylim([0, np.max(x_data)])
            ax.set_ylabel(r'\textrm{Height}', fontsize=size_font)
        elif str_exp == 'maximize_width':
            ax.set_ylim([0, 100])
            ax.set_ylabel(r'\textrm{Width}', fontsize=size_font)
        elif str_exp == 'maximize_depth':
            ax.set_ylim([0, 100])
            ax.set_ylabel(r'\textrm{Depth}', fontsize=size_font)
        elif str_exp == 'maximize_contacts':
            ax.set_ylim([0, 250])
            ax.set_ylabel(r'\textrm{\#Connected studs}', fontsize=size_font)

        plt.grid(True)
        plt.legend(loc='upper left', fancybox=False, edgecolor='black', fontsize=22)

        plt.savefig('../figures/{}.pdf'.format(str_exp), format='pdf', transparent=True, bbox_inches='tight')
        plt.show()
