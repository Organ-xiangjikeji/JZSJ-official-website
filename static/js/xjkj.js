function guid() {
    function S4() {
        return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
    }

    return (S4() + S4() + S4());
}

function init_vcode() {
    var vk = guid();
    var ex = $('#vcode-key').val().trim();
    $('#codeimg').attr('src', '/api/get_vcode_img/?vk=' + vk + '&ex=' + ex);
    $('#vcode-key').val(vk);
};

function bind_vcode() {
    $('#codeimg').click(function () {
        var vk = guid();
        var ex = $('#vcode-key').val().trim();
        $('#codeimg').attr('src', '/api/get_vcode_img/?vk=' + vk + '&ex=' + ex);
        $('#vcode-key').val(vk);
    });

}

function check_username() {
    var user_ele = $('input[name="user"]');
    var user_val = user_ele.val().trim();

    if (user_val) {
        var reg = /^[\u4e00-\u9fa5_a-z_A-Z]{2,20}$/;
        if (!reg.test(user_val)) {
            user_ele.siblings('span').text('用户名不可包含特殊字符，长度不能超过20字');
            user_ele[0].scrollIntoView(true);
            return false
        }
        else {
            user_ele.addClass('success');
            return true
        }

    }
}

function check_vcode() {
    var vcode_ele = $('input[name="vcode"]');
    var vcode_val = vcode_ele.val().trim();
    if (vcode_val) {
        var reg = /^[0-9_a-z_A-Z]{4}$/;
        if (!reg.test(vcode_val)) {
            vcode_ele.siblings('span').text('验证码格式不正确');
            vcode_ele.addClass('warning');
            return false
        }
        else {
            vcode_ele.addClass('success');
            return true
        }
    }
}

function checkphone() {
    var phone_ele = $('input[name="phone"]');
    var phone_val = phone_ele.val().trim();
    if (phone_val) {
        var reg = /^1[3456789]\d{9}$/;
        if (!reg.test(phone_val)) {
            init_vcode();
            phone_ele.siblings('span').text('手机号格式不正确');
            phone_ele.addClass('warning');
            phone_ele[0].scrollIntoView(true);
            return false
        }
        else {
            phone_ele.addClass('success');
            return true
        }
    }

}

function bind_move_warning() {
    $('input').focus(function () {
        $(this).removeClass('warning');
    });
}

function check_corp() {
    var corp_ele = $('input[name="corp"]');
    var corp_val = corp_ele.val().trim();
    if (corp_val) {
        var reg = /^[\u4e00-\u9fa5]{2,10}$/;
        var reg1 = /^[A-Za-z&]{2,20}$/;
        if (!reg.test(corp_val)) {
            if (!reg1.test(corp_val)) {
                corp_ele.addClass('warning');
                corp_ele.siblings('span').text('公司名只能是全英或全中文大于2个字符，中文不能超过10个字,英文不能超过20个字')
                corp_ele[0].scrollIntoView(true);
                return false
            }
            else {
                corp_ele.addClass('success');
                return true
            }

        }
    }

}

function sendmsg() {
    if (checkphone() & check_vcode()) {
        console.log('可以发送了');
    }
}

function bind_cancel() {
    $('#cancel').click(function () {
        console.log('hohohohohoho');
        $('.c1').addClass('hidden');

        $('.c2').addClass('hidden');

    });
}

function bind_clear_warning() {
    $("input").each(function () {
        $(this).focus(function () {
            $(this).siblings('span').text('');
        });
    });
}

function check_needs() {
    var needs_ele = $('textarea[name="needs"]');
    console.log(needs_ele.val());
    var needs_val = needs_ele.val().trim();
    console.log(needs_ele);
    if (needs_val) {
        var reg = /^.{1,1000}/;
        if (!reg.test(needs_val)) {
            needs_ele.addClass('warning');
            needs_ele.siblings('span').text('需求不能超过1000字');
            return false
        } else {
            needs_ele.addClass('success');
            return true
        }
    } else {
        return true
    }
}

function checkmail() {

    var email_ele = $('input[name="email"]');
    var email_val = email_ele.val().trim();
    if (email_val) {
        var reg = /^(?!_)[a-zA-Z0-9__]{2,10}@[a-z0-9-]{1,10}(\.[a-z0-9-]{1,10})*\.[a-z0-9]{2,6}$/;
        /*小写*/
        if (!reg.test(email_val)) {
            init_vcode();
            email_ele[0].scrollIntoView(true);
            email_ele.addClass('warning');
            email_ele.siblings('span').text('前缀名不能包含除了’_‘以外的特殊字符和中文字符,长度不能超过10个字符,');
            return false
        }
        else {
            email_ele.addClass('success');
            return true
        }
    }

}
function check_reg_input() {
     var flag = true;

    $('input').each(function () {
        if ($(this).attr('name') =='phone' | $(this).attr('name') =='vcode'  ){
              console.log('this');
        if ($(this).val().trim() == "" && $(this).attr('required')) {
            $(this).addClass('warning');
            $(this).attr('placeholder', '此字段不能为空');
            $(this).siblings('span').text('此字段不能为空');
            init_vcode();
            $(this)[0].scrollIntoView(true);
            flag = false;
        }}
    });
    return flag
}
function check_input() {
    var flag = true;
    $('input').each(function () {

        if ($(this).val().trim() == "" && $(this).attr('required')) {
            $(this).addClass('warning');
            $(this).attr('placeholder', '此字段不能为空');
            $(this).siblings('span').text('此字段不能为空');
            init_vcode();
            $(this)[0].scrollIntoView(true);

            flag = false;

        }
    });

    return flag


}

$(document).ready(function () {
    bind_vcode();
    init_vcode();
    bind_move_warning();
    bind_cancel();
    bind_clear_warning();
});