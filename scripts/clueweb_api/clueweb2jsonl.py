from ClueWeb22Api import ClueWeb22Api

import json
with open('/data/jcoelho/clueweb22/full_en_B/index/raw/full_corpus.jsonl', 'w') as raw_jsonl:
    for subfolder_id in range(0, 45):
        for jsongz_id in range(0, 100):
            for doc_id in range(0, 10000):

                ssubfolder_id = str(subfolder_id).zfill(2)
                jjsongz_id = str(jsongz_id).zfill(2)
                ddoc_id = str(doc_id).zfill(5)

                cweb_doc_id = f"clueweb22-en00{ssubfolder_id}-{jjsongz_id}-{ddoc_id}"
                clueweb_api = ClueWeb22Api(cweb_doc_id, "/mnt/datasets/clueweb2022")

                try:
                    clean_txt = eval(clueweb_api.get_clean_text())
                    cweb_id = clean_txt["ClueWeb22-ID"]
                    content = clean_txt["Clean-Text"].strip()
                except Exception as e:
                    continue

                to_write = {'id': cweb_id, 'contents': content}

                json.dump(to_write, raw_jsonl)
                raw_jsonl.write('\n')