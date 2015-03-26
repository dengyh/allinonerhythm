var can = true;
$(function() {
	$('.supportPlayer').each(function() {
		$(this).click(function() {
			if (!can) {
				alert('你的支持超过一定限度');
				return;
			}
			var add_id = $(this).attr('alt');
			$.getJSON('/support/',
				{
					'add_id' : add_id,
					'add_type' : 'player', 
				},
				function(data) {
					if (data['message'] == 'success') {
						$('#player' + add_id).text(data['now_support']);
					}
					can = false;
				});
		});
	});

	$('.supportCoach').each(function() {
		$(this).click(function() {
			if (can < 0) {
				alert('你的支持超过一定限度');
				return;
			}
			var add_id = $(this).attr('alt');
			$.getJSON('/support/',
				{
					'add_id' : add_id,
					'add_type' : 'coach', 
				},
				function(data) {
					if (data['message'] == 'success') {
						$('#coach' + add_id).text(data['now_support']);
					}
					can -= 1;
				});
		});
	});
});