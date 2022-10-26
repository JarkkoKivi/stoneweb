const kuvaOverlay = document.getElementById('picture-view-frame');
let sulkunappi = document.getElementById('close-button');

const galleryImage =  document.getElementsByClassName('gallery-img-wrapper');

const overlayImage = document.getElementById('current-portfolio-img');
const arrowLeft = document.getElementById('arrow-left');
const arrowRight = document.getElementById('arrow-right');


//Yksittäiskuvanäkymän sulkeminen

if(sulkunappi) {
    sulkunappi.addEventListener('click', () => {
        kuvaOverlay.style.display = 'none';
    });
}

//Ensimmäisen kuvan valinta yksittäiskuvaikkunaan

if(galleryImage) {
    for(let image of galleryImage) {

        image.firstElementChild.addEventListener('click', (e) => {
            kuvaOverlay.style.display = "flex";
            overlayImage['src'] = e.target['src'];
        });
    };
};
// Kuvan vaihtaminen nuolista

if(arrowLeft) {
    arrowLeft.addEventListener('click', (e) => {
        let imageSrc = overlayImage['currentSrc'];
        let imageIndex = 0;
        for (let i = 0; i < galleryImage.length; i++){
            if(galleryImage[i].firstElementChild.src == imageSrc) {
                imageIndex = i - 1;
                if(imageIndex == -1) {
                    imageIndex = galleryImage.length -1;
                }
            }
        }
        overlayImage['src'] = galleryImage[imageIndex].firstElementChild['src'];
    });

    arrowRight.addEventListener('click', () => {
        let imageSrc = overlayImage['currentSrc'];
        let imageIndex = 0;
        for (let i = 0; i < galleryImage.length; i++){
            if(galleryImage[i].firstElementChild.src == imageSrc) {
                imageIndex = i + 1;
                if(imageIndex == galleryImage.length) {
                    imageIndex = 0;
                }
            }
        }
        overlayImage['src'] = galleryImage[imageIndex].firstElementChild['src'];
    });
}