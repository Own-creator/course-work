// получаем элемент кнопки лайк
const like_button = document.getElementById('like_button')
// элемент изображения
const image = document.getElementById('wallpaper')
// массив фотографий который уже есть в локальном хранилище
let liked_photos = JSON.parse(localStorage.getItem('liked_photos'))
// если лайнутых фото нет то он пустой
if (!liked_photos) {
    liked_photos = []
}
// слушатель событый берем ссылку на изображение
like_button.addEventListener('click', () => {
    let link = image.attributes.getNamedItem('src').value;
// добавляем фон в локальное хранилище
    if (!liked_photos.includes(link)) {
        liked_photos.push(link)
        localStorage.setItem('liked_photos', JSON.stringify(liked_photos))
    }
})