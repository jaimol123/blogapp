$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name +'=')) {
                         cookieValue =decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) ||
/^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});

$("#submitsign").click(function(e){
$("#formsign").submit()
});
$("#formsign").submit(function(e) {
    e.preventDefault();
    var formData = new FormData(this);
    $.ajax({
    url : "{% url 'list' %}",
    type : "POST",
    data : formData,
    dataType:'json',
    contentType: false,
    processData: false,
        success : function(data) {

            if (data.status== 1)
             {
               alert("success");

             }

        },

        error : function(xhr,errmsg,errors) {
                  if(data.status==0)
                    {
                    alert("failed ")
                     }

        console.log(xhr.status + ": " + xhr.responseText);
        console.log(errors)// provide a bit more info about the error to the console
        }
    });
});


$("#apple").click(function(e){
$("#loginform").submit()
});
$("#loginform").submit(function(e) {

    e.preventDefault();
    alert("ajax call");
    var formData = new FormData(this);
    alert("inside form");
    $.ajax({
	url:"/login/",
	 data : formData,
	type:"post",
	datatype:"json",
	 contentType: false,
    processData: false,
	success:function(data)
		{
        if(data.val1==1)
        {
        alert("login sucess");
        }
        if(data.val1==2)
        {
        alert("username/password incorrect")
        }
        if(data.val1==3)
        {
        alert("login failed")
        }

		},
	error:function()
		{
		alert("connection failed");
		}
});
});



