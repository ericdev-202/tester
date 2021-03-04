$("#addEvent").on("submit", function GetTableData(e) {
		e.preventDefault();

		$.ajax({
			type:'POST',
			// url:'{% url "events" %}',
			data:{
				title:$('#title').val(),
				description:$('#description').val(),
				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
				action: 'post'

			},
			success:function(data){
				document.getElementById("addEvent").reset();
				$("#eventTable tbody").prepend(
					'<tr><td>${fields["title"]||""}</td><td>${fields["description"]||""}</td></tr>'
					)    
			},
			error : function(xhr,errmsg,err){
				console.log(xhr.status + ":" + xhr.responseText);
			}
		});
		// body...
	});
//save details to database
 	// $(document).on('submit','#room-form',function(e){
 	// 	e.preventDefault();

 	// 	$.ajax({
 	// 		type:'POST',
 	// 		url:'{% url "students" %}',
 	// 		data:{
 	// 			course:$('#course').val(),
 	// 			year_of_study:$('#year_of_study').val(),
 	// 			unit:$('#unit').val(),
 	// 			rooms:$('#rooms').val(),
 	// 			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
 	// 			action:'post'
 	// 		},
 	// 		success:function(){
 	// 			alert("Saved")

 	// 		}

 	// 	});

 	// });

// $(document).ready(function(){
// 	$(".delete_button").click(function(){
// 		var id = $(this).attr('id');
// 		$.ajax({
// 			type:'DELETE',
// 			url:'{% url "events_delete" %}',
// 			data:{'id':id},
// 			beforeSend: function(xhr){
// 				xhr.setRequestHeader("X-CSRFToken",{% csrf_token %});
// 			},
// 			success:function(response){

// 			}
// 		})
// 	})
// })


// $("#events-form").on("submit", function GetTableData(e){
// 	$(function(){
// 		$("#modal-event").dialog({
// 			autoOpen: false
// 		});
// 		$(".js-create-event").on("click", function(){
// 			$("#modal-event").dialog("open");
// 		});
// 	});
// 	$("submit").click(function(e){
// 		$.ajax({
// 			type:'POST',
// 			// url:'{% url "events" %}',
// 			data:{
// 				title:$('#title').val(),
// 				description:$('#description').val(),
// 				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
// 				action: 'post'

// 			},
// 			success:function(data){
// 				document.getElementById("events-form").reset();
// 				$("#my_events tbody").prepend(
// 					'<tr><td>${fields["title"]||""}</td><td>${fields["description"]||""}</td></tr>'
// 					)    
// 			},
// 			error : function(xhr,errmsg,err){
// 				console.log(xhr.status + ":" + xhr.responseText);
// 			}
// 		});
		
// 	});
// });


 // $("#events-form").on("submit", function GetTableData(e) {
	// 	e.preventDefault();
	// $(function(){
	// 	$("#dialog-link").dialog({
	// 		autoOpen: false,
	// 		show: {
	// 			effect: "blind",
	// 			duration: 1000
	// 		},
	// 		hide: {
	// 			effect: "explode",
	// 			duration: 1000
	// 		}
	// 	});
	// 	$(".js-create-event").on("click", function(event){
	// 		$("#dialog-link").dialog("open");
	// 		event.preventDefault();
	// 	});
	// });

	// 	$.ajax({
	// 		type:'POST',
	// 		// url:'{% url "events" %}',
	// 		data:{
	// 			title:$('#title').val(),
	// 			description:$('#description').val(),
	// 			venue:$('#venue').val(),
	// 			mdate:$('#mdate').val(),
	// 			mtime:$('#mtime').val(),
	// 			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
	// 			action: 'post'

	// 		},
	// 		success:function(data){
	// 			document.getElementById("events-form").reset();
	// 			$("#my_events tbody").prepend(
	// 				'<tr><td>${fields["title"]||""}</td><td>${fields["description"]||""}</td><td>${fields["venue"]||""}</td><td>${fields["mdate"]||""}</td><td>${fields["mtime"]||""}</td></tr>'
	// 				)    
	// 		},
	// 		error : function(xhr,errmsg,err){
	// 			console.log(xhr.status + ":" + xhr.responseText);
	// 		}
	// 	});
	// 	// body...
	// });
 // function deleteEvents(id){
 // 	var action = confirm("Are you sure you want to delete this event?"),
 // 	if (action != false) {
 // 		$.ajax({
 // 			url:'{% url "events_delete" %}',
 // 			data: {
 // 				'id': id,
 // 			},
 // 			dataType: 'json',
 // 			success: function(data){
 // 				if (data.deleted) {
 // 					$("#my_events tbody #event-" +id).remove();
 // 				}
 // 			}
 // 		})
 // 	}
 // }



 // $("#event-form").on("submit", function GetTableData(e) {
	// 	e.preventDefault();
	// $(function(){
	// 	$("#dialog-link").dialog({
	// 		autoOpen: false,
	// 		show: {
	// 			effect: "blind",
	// 			duration: 1000
	// 		},
	// 		hide: {
	// 			effect: "explode",
	// 			duration: 1000
	// 		}
	// 	});
	// 	$(".js-create-event").on("click", function(event){
	// 		$("#dialog-link").dialog("open");
	// 		event.preventDefault();
	// 	});
	// });

	// 	$.ajax({
	// 		type:'POST',
	// 		// url:'{% url "event" %}',
	// 		data:{
	// 			title:$('#title').val(),
	// 			description:$('#description').val(),
	// 			venue:$('#venue').val(),
	// 			mdate:$('#mdate').val(),
	// 			mtime:$('#mtime').val(),
	// 			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
	// 			action: 'post'

	// 		},
	// 		success:function(data){
	// 			document.getElementById("event-form").reset();
	// 			$("#my_event tbody").prepend(
	// 				'<tr><td>${fields["title"]||""}</td><td>${fields["description"]||""}</td><td>${fields["venue"]||""}</td><td>${fields["mdate"]||""}</td><td>${fields["mtime"]||""}</td></tr>'
	// 				)    
	// 		},
	// 		error : function(xhr,errmsg,err){
	// 			console.log(xhr.status + ":" + xhr.responseText);
	// 		}
	// 	});
	// 	// body...
	// });






// $("#event-form").on("submit", function GetTableData(e) {
// 		e.preventDefault();	

// 		$.ajax({
// 			type:'POST',
// 			url:'{% url "event" %}',
// 			data:{
// 				title:$('#title').val(),
// 				description:$('#description').val(),
// 				venue:$('#venue').val(),
// 				mdate:$('#mdate').val(),
// 				mtime:$('#mtime').val(),
// 				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
// 				action: 'post'
	
// 			},
// 			success:function(data){
// 				document.getElementById("event-form").reset();
// 				$("#my_event tbody").prepend(
// 					'<tr><td>${fields["title"]||""}</td><td>${fields["description"]||""}</td><td>${fields["venue"]||""}</td><td>${fields["mdate"]||""}</td><td>${fields["mtime"]||""}</td></tr>'
// 					) 
// 			},
// 			error : function(xhr,errmsg,err){
// 				console.log(xhr.status + ":" + xhr.responseText);
// 			}
// 		});
// 		// body...
// });


// $("form#updateEvent").on("submit",function GetTableData(e) {
// 	e.preventDefault();

// 		$.ajax({
// 			type:'POST',
// 			url:'{% url "events_update" %}',
// 			data:{
// 				title:$('#title').val(),
// 				description:$('#description').val(),
// 				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
// 				action: 'post'
	
// 			},
// 			success:function(data){
// 				if (data.event) {
// 					updateTomy_event(data.event);
// 				}	
// 			}
// 		});

// 	    $('form#updateEvent').trigger("reset");
//         $('#myModal').modal('hide');
//         return false;
// 		// body...
// });
// function editEvent(id) {
// 	if (id) {
// 		tr_id = "#event-" + id;
// 		title = $(tr_id).find(".eventTitle").text();
// 		description = $(tr_id).find(".eventDescription").text();
// 		$('#form-id').val(id);
// 		$('#form-title').val(title);
// 		$('#form-description').val(description);
// 	}
// }
// function updateToeventTable(event){
// 	$("#eventTable #event-" +event.id).children(".eventData").each(function (){
// 		var attr = $(this).attr("title");
// 		if (attr == "title") {
// 			$(this).text(event.title);
// 		}else{
// 			$(this).text(event.description);
// 		}
// 	});
// }

// function deleteEvent(id) {
// 	var action = confirm("Are you sure you want to delete this event?");
// 	if (action != false) {
// 		$.ajax({
// 			url: '{% url "events_delete" %}',
// 			data: {
// 				'id': id,
// 			},
// 			dataType:'json',
// 			success:function(data){
// 				if (data.deleted) {
// 					$("#eventTable #event-" +id).remove();
// 				}
// 			}
// 		});
// 	}
// }
