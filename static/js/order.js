var total ='{{order.get_cart_total}}'
var shipping = '{{order.shipping}}'
var form = document.getElementById('form')

//monitor click for make payment button
// document.getElementById('make-payment').addEventListener('click',function(e){
//     submitFormData()
// })

function submitFormData(){
    console.log('Payment button clicked....')

    // var userFormData = {
    //     'name':null,
    //     'email':null,
    //     'total':total,
    // }

    // var shippingInfo = {
    //     'address':null,
    //     'email':null,
    //     'phone':null,
    // }

    // if(shipping != 'False'){
    //     shippingInfo.address = form.address.value
    //     shippingInfo.email = form.email.value
    //     shippingInfo.phone = form.phone.value
    // }

    var url = '/process_order/'
    fetch(url, {
        method:'POST',
        headers:{
            'content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'form': userFormData, 'shipping': shippingInfo})
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data);
        // alert('Transaction completed');
        // window.location.href = "{% url 'index' %}"
    })
}