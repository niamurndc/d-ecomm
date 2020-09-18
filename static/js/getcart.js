document.addEventListener('DOMContentLoaded', getCart);

// get cart option
function getCart(){
  let cts = localStorage.getItem('cart');
  cts = JSON.parse(cts);
  cts.forEach(cart => {
    const cartTable = document.getElementById('cart-table');
    const cartItem = document.createElement('tr');
    cartItem.innerHTML = `<td class="cart_description">
                            <h4><a href="">${cart.title}</a></h4>
                          </td>
                          <td class="cart_price">
                            <p>$${cart.price}</p>
                          </td>
                          <td class="cart_quantity">
                              <input style="width: 70px;" class="cart_quantity_input" type="number" name="quantity" value="${cart.quantity}" size="1">
                          </td>
                          <td class="cart_total">
                            <p class="cart_total_price">$${cart.total}</p>
                          </td>
                          <td class="cart_delete" id="delete">
                            <a class="cart_quantity_delete" href="#"><i class="fa fa-times"></i></a>
                          </td>`;

    // final append
    cartTable.appendChild(cartItem);
  });
}

const deleteCart = document.getElementById('cart-table');
deleteCart.addEventListener('click', (e) => {
  console.log();
  if(e.target.parentElement.classList.contains('cart_quantity_delete')){
    let cartItems = JSON.parse(localStorage.getItem('cart'));
    cartItems.forEach((item, index) => {
      if(item.title == e.target.parentElement.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.innerText){
        cartItems.splice(index, 1);
        localStorage.setItem('cart', JSON.stringify(cartItems));
      }
    });

    e.target.parentElement.parentElement.parentElement.remove();
  }
});

const getProduct = document.getElementById('get-product');
const getMoney = document.getElementById('get-total');

const getall = JSON.parse(localStorage.getItem('cart'));
let getName = [];
let getTotal = 0;
getall.forEach(gt => {
  getName.push(gt.title);
  getTotal = getTotal + gt.total;
  console.log(getName);
})
getMoney.value = getTotal;
getProduct.value = getName;