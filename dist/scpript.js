let trendsContainer = document.getElementsByClassName('container')[0]

async function getArticleRBC(){
    let response = await fetch('http://127.0.0.1:5000?link=https://www.rbc.ru/')
    let JSONRBC = await response.json()
    return JSONRBC
}
        


getArticleRBC()
    .then(cardsJSON => {
        return cardsJSON.content
    })
    .then((cardsJSON) => {
        for(card of cardsJSON){
            console.log(card.link)
            let newsCardHeader = document.createElement('h1')
            newsCardHeader.classList.add('news-card__header')
            newsCardHeader.innerText = card.header

            let dateAndCategory = document.createElement('span')
            dateAndCategory.classList.add('news-card__date-category')
            dateAndCategory.innerHTML = card.date

            let newsCard = document.createElement('a')
            newsCard.classList.add('news-card')
            newsCard.appendChild(newsCardHeader)
            newsCard.href = card.link
            newsCard.appendChild(dateAndCategory)

            trendsContainer.appendChild(newsCard)
        }
    })
