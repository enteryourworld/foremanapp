document.addEventListener('DOMContentLoaded', () => { // Работники при загрузке страницы

  let reg = document.getElementById('addworker-form');
    reg.onsubmit = async function (e) {
        e.preventDefault();

        const data = {
            name: document.getElementById('name').value,
            patronymic: document.getElementById('patronymic').value,
            surname: document.getElementById('surname').value,
            number: document.getElementById('number').value,
            status: document.getElementById('status').value,
        };

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch('add-worker/', { //ссылка на апи
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
                        //  addPopUpMessage(data.message)
                        console.log(data.message || 'Registration failed');
                        setTimeout(function () {
                            window.location.href = 'list.html'; // dryg stran
                        }, 2000)// ебашьте
                    });
                }
            })

    }


    

    const photoElement = document.getElementById('equipmentphoto');
    photoElement.addEventListener('change', function (e) {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.onloadend = function () {

            let base64String = reader.result;
            console.log(base64String)
            let regeq = document.getElementById('addequipment-form');

            regeq.onsubmit = async function (e) {
                e.preventDefault();
        
            }
            const data = {
                names: document.getElementById('names').value,
                expirydate: document.getElementById('expirydate').value,
                owner: document.getElementById('owner').value,
                registersdate: document.getElementById('registersdate').value,
                equipmentphoto: base64String,
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

                        return response.json().then((data) => {
                            //  addPopUpMessage(data.message)
                            console.log(data.message || 'Registration failed');
                            setTimeout(function () {
                                window.location.href = 'list.html'; // dryg stran
                            }, 2000)// ебашьте
                        });
                    }
            })
        };
        reader.readAsDataURL(file);
    })
    
})

document.getElementById('worker-btn').addEventListener('click', function(){
    document.getElementById('workers-table').classList.toggle('active')
    document.getElementById('addworker-form').classList.toggle('active')
});