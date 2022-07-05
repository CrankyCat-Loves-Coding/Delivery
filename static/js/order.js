var total ='{{order.get_cart_total}}'
var form = document.getElementById('form')

// monitor click for make payment button
document.getElementsByClassName('make-payment').addEventListener('click',function(e){
    submitFormData()
})


function submitFormData(){
    console.log('Payment button clicked....')

    var userFormData = {
        'name':null,
        'phone':null,
        'email':null,
        'total':total,
    }

    var shippingInfo = {
        'address':null,
        'email':null,
        'eircode':null,
    }

    var url = '/process_order/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'form': userFormData, 'shipping': shippingInfo})
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data);
    })
}