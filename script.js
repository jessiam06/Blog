class PostCard {
    constructor (data){
        // Root element
        this.el = document.createElement("article"); // .el is convention for root element. 
        this.el.className = "post-card"

        // attributes
        this.title = data.title;
        this.date = data.date;
        this.description = data.description;
        this.thumbnail = data.thumbnail;
        this.readtime = data.readtime;
        this.tags = data.tags;

        this.render();
    }

    render () {
        // Render the Post

        // thumbnail
        const thumbnail_container = document.createElement("div");
        const thumbnail = document.createElement("img");
        thumbnail_container.className = "post-thumbnail"
        thumbnail.src = this.thumbnail;
        thumbnail_container.appendChild(thumbnail);

        // metadata
        const metadata = document.createElement("div");
        metadata.className = "metadata";

        //metadata_grid
        const metadata_grid = document.createElement("div");
        metadata_grid.className = "metadata_grid";


        // title
        const title = document.createElement("h2");
        title.className = "post-title";
        title.textContent = this.title;

        //date and read time
        const date_and_readtime = document.createElement("time");
        date_and_readtime.className = "post-date";
        date_and_readtime.textContent = this.date + " | " + this.readtime;

        // description
        const desc = document.createElement("p");
        desc.className = "post-desc";
        desc.textContent = this.description;

        metadata.append(title,date_and_readtime);
        this.el.append(thumbnail_container,metadata);
    }
}


const container = document.getElementById("post-grid");

fetch("posts.json")
    .then(function(response){
        return response.json();
    })
    .then(function(posts){
        for (let i = 0; i < 9; i++){
            const card = new PostCard(posts[0]);
            container.appendChild(card.el);
        }
    })
