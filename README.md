# COESOT 
A large-scale benchmark dataset for color-event based visual tracking 
[Revisiting Color-Event based Tracking: A Unified Network, Dataset, and Metric](https://arxiv.org/abs/).



## TODO List 
- [x] Paper (arXiv) release (2022-12-01)
- [x] COESOT dataset release (2022-12-01)
- [x] Evaluation Toolkit release (2022-12-01)
- [x] Source Code release (2022-12-01)
- [x] Tracking Models release (2022-12-01)


### Demo Video: 
* [[YouTube](https://youtu.be/_ROv09rvi2k)]


### Dataset Download: 
* [[Baidu](xxx)] 
* [[Googledrive](xxx)] 


```Shell
├── COESOT dataset
    ├── Training Subset
        ├── Video1
            ├── color_frames
            ├── event_frames
            ├── xxx.aedat4
            ├── groundtruth.txt
            ├── absent.txt
        ├── ... 
    ├── Testing Subset
        ├── Video1
            ├── color_frames
            ├── event_frames
            ├── xxx.aedat4
            ├── groundtruth.txt
            ├── absent.txt
        ├── ... 
```

### COESOT_eval_toolkit
1. unzip the COESOT_eval_toolkit.zip, and open it with matlab (over R2020).
2. add your tracking results in `$/coesot_tracking_results/` and modify the name in `$/utils/config_tracker.m` 
3. run `Evaluate_COESOT_benchmark_SP_PR_only.m` for the overall performance evaluation, including SR, PR, NPR

<p align="center">
  <img width="85%" src="https://github.com/Event-AHU/COESOT/EFUTrack/blob/main/figure/SRPRNPR.png" alt="SR_PR_NPR"/>
</p>

4. run `plot_BOC.m` for BOC score evaluation and figure plot.

5. run `Evaluate_COESOT_benchmark_attributes.m` for 17 attributes analysis and figure saved in `$/res_fig/`
6. run `plot_radar.m` for attributes radar figrue plot.

<p align="center">
  <img width="85%" src="https://github.com/Event-AHU/COESOT/EFUTrack/blob/main/figure/Radar.png" alt="Radar"/>
</p>





## EFUTrack

### Environment: 



# EFUTrack

[[Models]()]
[[Raw Results]()]
[Training logs]()]

<p align="center">
  <img width="85%" src="https://github.com/COESOT/EFUTrack/blob/main/assets/framework.png" alt="Framework"/>
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

Download pre-trained [MAE ViT-Base weights](https://dl.fbaipublicfiles.com/mae/pretrain/mae_pretrain_vit_base.pth) and put it under `$PROJECT_ROOT$/pretrained_models`

Download the model weights from [Google Drive]()
Put the downloaded weights on `EFUTrack/output/checkpoints/train/efutrack`


## Train & Test  & Evaluation
```
    # train
    export CUDA_VISIBLE_DEVICES=0
    python tracking/train.py --script ostrack --config vitb_256_mae_ce_32x4_coesot_ep100  \
    --save_dir ./output --mode multiple --nproc_per_node 1 --use_wandb  0
    # test
    python tracking/test.py   ostrack vitb_256_mae_ce_32x4_coesot_ep100 --dataset coesot --threads 20 --num_gpus 1
    # eval
    python tracking/analysis_results.py --dataset coesot  --parameter_name vitb_256_mae_ce_32x4_coesot_ep100
```


### Test FLOPs, and Speed
*Note:* The speeds reported in our paper were tested on a single RTX 3090 GPU.

```
# Profiling vitb_256_mae_ce_32x4_coesot_ep100
python tracking/profile_model.py --script efutrack --config vitb_256_mae_ce_32x4_coesot_ep100
```




### Acknowledgments
* Thanks for the [OSTrack](https://github.com/botaoye/OSTrack) and [PyTracking](https://github.com/visionml/pytracking) library 


### Citation: 
```bibtex
@article{tang2022coesot,
  title={Revisiting Color-Event based Tracking: A Unified Network, Dataset, and Metric},
  author={Tang, Chuanming and Wang, Xiao and Huang, Ju and Jiang, Bo and Zhu, Lin and Zhang, Jianlin and Wang, Yaowei and Tian, Yonghong},
  journal={arxiv pre-print},
  year={2022}
}
```


