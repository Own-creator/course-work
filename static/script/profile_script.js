// получаем обьект всех лайкнутых фотографий
let liked_photos = JSON.parse(localStorage.getItem('liked_photos'))
// контейнер для всех лайкнутых фотографий
const liked_photos_container = document.querySelector('.liked_photos_container')
// проходимся в цикле по всем фотографиям\добавляем слушатель собитый для кажддой фотографии
for (let i = 0; i < liked_photos.length; i++) {
    let image = document.createElement('img')
    image.addEventListener('click', () => {
        image.id = image.id === 'fullscreen' ? '' : 'fullscreen';
    })
    // для каждого изображение выствляем ссылку
    image.src = liked_photos[i]
    // в контейнер добавляем фотогарафию
    liked_photos_container.appendChild(image)
}
