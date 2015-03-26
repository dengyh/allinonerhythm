$(function() {
	$('#searchText').change(function() {
		$('#searchUser').attr('href', '#' + $('#searchText').val());
	});
});