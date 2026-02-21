/* Codigo JS necesario para las funcionalidades de editar.html */
const parametrosURL = new URLSearchParams(window.location.search);
const idDdeveloper = parametrosURL.get ('id')
const formulario = document.getElementsByid('Formulario-editar');


formulario.addEventListener('submit', async(evento)) = 
    evento.preventDefault();

    const datosNuevos = {
        name: document.getElementById('nombre').value,
        skills: document.getElementById('habilidad').value,
        salary: document.getElementById('salario').value,
        avatar: document.getElementById('avatar').value,
    };
/* mando los datos y doy respuestas si va todo bien */

    const respuesta = await fetch('http://127.0.0.1:5000')
    

    if (respuesta.ok){
        alert("Se actualizo");

    }  
    else {
        alert("Error");
    }

    