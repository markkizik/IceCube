// window.Telegram.WebApp.ready();

expand()

let ice = document.querySelector('.counter-coin');
let speedclick = document.querySelector('.charge-speed');

function incrementIce() {
    ice.innerHTML = parseInt(ice.innerHTML) + 1;
    speedclick.innerHTML = parseInt(speedclick.innerHTML) - 1;
}

localStorage.setItem('currency', ice.innerHTM);

setInterval(() => {
    let currentSpeed = parseInt(speedclick.innerHTML);

    if (currentSpeed < 500) {
        speedclick.innerHTML = currentSpeed + 1;
    }

}, 1000);
