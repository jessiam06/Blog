from pathlib import Path
import markdown as md
import json
CONTENT_DIR = Path("Content")
JSON_FILE = Path("posts.json")

def frontmatter_to_json(frontmatter):
    frontmatter_dict = {}
    frontmatter = frontmatter.split('\n')

    for entry in frontmatter:
        entry = entry.split(":")
        frontmatter_dict[entry[0]] = entry[1].strip()
    
    # format tags
    frontmatter_dict["tags"] = list(map(lambda x : x.strip() ,frontmatter_dict["tags"].split(",")))
    #frontmatter = json.dumps(frontmatter_dict)

    return frontmatter_dict



def parse_frontmatter(md_file: Path):
    with md_file.open("r",encoding="utf-8") as file:
        # read through for frontmatter

        # expect firstline to be ---
        flag = False
        delim = file.readline().strip()

        if delim != "---":
            raise Exception("Expected first line to be delimiter: ---")

        frontmatter = ""
        body = ""

        while flag == False:
            text = file.readline()
            if text.strip() == delim:
                flag = True
            else:
                frontmatter += text

        for line in file:
            body += line
            
        frontmatter = frontmatter.rstrip()
        frontmatter = frontmatter_to_json(frontmatter)
        return frontmatter, body
    

def write_to_json_file(frontmatter,json_file: Path):
    
    # load the file to append to. If empty, initialize empty file
    if JSON_FILE.stat().st_size > 0:
        with JSON_FILE.open("r",encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = []
    
    # append data
    data.append(frontmatter)
    
    with JSON_FILE.open("w",encoding="utf-8") as file:
        json.dump(data,file,indent=2)


for md_file in CONTENT_DIR.iterdir():
    if "_LOADED" not in md_file.name:
        frontmatter, body = parse_frontmatter(md_file)   
        write_to_json_file(frontmatter,JSON_FILE)
        md_file.rename(md_file.with_stem(md_file.stem + "_LOADED"))




    

