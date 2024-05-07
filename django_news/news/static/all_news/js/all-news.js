/* variables */

const newsList = document.querySelector('.news__list')
const newsTemplate = document.querySelector('#news__template')

currentNewsCount = 0
newsCountIncrease = 3
lastNewsElement = null

/* */

/* functions */

function addNewsElement(news_id, header, text, imageUrl, tags)
{
    let newNews = newsTemplate.cloneNode(true)
    newNews.setAttribute('href', '/' + news_id)
    newNews.style.display = 'block'

    taglist = ''
    for (tag of tags) taglist += `<div class="news__list-item__taglist-item text">${tag}</div>`

    newNews.querySelector('.news__list-item__header').innerHTML = header
    newNews.querySelector('.news__list-item__image > img').setAttribute('src', imageUrl)
    newNews.querySelector('.news__list-item__text').innerHTML = text
    newNews.querySelector('.news__list-item__taglist').innerHTML = taglist

    newsList.appendChild(newNews)
}

function loadNewsAttempt()
{
    fetch(`http://127.0.0.1:8000/api/get_multiple/${currentNewsCount}/${currentNewsCount + newsCountIncrease}`, 
    {
        method: 'GET',
        headers: 
        {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => 
    {
        if (lastNewsElement != data[data.length - 1])
        {
            for (news of data)
            {
                console.log(news.text.substring(0, 100) + '...')
                addNewsElement(news.id, news.header, news.text.substring(0, 100) + '...', news.image, news.tags)
            }
            currentNewsCount += data.length
        }
    })
}

/* */

/* event listeners */

window.addEventListener('scroll', () => 
{
    var scrollTop = (document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop;
    var windowHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
    var documentHeight = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight, document.body.offsetHeight, document.documentElement.offsetHeight);
    if (documentHeight - scrollTop - windowHeight < 100) loadNewsAttempt()
});



/* */

/* other */

loadNewsAttempt()

/* */

