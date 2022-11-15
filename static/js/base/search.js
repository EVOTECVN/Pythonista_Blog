function navBarSearchOnclick() {
    const keyword = document.getElementById('navSearchBar').value
    location.href = 'search?keyword=' + keyword
}


function searchOnclick() {
    const keyword = document.getElementById('searchBar').value
    location.href = 'search?keyword=' + keyword
}