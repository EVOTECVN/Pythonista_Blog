// Load first data
let next = ''
let postDiv = document.getElementById('postDiv')
let loadMoreButton = document.getElementById('loadMore')
console.log(postDiv)

function getPosts(nextUrl) {
    let apiUrl
    if (nextUrl === '') {
        apiUrl = "api/posts"
    }
    else {
        apiUrl = nextUrl
    }
    $.ajax({
        type: "GET",
        url: apiUrl,
        success: function (response) {
            console.log(response.next)
            next = response.next
            if (next===null) {
                loadMoreButton.style.visibility = 'hidden'
            }
            const data = response.results

            for (const post of data) {
                postDiv.innerHTML += `<div class="col-md-5 mx-2 my-2">
                    <a href="${post.url}">
                        <div class="card">
                            <img class="card-img-top img-fluid w-100" src="${post.image}" alt="{{ post.title }}">
                            <div class="card-body">
                                <h5 class="card-title">
                                    ${post.title}
                                </h5> 
                            </div>
                        </div>
                    </a>
                </div>`
            }
        }
    })
}

getPosts(next);

function loadMore() {
    getPosts(next)
}

