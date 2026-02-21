/* Codigo JS necesario para las funcionalidades de index.html */
const botonEditar = document.querySelector('button');
const main = document.querySelector('main');

botonEditar.addEventListener('click', async()=>
    {

        const respuesta = await fetch ('http://127.0.0.1:5000/developer');
        const developer = await respuesta.json()
        console.log(developer)
    })
