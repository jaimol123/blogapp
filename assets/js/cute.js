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
$("#submitsignup").click(function(e){
	e.preventDefault(); 
	$.ajax({
	url:"/",
	type:"post",
	datatype:"json", 
	data:$("#formsignup").serialize(),
	success:function(data)
		{

			if(data.status==1)
			{
			alert("signup successful");
			window.location.replace("{% url 'list' %}")
			}
			else if(data.status==0)
			{
			alert("password dont match");
			}


		else{


                  $("#formsignup :input:not(input[type='hidden'],input[type='submit'])").each(function ()
                  {                                                   // not is given for avoiding hidden fields and submit each fn is given for each iteration

                            var current = $(this).parent();  // here parent refers to the form or div where the code is enclosed
                            var current_name = $(this).attr('name'); // name of the current field in current iteration is obtained
                            $.each(data.key, function (index, value)
                            {                                          // from views.py we get the k-v pair index refers to key
                             if (current_name == index)
                             {
                                   current.after("<div class='error'></div>");
                                   current.next().html(value);


                                    }
                                });
                              });
                        }






		},
		error:function()
		{
		alert("connection failed");
		}
});
});






