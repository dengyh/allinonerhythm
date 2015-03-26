$(function() {
	function countDown() {
		var today = new Date();
		var goal = new Date(2014, 5, 13, 4, 0, 0);
		var def = goal - today;
		var day = Math.floor(def / 1000 / 60 / 60 / 24);
		var hour = Math.floor((def - day * 1000 * 60 * 60 * 24) / 1000 / 60 / 60);
		var minute = Math.floor((def - day * 1000 * 60 * 60 * 24 -
			hour * 1000 * 60 * 60) / 1000 / 60);
		var second = Math.floor((def - day * 1000 * 60 * 60 * 24 -
			hour * 1000 * 60 * 60 - minute * 1000 * 60) / 1000);
		$('#countDay').text(day);
		$('#countHour').text(hour);
		$('#countMinute').text(minute);
		$('#countSecond').text(second);
		setTimeout(countDown, 1000);
	}
	countDown();
});