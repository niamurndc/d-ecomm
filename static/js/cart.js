const submit = document.getElementById('submit');
const title = document.getElementById('title').innerText;
const price = document.getElementById('price').innerText;
const quantity = document.getElementById('quantity').value;

submit.addEventListener('click', submitCart);

let carts = [];

// duplicate check
function submitCart(){
  let lcart = JSON.parse(localStorage.getItem('cart'));
  if(lcart == null){
    addCart();
  }else{
    let names = [];
    lcart.forEach(lc => {
      names.push(lc.title);
    })

    if(names.includes(title)){
      console.log('Item Already Added');
    }else{
      console.log('pass');
      addCart();
    }
  }
}


// add cart option
function addCart(){
  const cart = {
    title: title,
    price: price,
    quantity: quantity,
    total: price * quantity,
  };
  const getcart = JSON.parse(localStorage.getItem('cart'));
  if(getcart == null){
    carts = [];
  }else{
    carts = getcart;
  }
  carts.push(cart);
  localStorage.setItem('cart', JSON.stringify(carts));
}






