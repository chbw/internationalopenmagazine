'''python3 script to recursive walk throug all non-draft files inside the
content folder and extract information

no longer necessary since i found out how to do count tags with 
pelican itself. The script may be useful for other purposes,
like automatic replacement or counting of strings
'''


import os

tagger = { "teaching" : 0,
           "coding": 0,
           "making": 0,
           "review": 0,
           "report": 0
        }
        


for root, dirs, files in os.walk("content", topdown=False):
    for name in files:
#       print( root, name)
        if ".md" in name or ".rst" in name or ".html" in name:
            f =open(os.path.join(root, name))
            lines = f.readlines()
            # is it a draft:
            draft = False
            for line in lines:
                if "status:" in line[:7] and "draft" in line[7:]:
                    draft = True
            if draft:
                continue
            for line in lines:
                if "tags:" in line[:5].lower():
                    for tag in tagger:
                        if tag in line[5:].lower():
                            tagger[tag] += 1
            f.close()
#    for name in dirs:
#        print(os.path.join(root, name))
        
print("fertig")
print("--------------")

for tag in tagger:
    print( tag.upper(),"=", tagger[tag])
