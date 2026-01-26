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

        // title
        const h2 = document.createElement("h2");
        h2.textContent = this.title;

        //date
        const date = document.createElement("time");
        date.textContent = this.date;

        // description
        const desc = document.createElement("p");
        desc.textContent = this.description;

        // thumbnail
        const thumbnail = document.createElement("img");
        thumbnail.src = this.thumbnail;
        
        // read time 
        const read_time = document.createElement("p");
        read_time.textContent = this.readtime;


        this.el.append(h2,date,desc);
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
