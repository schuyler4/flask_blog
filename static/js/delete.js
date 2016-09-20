
$('#deleteButton').click(function() {
	$.ajax({
		type: "POST",
		url: "/deleteblogpost",
		data: {
			title:$('#deleteButton').parent().val()
		}
	})
	console.log($('#deleteButton'))
});
