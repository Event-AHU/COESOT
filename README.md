<div align="center">
 
<img src="https://github.com/Event-AHU/COESOT/blob/main/figures/COESOT.png" width="600">

 **A general and large-scale benchmark COESOT dataset for color-event based visual tracking**

 ------
 
</div>

> **[Revisiting Color-Event based Tracking: A Unified Network, Dataset, and Metric](https://arxiv.org/abs/2211.11010)**, Chuanming Tang, Xiao Wang, Ju Huang, Bo Jiang, Lin Zhu, Jianlin Zhang, Yaowei Wang, Yonghong Tian 
[[Paper](https://arxiv.org/abs/2211.11010)] 
[[DemoVideo](https://youtu.be/_ROv09rvi2k)] 
[[Project](https://sites.google.com/view/coesot/)]




### Demo Video: 
* [[YouTube](https://youtu.be/_ROv09rvi2k)]


### Dataset Download: 
```
百度网盘：  链接：https://pan.baidu.com/s/12XDlKABlz3lDkJJEDvsu9A     提取码：AHUT 
```




```Shell
├── COESOT dataset
    ├── Training Subset (827 videos, 160GB)
        ├── dvSave-2021_09_01_06_59_10
            ├── dvSave-2021_09_01_06_59_10_aps
            ├── dvSave-2021_09_01_06_59_10_dvs
            ├── dvSave-2021_09_01_06_59_10.aedat4
            ├── groundtruth.txt
            ├── absent.txt
            ├── start_end_index.txt
        ├── ... 
    ├── Testing Subset (528 videos, 105GB)
        ├── dvSave-2021_07_30_11_04_12
            ├── dvSave-2021_07_30_11_04_12_aps
            ├── dvSave-2021_07_30_11_04_12_dvs
            ├── dvSave-2021_07_30_11_04_12.aedat4
            ├── groundtruth.txt
            ├── absent.txt
            ├── start_end_index.txt
        ├── ... 
```

### COESOT_eval_toolkit
1. unzip the COESOT_eval_toolkit.zip, and open it with Matlab (over Matlab R2020).
2. add your tracking results and [baseline results (提取码：siaw)](https://pan.baidu.com/s/1YN07LHERxO31zflMUzgK4A)  in `$/coesot_tracking_results/` and modify the name in `$/utils/config_tracker.m` 

3. run `Evaluate_COESOT_benchmark_SP_PR_only.m` for the overall performance evaluation, including SR, PR, NPR.

<p align="left">
  <img width="100%" src="./figures/SRPRNPR.jpg" alt="SR_PR_NPR"/>
</p>

4. run `plot_BOC.m` for BOC score evaluation and figure plot.
5. run `plot_radar.m` for attributes radar figrue plot.

<p align="center">
  <img width="45%" src="./figures/radar1.png" alt="Radar"/><img width="55%" src="./figures/BOC_score.jpg" alt="Radar"/>
</p>

6. run `Evaluate_COESOT_benchmark_attributes.m` for attributes analysis and figure saved in `$/res_fig/`. 




# CEUTrack
A unified framework for color-event tracking. 

[[Models](https://pan.baidu.com/s/1B6VPTqoltVCgOCfceK7bTA )] 提取码：0uk0
[[Raw Results](https://pan.baidu.com/s/1ZCpz9qvrirwnyK-egFPbCg )] 提取码：zisx
[[Training logs](https://pan.baidu.com/s/12KHyJZ-X4UQu0xjsoKEPqg )] 提取码：hnim

<p align="center">
  <img width="85%" src="./figures/framework.jpg" alt="Framework"/>
</p>


Install env
```
conda create -n event python=3.7
conda activate event
bash install.sh
```

Run the following command to set paths for this project
```
python tracking/create_default_local_file.py --workspace_dir . --data_dir ./data --save_dir ./output
```

After running this command, you can also modify paths by editing these two files
```
lib/train/admin/local.py  # paths about training
lib/test/evaluation/local.py  # paths about testing
```

Then, put the tracking datasets COESOT in `./data`. 

Download pre-trained [MAE ViT-Base weights](https://dl.fbaipublicfiles.com/mae/pretrain/mae_pretrain_vit_base.pth) and put it under `$/pretrained_models`

Download the model weights and put it on `$/output/checkpoints/train/ceutrack`


## Train & Test & Evaluation
```
    # train
    export CUDA_VISIBLE_DEVICES=0
    python tracking/train.py --script ceutrack --config ceutrack_coesot  \
    --save_dir ./output --mode multiple --nproc_per_node 1 --use_wandb  0
    # test
    python tracking/test.py   ceutrack ceutrack_coesot --dataset coesot --threads 4 --num_gpus 1
    # eval
    python tracking/analysis_results.py --dataset coesot  --parameter_name ceutrack_coesot
```




### Test FLOPs, and Speed
*Note:* The speeds reported in our paper were tested on a single RTX 3090 GPU.

```
# Profiling ceutrack_coesot
python tracking/profile_model.py --script ceutrack --config ceutrack_coesot
```

## TODO List 
- [x] Paper (arXiv) release
- [x] COESOT dataset release
- [x] Evaluation Toolkit release
- [x] Source Code release
- [x] Tracking Models release



### Acknowledgments
* Thanks for the [OSTrack](https://github.com/botaoye/OSTrack), [PyTracking](https://github.com/visionml/pytracking) and [ViT](https://github.com/rwightman/pytorch-image-models) library for a quickly implement.


### Citation: 
```bibtex
@article{tang2022coesot,
  title={Revisiting Color-Event based Tracking: A Unified Network, Dataset, and Metric},
  author={Tang, Chuanming and Wang, Xiao and Huang, Ju and Jiang, Bo and Zhu, Lin and Zhang, Jianlin and Wang, Yaowei and Tian, Yonghong},
  journal={arxiv pre-print arXiv:2211.11010}, 
  year={2022}
}
```


