var updateBtns = document.getElementsByClassName('update-cart')


for ( var i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function (){
        var  product=this.dataset.product
        var action=this.dataset.action
        console.log('productId;', product, 'action:', action)

        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log('Not Loged In')
        }else {
            updateuserorder(product , action)
        }
    })
}

function updateuserorder(product ,action ) {
    console.log('user is logged in , sending the data..')
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'productId': product, 'action': action})
    })

        .then((response) => {
            return response.json()

                .then((data) => {

                        console.log('data:', data)

                })
        })
}


function addCookieItem(product, action){
	console.log('User is not authenticated')

	if (action === 'add'){
		if ( carts[foodId]===undefined){
		carts[foodId] = {'quantity':1}

		}else{
			carts[foodId]['quantity'] += 1
		}
	}

	if (action === 'remove'){
		carts[foodId]['quantity'] -= 1

		if (carts[foodId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete carts[foodId];
		}
	}
	console.log('CART:', carts);
	document.cookie ='cart=' + JSON.stringify(carts) + ";domain=;path=/"

	location.reload()
}

