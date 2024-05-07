/* variables */

let reactionsElement = document.querySelector('.news__list-item__reactions')
let likeElement = document.querySelector('.news__list-item__reactions__like')
let dislikeElement = document.querySelector('.news__list-item__reactions__dislike')

/* */

/* functions */

function updateReactions(reactionsElement, news_id)
{
    let likeElement = reactionsElement.querySelector('.news__list-item__reactions__like')
    let dislikeElement = reactionsElement.querySelector('.news__list-item__reactions__dislike')

    fetch('http://127.0.0.1:8000/api/get_single/' + news_id, 
    {
        method: 'GET',
        headers: 
        {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    })
    .then(response => response.json())
    .then(data => 
    {
        likeElement.innerHTML = 'LIKE ' + data.likes,
        dislikeElement.innerHTML = 'DISLIKE ' + data.dislikes
    })
    .catch(error => console.log(error))
}

function newsReact(news_id, action, reactionsElement)
{
    let APIRequest = null;
    if (action == 'like') APIRequest = 'like'
    else if (action == 'dislike') APIRequest = 'dislike'
    else throw new Error('Wrong value')
    
    return fetch('http://127.0.0.1:8000/api/' + APIRequest + '/' + news_id, 
    {
        method: 'POST',
        headers: 
        {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    })
    .then(response => updateReactions(reactionsElement, news_id))
    .catch(error => console.log(error))
}

/* */

/* event listeners */

likeElement.addEventListener('click', (e) => { e.preventDefault(); newsReact(news_id, 'like', reactionsElement) })
dislikeElement.addEventListener('click', (e) => { e.preventDefault(); newsReact(news_id, 'dislike', reactionsElement) })

/* */

/* other */

updateReactions(reactionsElement, news_id)

// add view
fetch('http://127.0.0.1:8000/api/view/' + news_id, 
{
    method: 'POST',
    headers: 
    {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    }
})

/* */