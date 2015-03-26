$(function() {
	$("#indexPage").addClass("liActive");
	$(".teamButton").hide();
	$(".peopleButton").hide();
	$(".matchButton").hide();

	$("#teamPage").click(function() {
		$(this).siblings().removeClass("liActive");
		$(this).addClass("liActive");
		$(".teamButton").show();
		$(".peopleButton").hide();
		$(".matchButton").hide();
	});

	$("#indexPage").click(function() {
		$(this).siblings().removeClass("liActive");
		$(this).addClass("liActive");
		$(".teamButton").hide();
		$(".peopleButton").hide();
		$(".matchButton").hide();
	});

	$("#peoplePage").click(function() {
		$(this).siblings().removeClass("liActive");
		$(this).addClass("liActive");
		$(".teamButton").hide();
		$(".peopleButton").show();
		$(".matchButton").hide();
	});

	$("#matchPage").click(function() {
		$(this).siblings().removeClass("liActive");
		$(this).addClass("liActive");
		$(".teamButton").hide();
		$(".peopleButton").hide();
		$(".matchButton").show();
	});

});