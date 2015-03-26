var can = 10;
$(function() {
	$('.teamList').first().addClass('nameActive');
	$('.teamContent').hide();
	$('.teamContent').first().fadeIn('fast');
	$('.teamList').each(function() {
		$(this).click(function() {
			$('.teamContent:visible').hide('fast');
			$('#' + $(this).val()).fadeIn('fast');
			$('.teamList').removeClass('nameActive');
			$(this).addClass('nameActive');
		});
	});

	$('.supportButton').each(function() {
		$(this).click(function() {
			if (can < 1) {
				alert('你的支持超过一定限度');
				return;
			}
			var team_id = $(this).attr('alt');
			$.getJSON('/support/',
				{
					'add_id' : team_id,
					'add_type' : 'team', 
				},
				function(data) {
					if (data['message'] == 'success') {
						$('#support' + team_id).text(data['now_support']);
					}
					can -= 1;
				});
		});
	});
});