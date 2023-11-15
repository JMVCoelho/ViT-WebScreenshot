labels_path=$1
jpgs_path=$2

pushd $jpgs_path
comm -23 <(ls *.jpg | sort | grep -Eo '^[^.]+') <(cut -f1 $labels_path | sort) | xargs -I {} rm {}.jpg
popd