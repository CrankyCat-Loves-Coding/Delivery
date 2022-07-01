var errorName = true
var errorPwd = true
var errorConfirmPwd = true
var errorCheckout = false
var errorEmail = true

$(function () {
    //input reminder
    $('#user_name').blur(function () {
        checkName()
    })
    $('#pwd').blur(function () {
        checkPwd()
    })
    $('#cpwd').blur(function () {
        checkConfirmPwd()
    })
    $('#email').blur(function () {
        checkEmail()
    })

});
//checking input
function checkName() {
    name = $('#user_name').val().length;
    if (name==0){
        $('#user_name').next().html("Username can't be empty");
        $('#user_name').next().show();
        errorName = true
    }
    else if(name > 15){
        $('#user_name').next().html('Username is too long')
        $('#user_name').next().show();
        errorName = true
    }
    else{
        // check valid username
        $.get('/user/register/checkname/'+$('#user_name').val(), function (data) {
            if (data==0){
                $('#user_name').next().html('Username is alright exist')
                $('#user_name').next().show()
                errorName = true
            }
            else {
                $('#user_name').next().hide();
                errorName = false
            }
        })
    }
}
//check valid password
function checkPwd() {
    pwdLength = $('#pwd').val().length;
    if(pwdLength<6 || pwdLength > 20){
        $('#pwd').next().html('Password need to be atlest 6')
        $('#pwd').next().show()
        errorPwd = true
    }
    else {
        $('#pwd').next().hide()
        errorPwd = false
    }
}
//检验两次输入密码是否一致
function checkConfirmPwd() {
    pwd = $('#pwd').val();
    cpwd = $('#cpwd').val();
    if(pwd != cpwd){
        $('#cpwd').next().html('两次密码输入不一致')
        $('#cpwd').next().show()
        errorConfirmPwd = true
    }
    else {
        $('#cpwd').next().hide()
        errorConfirmPwd  = false
    }
}
//检验手机号码
function checkEmail() {
    var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			errorEmail = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			errorEmail = true;
		}
}
//发送post请求时在进行检验输入合法性
$(function () {
    $('#reg_form').submit(function () {
    //     alert('jiance')
    checkName()
    checkPwd()
    checkConfirmPwd()
    checkEmail()
    if(errorName == false && errorPwd == false && errorConfirmPwd == false &&errorEmail == false && errorCheckout==false){
        // 验证成功，提交
        return true
    }
    // 验证不成功，阻止表单的默认行为。
    return false

})
})