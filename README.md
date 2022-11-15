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




### Acknowledgement: 

### Citation: 
```bibtex
@article{tang2022coesot,
  title={Revisiting Color-Event based Tracking: A Unified Network, Dataset, and Metric},
  author={Tang, Chuanming and Wang, Xiao and Huang, Ju and Jiang, Bo and Zhu, Lin and Zhang, Jianlin and Wang, Yaowei and Tian, Yonghong},
  journal={arxiv pre-print},
  year={2022}
}
```


