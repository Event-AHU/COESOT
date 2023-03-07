# -*- coding:utf-8 -*-
# ! ./usr/bin/env python
# __author__ = 'zzp'

import os
import random
import argparse
import numpy as np
import matplotlib.pyplot as plt
import itertools
from os.path import join, normpath


plt.rc('font',family='Times New Roman')

parser = argparse.ArgumentParser(description='Plot VOT boc dis.')
parser.add_argument('--dataset', default='COESOT', type=str, help='Year of VOT benchmark')

eps = 1e-5


def flip(items, ncol):
    return itertools.chain(*[items[i::ncol] for i in range(ncol)])


def check_marker(marker_used, color_used, m_idx_now, c_idx_now):
    """
    :return: return '' indicate conflict
    """
    for (m, c) in zip(marker_used, color_used):
        if (m_idx_now, c_idx_now) == (m, c):
            return True

    return False


def draw_boc(args, max_nums=30, legend_cols=7, legend_rows=4):
    fig, ax = plt.subplots(figsize=(11.5, 3.5))   # set width and height     # 8, 3
    ax.set_axisbelow(True)

    Colors_style = ['r', 'gold', 'lawngreen', 'aquamarine', 'dodgerblue', 'blue', 'fuchsia']
    Maker_style = ['o', 'x', '*', 'v', 'D', '+', '<', 'p', '>', 's', '^', 'h']

    # read vot result (txt format)
    r_file = args.dataset + '_results.txt'
    fin = open(r_file, 'r')
    lines = fin.readlines()

    trackers = []
    bocs = []
    for line in lines:
        tracker, boc = line.split(':')
        boc = boc.split('\n')[0]   # remove \n
        trackers.append(tracker)
        bocs.append(float(boc))

    # reorder
    bocs = np.array(bocs)
    sort_idx = np.argsort(-bocs)  # decend
    sort_bocs = sorted(bocs, reverse=True)
    sort_trackers = [trackers[idx] for idx in sort_idx]

    # start draw
    max_nums = min(max_nums, len(trackers))
    # legend_nums = min(max_nums, legend_nums)
    sort_trackers = sort_trackers[: max_nums]
    sort_bocs = sort_bocs[: max_nums]

    print('We will draw {0} trackers for {1} benchmark'.format(max_nums, args.dataset))

    linewidth = 2.5
    scale = 150
    marker_used = []
    color_used = []

    for i, score in enumerate(sort_bocs):
        real_rank = i + 1
        fake_rank = max_nums - i
        color_idx = i % len(Colors_style)
        marker_idx = i % len(Maker_style)

        # check conflict
        while True:
            flag = check_marker(marker_used, color_used, marker_idx, color_idx)
            if not color_idx or not marker_idx or not flag:
                #  not conflict
                marker_used.append(marker_idx)
                color_used.append(color_idx)
                break
            else:
                color_idx = random.choice(np.arange(0, len(Colors_style)))
                marker_idx = random.choice(np.arange(0, len(Maker_style)))


        # some edge color=none
        # onlt ist use red hard circle
        if i == 0:
            marker_idx = 0
            color_idx = 0
        # others not use red hard circle
        if marker_idx == 0 and color_idx == 0 and not i == 0:
            marker_idx = 2
            color_idx = 1

        if Maker_style[marker_idx] in ['D']:
            scale = 130

        if Maker_style[marker_idx] in ['*', 'v', 'D', '<', 'p', '>', 's', '^', 'h']:
            if i < legend_rows * legend_cols:
                plt.scatter(fake_rank, score, marker=Maker_style[marker_idx], facecolors='none',
                            edgecolors=Colors_style[color_idx], s=scale, linewidths=linewidth, label=sort_trackers[i])
            else:
                plt.scatter(fake_rank, score, marker=Maker_style[marker_idx], facecolors='none',
                            edgecolors=Colors_style[color_idx], s=scale, linewidths=linewidth)
        else:
            if i < legend_rows * legend_cols:
                plt.scatter(fake_rank, score, marker=Maker_style[marker_idx], facecolors=Colors_style[color_idx],
                            edgecolors=Colors_style[color_idx], s=scale, linewidths=linewidth, label=sort_trackers[i])
            else:
                plt.scatter(fake_rank, score, marker=Maker_style[marker_idx], facecolors=Colors_style[color_idx],
                            edgecolors=Colors_style[color_idx], s=scale, linewidths=linewidth)

    # legend
    handles, labels = ax.get_legend_handles_labels()
    plt.legend(flip(handles, 7), flip(labels, 7), loc=9, ncol=legend_cols, bbox_to_anchor=(0.5, -0.25),
               frameon=False, labelspacing=0.7, fontsize=12)

    # ax.legend(loc='lower center', ncol=legend_cols, bbox_to_anchor=(0.5, -0.65), frameon=False)


    # x/y axis
    plt.xlim(0.5, max_nums+0.5)
    min_y = 11
    max_y = 23
    plt.yticks(np.arange(min_y, max_y, 2))
    # plt.ylim(min_y, max_y)
    x_tick = list(range(0, max_nums))     # real position [0, 5, 10...30]

    x_tick = [x_tick[x] + 1 for x in x_tick if ((x+1) % 5 - 0) < eps]
    x_labels = [max_nums - tick + 1 for tick in x_tick]  # fake/show position  [...6, 1]
    ax.set_xticks(x_tick)
    ax.set_xticklabels(x_labels)

    ax.tick_params(width=3, direction='in', labelsize=16, pad=8)

    ax.spines['top'].set_linewidth(3)
    ax.spines['right'].set_linewidth(3)
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)

    # vertical line
    x_fake = list(range(0, max_nums))
    x_fake = [max_nums - x for x in x_fake]
    for i, x in enumerate(x_fake):
        # plt.vlines(x, 0.1, sort_bocs[i], linestyles='--', linewidth=0.5, colors='grey')
        plt.axvline(x, 0, (sort_bocs[i]-min_y-0.01)/(max_y - min_y), linestyle=':', linewidth=0.4, color='grey')


    # show and plot
    plt.xlabel('Order', fontsize=16)
    plt.ylabel('BOC', fontsize=16)
    plt.title('BOC Scores Rank on {}'.format(args.dataset), fontsize=20)
    plt.grid(axis='x', linewidth=3, ls='-', c='gainsboro')
    plt.grid(axis='y', linewidth=3, ls='-', c='gainsboro')
    ax.grid(alpha=1)


    save_name1 = 'BOC_{}.png'.format(args.dataset)
    save_name2 = 'BOC_{}.pdf'.format(args.dataset)
    save_name3 = 'BOC_{}.svg'.format(args.dataset)
    plt.savefig(save_name1, bbox_inches='tight', dpi=100)
    plt.savefig(save_name2, bbox_inches='tight', dpi=100)
    plt.savefig(save_name3, bbox_inches='tight', dpi=100)
    plt.show()


if __name__ == '__main__':
    args = parser.parse_args()
    draw_boc(args)




