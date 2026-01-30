from pathlib import Path
import markdown
import json
import shutil
CONTENT_DIR = Path("Content")
JSON_FILE = Path(r"static\posts.json")

def frontmatter_to_json(frontmatter):
    frontmatter_dict = {}
    frontmatter = frontmatter.split('\n')

    for entry in frontmatter:
        entry = entry.split(":")
        frontmatter_dict[entry[0]] = entry[1].strip()
    
    # format tags
    frontmatter_dict["tags"] = list(map(lambda x : x.strip() ,frontmatter_dict["tags"].split(",")))
    #frontmatter = json.dumps(frontmatter_dict)

    frontmatter_dict["link"] = fr"/build/posts/{frontmatter_dict["title"].replace("?","")}.html"

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

def populate_html_template(frontmatter: dict, body):
    title = frontmatter["title"]
    subtitle = frontmatter["subtitle"]
    desc = frontmatter["description"]
    date = frontmatter["date"]
    thumbnail = frontmatter["thumbnail"]
    tags = frontmatter["tags"]
    readtime = frontmatter["readtime"]

    # create a copy of the template
    template = Path(r"Templates\post.html")
    
    # destination directory
    post = Path(fr"build\posts\{title.replace("?","")}.html")

    shutil.copy(template,post)

    # edit the html file (read - edit - write)

    contents = post.read_text(encoding="utf-8")
    contents = contents.replace("{{Title}}",title)
    contents = contents.replace("{{Subtitle}}",subtitle)
    contents = contents.replace("{{date}}", date)
    contents = contents.replace("{{readtime}}",readtime)
    contents = contents.replace("{{tags}}",",".join(tags))
    contents = contents.replace("{{Thumbnail}}",thumbnail)
    contents = contents.replace("{{content}}",body)

    post.write_text(contents,encoding="utf-8")





def render():
    for md_file in CONTENT_DIR.iterdir():
        if "_LOADED" not in md_file.name:
            frontmatter, body = parse_frontmatter(md_file)   
            write_to_json_file(frontmatter,JSON_FILE)
            md_file.rename(md_file.with_stem(md_file.stem + "_LOADED"))

            body_html = markdown.markdown(body)
            populate_html_template(frontmatter,body_html)

render()







    

