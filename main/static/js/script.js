function addPopUpMessage(message){
    let popupback = document.createElement('div')
    popupback.classList.add('popup-bg');
    popupback.innerHTML = `<div>${message}</div>`;
    document.body.appendChild(popupback);
}

let tabs = document.querySelector('.tabs');
tabs.addEventListener('click', e => {
    let target = e.target;
    if(target.closest('.tabs__item')){
        tabs.querySelectorAll('.tabs__item').forEach((item) => {
            item.classList.remove('active')
        })
        document.querySelectorAll('.tabs__form').forEach((item) => {
            item.classList.remove('active')
        })
        target.closest('.tabs__item').classList.add('active')
        document.getElementById(target.dataset.tab).classList.add('active')
    }
})

let reg = document.getElementById('foremans-form');
reg.onsubmit = async function(e){
  e.preventDefault();

  const data = {
        names: document.getElementById('names').value,
        patronymic: document.getElementById('patronymic').value,
        surname: document.getElementById('surname').value,
        number: document.getElementById('number').value,
        password: document.getElementById('password').value,
    };

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

fetch('add-foremans/', { //ссылка на апи
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
             'X-CSRFToken': csrfToken,

        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) { 

            return response.json().then((data) => {
                addPopUpMessage(data.message)
                setTimeout(function(){
                    window.location.href = 'list.html'; // dryg stran
                }, 2000)
            });
        }
    })
    console.log('e')

}

let form = document.getElementById('enter-form');
form.onsubmit = async function(e){
  e.preventDefault();

  const data = {
        number: document.getElementById('number-enter').value,
        password: document.getElementById('password-enter').value,
    };

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

fetch('add-equipment/', { //ссылка на апи
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
             'X-CSRFToken': csrfToken,

        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
           
           window.location.href = 'cabinet'; // dryg stran
            return response.json().then((data) => {
                console.log(data.message || 'Registration failed');
            });
        }
    })
    console.log('e')

}