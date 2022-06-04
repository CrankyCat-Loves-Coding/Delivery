var updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var mealsId = this.dataset.meals
        var dessertsId = this.dataset.desserts
        var drinksId = this.dataset.drinks
        var action = this.dataset.action
        console.log(
            'mealsId:', mealsId,
            'dessertsId:', dessertsId,
            'drinksId:', drinksId,
            'action:', action,
        )( )

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(menuId, action)
        }
    })
}

function updateUserOrder(menuId, action){
    console.log('User is logged in, sending data...')

    var url = '/update_cart/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'menuId': menuId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
    })
}