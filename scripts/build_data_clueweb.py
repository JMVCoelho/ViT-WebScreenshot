from clueweb_api import ClueWeb22Api
import sys

#path_clueweb = "/mnt/datasets/clueweb2022"
path_clueweb = sys.argv[1]

path_out = sys.argv[2]
#path_out = "data"

subdirectory = "en0000"
file_sequence = "00"

max_docs_per_file_sequence = 25000

with open(f'{path_out}/labels.tsv', 'w') as out:
    for doc_id in range(0, max_docs_per_file_sequence):

        ddoc_id = str(doc_id).zfill(5)

        cweb_doc_id = f"clueweb22-{subdirectory}-{file_sequence}-{ddoc_id}"
        clueweb_api = ClueWeb22Api(cweb_doc_id, path_clueweb)

        try:
            in_links = len(eval(clueweb_api.get_inlinks())['anchors'])

        except Exception as e:
            continue
        
        # write to tsv format
        out.write(f"{cweb_doc_id}\t{in_links}\n")