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
$("#viewnow").click(function(e){ 
	e.preventDefault(); 
	$.ajax({
	url:"viewpostfn",
	type:"post",
	datatype:"json", 
	data:$("#viewimg").serialize(), 
	success:function(data)
		{
			if(data.status)     
			{
			$("#textview").val(data.val1)
			}	
			else
			{
			alert("enter a valid name");
			}
		},
		error:function()
		{
		alert("connection failed");
		}
});
});

