### About

Simple experiment where given a web page screenshot, we try to predict centrality estimators such as the number of inlinks.  

Contains code for data processing, model training, and evaluation.  

Results:
RMSE: 0.18  
Random predictor: 0.55  

### Environment
conda create -n webvit python=3.9.6

conda activate webvit

pip install transformers

conda install -c conda-forge tqdm

conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia

### Data
This requires access to the ClueWeb22 dataset. More specifically, this uses images in the en0000-00 subset.

As such, you should unzip `<cluewebpath>/jpg/en/en00/en0000/en0000-00.zip` to a folder of your choosing, `<unzipped_jpgs_path>`.

To use different or more subsets, change `python scripts/build_data_clueweb.py` accordingly.

### How to run

#### Build labels from clueweb data:
`python scripts/build_data_clueweb.py <clueweb_path> <data_save_path>`

this will write the file `<data_save_path>/labels.tsv` , in the format <doc_id>\t<n_inlinks>

#### Prepare images:


`./scripts/remove_unlabeled_jpgs.sh <data_save_path>/labels.tsv <unzipped_jpgs_path>` 

`./scripts/train_test_splits.sh <data_save_path>`

This remove any images that couldn't be labeled, and split them into train, test (1k), and validation (1k). 

#### Train and evaluate (with slurm):

This assumes `<data_save_path>` as `./data`, change accordingly:

`sbatch ./launch.sh`


### Random baseline

`python scripts/random_predictor.py <data_save_path>`
