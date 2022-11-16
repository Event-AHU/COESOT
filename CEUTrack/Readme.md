                                                            ### ours
# train

    export CUDA_VISIBLE_DEVICES=6
    python tracking/train.py --script ceutrack --config ceutrack_coesot  \
    --save_dir ./output --mode multiple --nproc_per_node 1 --use_wandb  0
    python tracking/test.py   ceutrack ceutrack_coesot --dataset coesot --threads 20 --num_gpus 1
    python tracking/analysis_results.py --dataset coesot  --parameter_name ceutrack_coesot


    export CUDA_VISIBLE_DEVICES=5
    python tracking/train.py --script ceutrack --config ceutrack_fe108  \
    --save_dir ./output --mode multiple --nproc_per_node 1 --use_wandb  0
    python tracking/test.py   ceutrack ceutrack_fe108 --dataset fe108 --threads 16 --num_gpus 1
    python tracking/analysis_results.py --dataset fe108  --parameter_name ceutrack_fe108


    export CUDA_VISIBLE_DEVICES=6
    python tracking/train.py --script ceutrack --config ceutrack_visevent  \
    --save_dir ./output --mode multiple --nproc_per_node 1 --use_wandb  0
    python tracking/test.py   ceutrack ceutrack_visevent --dataset visevent --threads 16 --num_gpus 1
    python tracking/analysis_results.py --dataset visevent  --parameter_name ceutrack_visevent
