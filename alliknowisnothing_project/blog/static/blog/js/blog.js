
var fetchBlogEntry = function(url) {
//	var sample = '/static/blog_entries/2013-12-28_Hello-World.json';
	$.getJSON(url, function(data) {
		$('title').html(data.title);
		$('#title').html(data.title);
		$('#date').html(data.date);
		$('#content').html(data.content);
	});
};

