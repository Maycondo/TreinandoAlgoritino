let items = []


document.querySelector('input[type=submit]')
.addEventListener('click', () => {
    let nomeProduto = document.querySelector('input[name=nome_produto]');
    let precoProduto = document.querySelector('input[name=price');


    items.push({
        nome: nomeProduto.value,
        valor: precoProduto.value,
    });

    let listaProdutos = document.querySelector('.lista-produtos')
    let soma = 0;
    listaProdutos.innerHTML = '';

    items.map(function(val) {
        soma+=parseFloat(val.valor) ;
        listaProdutos.innerHTML += ` 

        <div class="lista-produtos-single">
        <h3>${val.nome}</h3>
        <h3 class="price-produto"><span>${val.valor}</span></h3>
      </div>

      `
    })


soma = soma.toFixed(3)
nomeProduto.value = '';
precoProduto.value = ''; 

let elementoSoma = document.querySelector('.soma-produto h1');
elementoSoma.innerHTML = 'R$'+soma + 'REAIS';

}); 


document.querySelector('button[name=limpar]')
.addEventListener('click', () => {
    items = [];

    let listaProdutos = document.querySelector('.lista-produtos').innerHTML = '';
    let elementoSoma = document.querySelector('.soma-produto h1').innerHTML = 'TOTAL: 000 $REAIS';
})