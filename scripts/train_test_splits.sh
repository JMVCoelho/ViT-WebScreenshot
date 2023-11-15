data_path=$1

# ../data/clueweb_screeshots/val

mkdir -p $data_path/train
mkdir -p $data_path/val
mkdir -p $data_path/test


find . -name '*.jpg' -print | shuf -n 1000 | xargs -I{} mv {} $data_path/val && find . -name '*.jpg' -print | shuf -n 1000 | xargs -I{} mv {} $data_path/test && find . -name '*.jpg' -print | xargs -I{} mv {} $data_path/train